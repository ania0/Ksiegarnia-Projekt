from SetUp import SetUp


class KlasyTestujace:
    def __init__(self, *args, **kwargs):
        pass

    # --- Metoda pomocnicza do walidacji ISBN ---
    def _napraw_isbn(self, isbn):
        """
        Dostosowuje ISBN z testów (np. 12345) do wymagań klasy KsiazkaPapierowa (13 cyfr).
        Jeśli ISBN jest za krótki, dopełnia go zerami.
        """
        s_isbn = str(int(isbn))
        if len(s_isbn) < 13:
            # Dopełniamy zerami z prawej strony, np. 12345 -> 1234500000000
            return int(s_isbn.ljust(13, '0'))
        return int(s_isbn)

    # --- Operacje sprawdzające stan ---
    def stan_uzytkownikow(self):
        return int(SetUp.Inwentarz.ileUzytkownikow())

    def stan_ksiazek(self):
        return len(SetUp.Inwentarz.pobierzWszystkie())

    # --- PU01: Rejestracja ---
    def stworz_konto(self, imie, nazwisko, email, haslo, adres):
        stan_p = self.stan_uzytkownikow()
        try:
            from encje.Klient import Klient
            n = Klient(imie, nazwisko, email, haslo, adres, False)
            SetUp.Inwentarz.rejestrujUzytkownika(n)
        except Exception as e:
            return f"False: {e}"
        return "True" if self.stan_uzytkownikow() > stan_p else "False"

    # --- PU03: Usuwanie użytkownika ---
    def usun_uzytkownika(self, email):
        stan_p = self.stan_uzytkownikow()
        u = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email)
        if u:
            SetUp.Inwentarz.usun(u.id)
        return "True" if self.stan_uzytkownikow() < stan_p else "False"

    # --- PU09: Dodawanie książek ---
    def dodaj_ksiazke(self, typ, tytul, autor, cena, isbn, gatunek):
        stan_p = self.stan_ksiazek()
        try:
            from encje.FabrykaKsiazek import FabrykaKsiazek
            fabryka = FabrykaKsiazek()

            # 1. Mapowanie typu (test wysyła "papier", aplikacja chce "ksiazka_papierowa")
            typ_faktyczny = typ
            if str(typ).lower() == "papier":
                typ_faktyczny = "papierowa"

            # 2. Naprawa ISBN (test wysyła 12345, aplikacja chce 13 cyfr)
            valid_isbn = self._napraw_isbn(isbn)

            # 3. Ustawienie ścieżki (dla ebooków)
            sciezka = "file.pdf" if str(typ).lower() == "ebook" else ""

            # 4. Utworzenie książki z 9 argumentami i poprawnymi danymi
            ksiazka = fabryka.utworzKsiazke(
                typ_faktyczny,
                tytul,
                autor,
                float(cena),
                valid_isbn,  # <-- Używamy naprawionego ISBN
                gatunek,
                10,
                "Opis testowy",  # <-- Wymagany przez _waliduj_niepuste
                sciezka
            )
            SetUp.Inwentarz.dodajKsiazke(ksiazka)
        except Exception as e:
            return f"False: {e}"

        return "True" if self.stan_ksiazek() > stan_p else "False: Stan licznika sie nie zmienil"

    # --- PU11: Zmiana stanu magazynowego ---
    def zmien_stan(self, isbn, nowy_stan):
        try:
            # Tutaj też musimy użyć naprawionego ISBN, żeby znaleźć książkę,
            # którą dodaliśmy przed chwilą (jako 1234500000000).
            valid_isbn = self._napraw_isbn(isbn)

            SetUp.Inwentarz.aktualizujStan(valid_isbn, int(nowy_stan))
            k = SetUp.Inwentarz.pobierzPoISBN(valid_isbn)
            return str(k.stanMagazynowy)
        except Exception as e:
            return f"Błąd: {e}"

    # --- Zadanie 2: Rabat Lojalnościowy ---
    def oblicz_cene_dla_klienta(self, czy_lojalny, cena_bazowa):
        from encje.Klient import Klient
        from encje.Zamowienie import Zamowienie

        lojalny = str(czy_lojalny).lower() == "true"
        k = Klient("T", "U", "t@u.pl", "h", "ul. T", lojalny)
        z = Zamowienie()

        # Mock Produktu dostosowany do wymogów Zamowienia i Dekoratora
        class Produkt:
            def __init__(self, c):
                self.c = float(c)
                self.ilosc = 1
                self.cenaJednostkowa = float(c)
                self.cena = float(c)

            def obliczCene(self):
                return self.c

        z.dodajPozycje(Produkt(cena_bazowa))

        try:
            wynik = SetUp.Inwentarz.obliczCeneOstateczna(z, k)
            return str(float(wynik))
        except Exception as e:
            return f"Error: {e}"

    def czy_rabat_zostal_naliczony(self, cena_bazowa):
        cena_po = self.oblicz_cene_dla_klienta("True", cena_bazowa)
        if "Error" in cena_po:
            return "False"
        return "True" if float(cena_po) < float(cena_bazowa) else "False"