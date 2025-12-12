from typing import Optional
from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IKsiazka import IKsiazka
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
import sys  # Dodatkowy import do obsługi błędu


class ZarzadzanieKsiazkami(ProcesZarzadzania):
    """
    Proces zarządzania książkami – PU08–PU12.
    """

    def __init__(self, fasada_encji: Optional[IEncjeFasada] = None, uzytkownik: Optional[Administrator] = None):
        super().__init__(fasada_encji, uzytkownik)
        self._fasada_encji: Optional[IEncjeFasada] = fasada_encji
        self._uzytkownik: Optional[Administrator] = uzytkownik

    def wyswietl_katalog(self):
        # ... (metoda bez zmian)
        ksiazki = self._fasada_encji.pobierzWszystkie() if self._fasada_encji else []
        print("\nKsiążki w katalogu:")
        if ksiazki:
            for k in ksiazki:
                stan = k.stanMagazynowy if isinstance(k, KsiazkaPapierowa) else "-"
                print(f"[ISBN: {k.ISBN}] tytuł: {k.tytul} – {k.autor} – {k.cena} zł (stan: {stan})")
        else:
            print("Brak książek w katalogu.")

    def dodaj_ksiazke(self):
        """Logika dodawania książki (PU09) z walidacją ceny i stanu magazynowego."""
        print("\n--- Dodawanie nowej książki (PU09) ---")
        try:
            tytul = input("Tytuł: ")
            autor = input("Autor: ")

            # Walidacja Ceny
            cena = float(input("Cena: "))
            if cena < 0:
                print("Błąd: Cena musi być nieujemna.")
                return  # Powrót do głównego menu Zarządzania Katalogiem

            ISBN = int(input("ISBN: "))
            typ = input("Typ książki (papierowa/ebook): ").strip().lower()
            gatunek = input("Gatunek: ")
            opis = input("Opis książki: ")

            stanMagazynowy = 0
            sciezkaDoPliku = ""

            if typ == "papierowa":
                # Walidacja Stanu Magazynowego
                stanMagazynowy_input = input("Stan magazynowy książki papierowej: ")
                stanMagazynowy = int(stanMagazynowy_input)
                if stanMagazynowy < 0:
                    print("Błąd: Stan magazynowy musi być nieujemny.")
                    return  # Powrót do głównego menu Zarządzania Katalogiem
            elif typ == "ebook":
                sciezkaDoPliku = input("Ścieżka do pliku ebooka: ")

        except ValueError:
            print("Błąd: Wprowadzono niepoprawny format dla ceny lub stanu magazynowego (oczekiwano liczby).")
            return

        if typ not in ["papierowa", "ebook"]:
            print("Błąd: Nieznany typ książki. Możliwe typy: papierowa, ebook.")
            return

        # Tworzenie i dodawanie książki
        ksiazka: IKsiazka = self._fasada_encji._fabrykaKsiazek.utworzKsiazke(
            typ=typ,
            tytul=tytul,
            autor=autor,
            cena=cena,
            ISBN=ISBN,
            gatunek=gatunek,
            stanMagazynowy=stanMagazynowy,
            opis=opis,
            sciezkaDoPliku=sciezkaDoPliku
        )
        self._fasada_encji.dodajKsiazke(ksiazka)
        print(f"Pomyślnie dodano książkę: {tytul}")

        # Po dodaniu nowej książki przechodzi do menu edycji tej książki
        self.edycja_ksiazki_menu(ksiazka)

    def edycja_ksiazki_menu(self, ksiazka: IKsiazka) -> None:
        """
        Menu do edycji szczegółów wybranej książki z walidacją danych.
        """
        while True:
            print(f"\n--- Edycja Książki: {ksiazka.tytul} [ISBN: {ksiazka.ISBN}] ---")
            print("1. Zmień szczegóły książki (PU10)")
            print("2. Zmień stan magazynowy (tylko dla papierowych) (PU11)")
            print("3. Usuń książkę (PU12)")
            print("4. Powrót do Zarządzania Katalogiem")

            opcja = input("Wybierz opcję: ").strip()

            if opcja == "1":  # PU10 – Edytuj szczegóły z walidacją ceny
                print("\n[Modyfikacja szczegółów. Pomiń, aby zachować starą wartość.]")

                # Zbieranie nowych danych
                nowy_tytul = input(f"Tytuł [{ksiazka.tytul}]: ") or ksiazka.tytul
                nowy_autor = input(f"Autor [{ksiazka.autor}]: ") or ksiazka.autor

                # Walidacja Ceny
                nowa_cena_input = input(f"Cena [{ksiazka.cena}]: ")
                nowa_cena = ksiazka.cena
                if nowa_cena_input:
                    try:
                        nowa_cena = float(nowa_cena_input)
                        if nowa_cena < 0:
                            print("Błąd: Cena musi być nieujemna. Anulowano modyfikację.")
                            continue  # Powrót do menu edycji
                    except ValueError:
                        print("Błąd: Wprowadzono niepoprawny format dla ceny. Anulowano modyfikację.")
                        continue  # Powrót do menu edycji

                nowy_gatunek = input(f"Gatunek [{ksiazka.gatunek}]: ") or ksiazka.gatunek
                nowy_opis = input(f"Opis [{ksiazka.opis}]: ") or ksiazka.opis

                # Aktualizacja pól specyficznych
                if isinstance(ksiazka, KsiazkaPapierowa):
                    nowy_stan_input = input(f"Stan magazynowy [{ksiazka.stanMagazynowy}]: ")
                    if nowy_stan_input:
                        try:
                            temp_stan = int(nowy_stan_input)
                            if temp_stan < 0:
                                print("Błąd: Stan magazynowy musi być nieujemny. Anulowano modyfikację.")
                                continue  # Powrót do menu edycji
                            ksiazka.stanMagazynowy = temp_stan
                        except ValueError:
                            print("Błąd: Niepoprawny format dla stanu magazynowego. Anulowano modyfikację.")
                            continue  # Powrót do menu edycji

                elif isinstance(ksiazka, Ebook):
                    nowa_sciezka_input = input(f"Ścieżka do pliku [{ksiazka.sciezkaDoPliku}]: ")
                    if nowa_sciezka_input:
                        ksiazka.sciezkaDoPliku = nowa_sciezka_input

                # Aktualizacja pól wspólnych
                ksiazka.tytul = nowy_tytul
                ksiazka.autor = nowy_autor
                ksiazka.cena = nowa_cena
                ksiazka.gatunek = nowy_gatunek
                ksiazka.opis = nowy_opis

                self._fasada_encji.aktualizujDane(ksiazka)
                print(f"Pomyślnie zaktualizowano szczegóły książki '{ksiazka.tytul}'")

            elif opcja == "2":  # PU11 – Zmień stan magazynowy z walidacją
                if isinstance(ksiazka, KsiazkaPapierowa):
                    try:
                        nowy_stan_input = input(f"Podaj nowy stan dla '{ksiazka.tytul}': ")
                        nowy_stan = int(nowy_stan_input)

                        if nowy_stan < 0:
                            print("Błąd: Stan magazynowy musi być nieujemny. Powrót do menu edycji.")
                            continue  # Powrót do menu edycji

                        self._fasada_encji.aktualizujStan(ksiazka.ISBN, nowy_stan)
                        ksiazka.stanMagazynowy = nowy_stan
                        print(f"Zaktualizowano stan książki '{ksiazka.tytul}' na {nowy_stan}")
                    except ValueError:
                        print("Błąd: Niepoprawny format liczby dla stanu magazynowego. Powrót do menu edycji.")
                        continue  # Powrót do menu edycji
                else:
                    print("Błąd: Nie można zmienić stanu – tylko książki papierowe mają stan magazynowy.")

            elif opcja == "3":  # PU12 – Usuń książkę (bez zmian)
                potwierdzenie = input(f"Czy na pewno chcesz usunąć książkę '{ksiazka.tytul}'? (t/n): ").lower()
                if potwierdzenie == 't':
                    self._fasada_encji.usunKsiazke(ksiazka.ISBN)
                    print(f"Usunięto książkę '{ksiazka.tytul}' o ISBN {ksiazka.ISBN}")
                    return  # Wracamy do głównego menu Zarządzania Katalogiem

            elif opcja == "4":  # Powrót (bez zmian)
                return

            else:
                print("Niepoprawna opcja, spróbuj ponownie.")

    def zarzadzajKsiazkami(self) -> None:
        # ... (metoda zarzadzajKsiazkami bez zmian, poza zmianami w wywoływanych funkcjach)
        if not self._uzytkownik or not isinstance(self._uzytkownik, Administrator):
            print("Brak uprawnień! Tylko Administrator może zarządzać katalogiem.")
            return

        while True:
            self.wyswietl_katalog()

            print("\n--- Zarządzanie Katalogiem (Menu Główne) ---")
            print("1. Dodaj nową książkę (PU09)")
            print("2. Wybierz książkę (aby edytować/usunąć)")
            print("3. Wyjście z Zarządzania Katalogiem")

            opcja = input("Wybierz opcję: ").strip()

            if opcja == "1":  # Dodaj książkę (PU09)
                self.dodaj_ksiazke()

            elif opcja == "2":  # Wybierz książkę (przechodzi do edycji)
                try:
                    isbn = int(input("Podaj ISBN książki do edycji: "))
                    ksiazka = self._fasada_encji.pobierzPoISBN(isbn)

                    if ksiazka:
                        self.edycja_ksiazki_menu(ksiazka)
                    else:
                        print(f"Błąd: Nie znaleziono książki o ISBN {isbn}. Spróbuj ponownie.")

                except ValueError:
                    print("Błąd: ISBN musi być liczbą całkowitą.")

            elif opcja == "3":  # Wyjście
                print("Kończymy zarządzanie katalogiem.")
                break

            else:
                print("Niepoprawna opcja, spróbuj ponownie.")

        print("\nKatalog książek zaktualizowany.")