from typing import Optional
from encje.IEncjeFasada import IEncjeFasada
from encje.Administrator import Administrator
from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IKsiazka import IKsiazka
from encje.KsiazkaPapierowa import KsiazkaPapierowa
from encje.Ebook import Ebook

class ZarzadzanieKsiazkami(ProcesZarzadzania):
    """
    Proces zarządzania książkami – PU08–PU12.
    """

    def __init__(self, fasada_encji: Optional[IEncjeFasada] = None, uzytkownik: Optional[Administrator] = None):
        super().__init__(fasada_encji, uzytkownik)
        self._fasada_encji: Optional[IEncjeFasada] = fasada_encji
        self._uzytkownik: Optional[Administrator] = uzytkownik

    def zarzadzajKsiazkami(self) -> None:
        """PU08 – Zarządzanie katalogiem interaktywnie."""

        if not self._uzytkownik:
            print("Brak uprawnień! Użytkownik nie jest zalogowany.")
            return

        if not isinstance(self._uzytkownik, Administrator):
            print(f"Brak uprawnień! Użytkownik '{self._uzytkownik.email}' nie jest Administratorem.")
            return

        while True:
            print("\nKsiążki w katalogu:")
            ksiazki = self._fasada_encji.pobierzWszystkie() if self._fasada_encji else []
            if ksiazki:
                for k in ksiazki:
                    stan = k.stanMagazynowy if isinstance(k, KsiazkaPapierowa) else "-"
                    print(f"[{k.id}] {k.tytul} – {k.autor} – {k.cena} zł (stan: {stan})")
            else:
                print("Brak książek w katalogu.")

            # Opcje PU09–PU12
            print("\nOpcje:")
            print("1. Dodaj książkę (PU09)")
            print("2. Zmień stan magazynowy ksiazki papierowej (PU11)")
            print("3. Usuń książkę (PU12)")
            print("4. Edytuj szczegóły książki (PU10)")
            print("5. Wyjście z zarządzania katalogiem")


            opcja = input("Wybierz opcję: ").strip()

            if opcja == "1":  # PU09 – dodanie książki
                tytul = input("Tytuł nowej książki: ")
                autor = input("Autor: ")
                cena = float(input("Cena: "))
                ISBN = int(input("ISBN: "))
                typ = input("Typ książki (papierowa/ebook): ").strip().lower()
                gatunek = input("Gatunek: ")
                opis = input("Opis książki: ")

# pytanie czy to dobre rozwiązanie, bo stan magazynowy jest tylko dla papierowej a sciezka dla ebooka
                stanMagazynowy = 0
                sciezkaDoPliku = ""
                if typ == "ebook":
                    sciezkaDoPliku = input("Ścieżka do pliku ebooka: ")
                elif typ == "papierowa":
                    stanMagazynowy = int(input("Stan magazynowy książki papierowej: "))

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
                print(f"Dodano książkę: {tytul}")
            elif opcja == "2":  # PU11 – zmiana stanu magazynowego
                isbn = int(input("Podaj ISBN książki papierowej: "))
                ksiazka = self._fasada_encji.pobierzPoISBN(isbn)
                if ksiazka and isinstance(ksiazka, KsiazkaPapierowa):
                    nowy_stan = int(input(f"Podaj nowy stan dla '{ksiazka.tytul}': "))
                    self._fasada_encji.aktualizujStan(isbn, nowy_stan) # nowy stan sie nie chce nadpisać - nie wiem za bardzo jak to poprawić
                    print(f"Zaktualizowano stan książki '{ksiazka.tytul}' na {nowy_stan}")
                elif ksiazka:
                    print(f"Nie można zmienić stanu ebooka '{ksiazka.tytul}' – tylko książki papierowe mają stan magazynowy.")
                else:
                    print(f"Nie znaleziono książki o ISBN {isbn}")
            elif opcja == "3":  # PU12 – usunięcie książki - dziala
                isbn = int(input("Podaj ISBN książki do usunięcia: "))
                ksiazka = self._fasada_encji.pobierzPoISBN(isbn)
                if ksiazka:
                    self._fasada_encji.usunKsiazke(isbn)
                    print(f"Usunięto książkę '{ksiazka.tytul}' o ISBN {isbn}")
                else:
                    print(f"Nie znaleziono książki o ISBN {isbn}")
            elif opcja == "4":  # PU10 – modyfikacja szczegółów książki, dziala
                isbn = int(input("Podaj ISBN książki do modyfikacji: "))
                ksiazka = self._fasada_encji.pobierzPoISBN(isbn)
                if ksiazka:
                    # Pytamy o nowe wartości; jeśli użytkownik nic nie wpisze, zostaje stara
                    nowy_tytul = input(f"Tytuł [{ksiazka.tytul}]: ") or ksiazka.tytul
                    nowy_autor = input(f"Autor [{ksiazka.autor}]: ") or ksiazka.autor
                    nowa_cena = input(f"Cena [{ksiazka.cena}]: ")
                    nowa_cena = float(nowa_cena) if nowa_cena else ksiazka.cena
                    nowy_gatunek = input(f"Gatunek [{ksiazka.gatunek}]: ") or ksiazka.gatunek
                    nowy_opis = input(f"Opis [{ksiazka.opis}]: ") or ksiazka.opis

                    # Pola specyficzne dla typu książki
                    if isinstance(ksiazka, KsiazkaPapierowa):
                        nowy_stan_input = input(f"Stan magazynowy [{ksiazka.stanMagazynowy}]: ")
                        if nowy_stan_input:
                                ksiazka.stanMagazynowy = int(nowy_stan_input)
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

                    print(f"Zaktualizowano szczegóły książki '{ksiazka.tytul}'")
                else:
                    print(f"Nie znaleziono książki o ISBN {isbn}")
            elif opcja == "5":
                print("Kończymy zarządzanie katalogiem.")
                break
            else:
                print("Niepoprawna opcja, spróbuj ponownie.")

            # Po każdej operacji odśwież listę książek
            ksiazki = self._fasada_encji.pobierzWszystkie() if self._fasada_encji else []

        print("\nKatalog książek zaktualizowany.")
