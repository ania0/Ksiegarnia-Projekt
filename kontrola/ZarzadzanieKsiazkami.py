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
        Menu do edycji szczegółów wybranej książki.
        Dostosowane do diagramu: przekazuje dane do Fasady, nie ustawia ich tu.
        """
        while True:
            print(f"\n--- Edycja Książki: {ksiazka.tytul} [ISBN: {ksiazka.ISBN}] ---")
            print("1. Zmień szczegóły książki (PU10)")
            print("2. Zmień stan magazynowy (tylko dla papierowych) (PU11)")
            print("3. Usuń książkę (PU12)")
            print("4. Powrót")

            opcja = input("Wybierz opcję: ").strip()

            if opcja == "1":  # PU10 – Zgodne z Diagramem
                print("\n[Modyfikacja szczegółów. Wciśnij Enter, aby pominąć.]")

                # Zbieramy dane (jako stringi lub None)
                nowy_tytul = input(f"Tytuł [{ksiazka.tytul}]: ") or None
                nowy_autor = input(f"Autor [{ksiazka.autor}]: ") or None
                nowy_gatunek = input(f"Gatunek [{ksiazka.gatunek}]: ") or None
                nowy_opis = input(f"Opis [{ksiazka.opis}]: ") or None

                nowa_cena_str = input(f"Cena [{ksiazka.cena}]: ")
                nowa_cena = float(nowa_cena_str) if nowa_cena_str else None

                # Specjalne pola (poza diagramem, ale potrzebne dla spójności)
                if isinstance(ksiazka, Ebook):
                    sciezka = input(f"Ścieżka [{ksiazka.sciezkaDoPliku}]: ")
                    if sciezka: ksiazka.sciezkaDoPliku = sciezka  # To poza diagramem, zostawiamy tutaj

                # Wywołanie Fasady zgodnie z diagramem
                wynik = self._fasada_encji.aktualizujDane(
                    ksiazka, nowy_tytul, nowy_autor, nowy_gatunek, nowa_cena, nowy_opis
                )

                if wynik == "UjemnaCena":
                    print("❌ Błąd: Cena nie może być ujemna (zgodnie z walidacją w systemie).")
                else:
                    print(f"Pomyślnie zaktualizowano szczegóły książki.")

            elif opcja == "2":  # PU11
                # ... (Reszta bez zmian, bo to inny przypadek użycia)
                if isinstance(ksiazka, KsiazkaPapierowa):
                    try:
                        stan = int(input(f"Nowy stan [{ksiazka.stanMagazynowy}]: "))
                        if stan < 0: print("Błąd: Stan ujemny."); continue
                        self._fasada_encji.aktualizujStan(ksiazka.ISBN, stan)
                        ksiazka.stanMagazynowy = stan
                        print("Zaktualizowano stan.")
                    except ValueError:
                        print("Błąd formatu.")
                else:
                    print("To nie jest książka papierowa.")

            elif opcja == "3":  # PU12
                if input("Potwierdzasz usunięcie? (t/n): ") == 't':
                    self._fasada_encji.usunKsiazke(ksiazka.ISBN)
                    print("Usunięto.");
                    return
            elif opcja == "4":
                return
            else:
                print("Niepoprawna opcja.")

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