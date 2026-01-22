from SetUp import SetUp


class KlasyTestujace:
    def __init__(self, *args, **kwargs):
        pass

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
        except:
            return "False"
        return "True" if self.stan_uzytkownikow() > stan_p else "False"

    # --- PU03: Usuwanie użytkownika ---
    def usun_uzytkownika(self, email):
        stan_p = self.stan_uzytkownikow()
        u = SetUp.Inwentarz.znajdzUzytkownikaPoEmailu(email)
        if u:
            SetUp.Inwentarz.usun(u.id)
        return "True" if self.stan_uzytkownikow() < stan_p else "False"

#PU09 - dodawanie ksiazek
    def dodaj_ksiazke(self, typ, tytul, autor, cena, isbn, gatunek):
        stan_p = self.stan_ksiazek()
        try:
            ksiazka = SetUp.Inwentarz.fabryka.stworz(
                typ, tytul, autor, float(cena), int(isbn), gatunek, 10
            )
            SetUp.Inwentarz.dodajKsiazke(ksiazka)
        except Exception as e:
            print(e)
            return "False"

        return "True" if self.stan_ksiazek() > stan_p else "False"

    # --- PU11: Zmiana stanu magazynowego ---
    def zmien_stan(self, isbn, nowy_stan):
        try:
            SetUp.Inwentarz.aktualizujStan(int(isbn), int(nowy_stan))
            k = SetUp.Inwentarz.pobierzPoISBN(int(isbn))
            return str(k.stanMagazynowy)
        except:
            return "Błąd"

    # --- Zadanie 2: Rabat Lojalnościowy ---
    def oblicz_cene_dla_klienta(self, czy_lojalny, cena_bazowa):
        from encje.Klient import Klient
        from encje.Zamowienie import Zamowienie
        lojalny = str(czy_lojalny).lower() == "true"
        k = Klient("T", "U", "t@u.pl", "h", "ul. T", lojalny)
        z = Zamowienie(k)

        class Produkt:
            def __init__(self, c): self.c = float(c)

            def obliczCene(self): return self.c

        z.dodajPozycje(Produkt(cena_bazowa))
        return str(float(SetUp.Inwentarz.obliczCeneOstateczna(z, k)))

    def czy_rabat_zostal_naliczony(self, cena_bazowa):
        cena_po = self.oblicz_cene_dla_klienta("True", cena_bazowa)
        return "True" if float(cena_po) < float(cena_bazowa) else "False"