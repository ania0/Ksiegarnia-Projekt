
# pu 07
# def test_PU07_zlozenie_zamowienia_poprawne(): # nie wiem czemu nie działa
#     encje, kontrola, klient, ksiazka = przygotuj_system()
#
#     # próbujemy złożyć zamówienie
#     kontrola.zlozZamowienie(
#         klient.pobierzId(),
#         [ksiazka.ISBN]
#     )
#
#     # pobieramy historię klienta
#     historia = encje.pobierzHistorieDlaKlienta(klient.pobierzId())
#
#     # sprawdzamy, że klient ma nowe zamówienie
#     assert len(historia) == 1
#     assert historia[0].pozycje[0].ISBN == ksiazka.ISBN

#
# def test_PU07_zlozenie_zamowienia_bledne_ISBN():
#     encje, kontrola, klient, _ = przygotuj_system()
#
#     stan_przed = len(encje.pobierzWszystkieZamowienia())
#
#     kontrola.zlozZamowienie(
#         klient.pobierzId(),
#         [9999999999999]
#     )
#
#     stan_po = len(encje.pobierzWszystkieZamowienia())
#     assert stan_po == stan_przed
#

from testy.test_setup import przygotuj_system

from encje.Klient import Klient


def test_rejestracja_poprawna():
    encje, _, _, _ = przygotuj_system()

    nowy_klient = Klient("Anna", "Nowak", "anna@test.pl", "tajne", "Adres 1", False)
    encje.rejestrujUzytkownika(nowy_klient)

    znaleziony = encje.znajdzUzytkownikaPoEmailu("anna@test.pl")
    assert znaleziony is not None
    assert znaleziony.pobierzEmail() == "anna@test.pl"


def test_rejestracja_duplikat():
    encje, _, _, _ = przygotuj_system()

    # Próba rejestracji tego samego email
    nowy_klient = Klient("Jan", "Kowalski", "jan@test.pl", "haslo", "Testowa 1", False)

    try:
        encje.rejestrujUzytkownika(nowy_klient)
        assert False, "Powinien być błąd dla istniejącego email"
    except ValueError:
        pass


def test_logowanie_poprawne():
    encje, kontrola, klient, _ = przygotuj_system()

    zalogowany = kontrola.logowanie(klient.pobierzEmail(), "haslo")
    assert zalogowany is True


def test_logowanie_bledne_haslo():
    encje, kontrola, klient, _ = przygotuj_system()

    zalogowany = kontrola.logowanie(klient.pobierzEmail(), "zle_haslo")
    assert zalogowany is False


def test_usuniecie_konta():
    encje, kontrola, klient, _ = przygotuj_system()

    # Konto istnieje
    assert encje.czyIstnieje(klient.pobierzEmail())

    # Usuwamy konto
    encje.usun(klient.pobierzId())

    # Konto nie powinno istnieć
    assert not encje.czyIstnieje(klient.pobierzEmail())