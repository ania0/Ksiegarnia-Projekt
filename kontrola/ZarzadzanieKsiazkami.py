from typing import Optional
from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IKsiazka import IKsiazka
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook
import sys


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

        tytul = input("Tytuł: ").strip()
        autor = input("Autor: ").strip()
        cena_str = input("Cena: ").strip()
        isbn_str = input("ISBN: ").strip()
        typ = input("Typ (papierowa/ebook): ").strip().lower()
        gatunek = input("Gatunek: ").strip()
        opis = input("Opis książki: ").strip()

        # Lista na błędy
        lista_bledow = []

        # WALIDACJA PUSTYCH PÓL
        if not tytul: lista_bledow.append("Tytuł nie może być pusty.")
        if not autor: lista_bledow.append("Autor nie może być pusty.")
        if not gatunek: lista_bledow.append("Gatunek nie może być pusty.")
        if not opis: lista_bledow.append("Opis nie może być pusty.")


        # WALIDACJA WIELKICH LITER
        if tytul and not tytul[0].isupper():
            lista_bledow.append("Tytuł musi zaczynać się od wielkiej litery.")

        if autor:
            czlony = autor.replace('-', ' ').split()
            for czlon in czlony:
                if not czlon[0].isupper():
                    lista_bledow.append(f"Człon autora '{czlon}' musi zaczynać się od wielkiej litery.")

        # WALIDACJA LICZB
        cena = 0.0
        try:
            cena = float(cena_str)
            if cena < 0: lista_bledow.append("Cena nie może być ujemna.")
        except ValueError:
            lista_bledow.append("Cena musi być liczbą (np. 29.99).")

        ISBN = 0
        try:
            ISBN = int(isbn_str)
            if len(str(ISBN)) != 13:
                lista_bledow.append(f"ISBN musi mieć 13 cyfr (wpisano {len(str(ISBN))}).")
        except ValueError:
            lista_bledow.append("ISBN musi składać się wyłącznie z cyfr.")

        # SPRAWDZENIE CZY SĄ JAKIEKOLWIEK BŁĘDY
        if lista_bledow:
            print("BŁĘDY: ")
            for i, blad in enumerate(lista_bledow, 1):
                print(f" {i}. {blad}")
            return

        try:
            ksiazka = self._fasada_encji._fabrykaKsiazek.utworzKsiazke(
                typ=typ, tytul=tytul, autor=autor, cena=cena, ISBN=ISBN,
                gatunek=gatunek, stanMagazynowy=0, opis=opis, sciezkaDoPliku=""
            )
            self._fasada_encji.dodajKsiazke(ksiazka)
            print(f"\n[SUKCES] Pomyślnie dodano książkę: {tytul}")
        except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd przy zapisie: {e}")

    def edycja_ksiazki_menu(self, ksiazka: IKsiazka) -> None:
        """
        Menu do edycji szczegółów wybranej książki.
        """
        while True:
            print(f"\n--- Edycja Książki: {ksiazka.tytul} [ISBN: {ksiazka.ISBN}] ---")
            print("1. Zmień szczegóły książki (PU10)")
            print("2. Zmień stan magazynowy (tylko dla papierowych) (PU11)")
            print("3. Usuń książkę (PU12)")
            print("4. Powrót")

            opcja = input("Wybierz opcję: ").strip()

            if opcja == "1":  # PU10
                print("\n[Modyfikacja szczegółów. Wciśnij Enter, aby pominąć.]")

                nowy_tytul = input(f"Tytuł [{ksiazka.tytul}]: ") or None
                nowy_autor = input(f"Autor [{ksiazka.autor}]: ") or None
                nowy_gatunek = input(f"Gatunek [{ksiazka.gatunek}]: ") or None
                nowy_opis = input(f"Opis [{ksiazka.opis}]: ") or None

                nowa_cena_str = input(f"Cena [{ksiazka.cena}]: ")
                nowa_cena = float(nowa_cena_str) if nowa_cena_str else None


                if isinstance(ksiazka, Ebook):
                    sciezka = input(f"Ścieżka [{ksiazka.sciezkaDoPliku}]: ")
                    if sciezka: ksiazka.sciezkaDoPliku = sciezka  # To poza diagramem, zostawiamy tutaj

                lista_bledow = []

                if nowy_tytul and not nowy_tytul[0].isupper()  :
                    lista_bledow.append("Tytuł musi zaczynać się od wielkiej litery.")

                if nowy_autor:
                    czlony = nowy_autor.replace('-', ' ').split()
                    for czlon in czlony:
                        if not czlon[0].isupper():
                            lista_bledow.append(f"Człon autora '{czlon}' musi zaczynać się od wielkiej litery.")

                if nowa_cena_str:
                    try:
                        cena_val = float(nowa_cena_str)
                        if cena_val < 0:
                            lista_bledow.append("Cena nie może być ujemna.")
                    except ValueError:
                        lista_bledow.append("Cena musi być liczbą (np. 29.99).")

                if lista_bledow:
                    print("BŁĘDY :")
                    for i, blad in enumerate(lista_bledow, 1):
                        print(f" {i}. {blad}")
                    return

                wynik = self._fasada_encji.aktualizujDane(
                ksiazka, nowy_tytul, nowy_autor, nowy_gatunek, nowa_cena, nowy_opis
                )

                if wynik == "UjemnaCena":
                    print("Błąd: Cena nie może być ujemna (zgodnie z walidacją w systemie).")
                else:
                    print(f"Pomyślnie zaktualizowano szczegóły książki.")

            elif opcja == "2":  # PU11
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