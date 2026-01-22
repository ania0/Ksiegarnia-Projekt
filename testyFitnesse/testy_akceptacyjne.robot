*** Settings ***
Library    KlasyTestujace.py    WITH NAME    System

*** Test Cases ***

# ==========================================
# 1. ZARZADZANIE UZYTKOWNIKAMI
# ==========================================

Rejestracja Nowego Uzytkownika
    [Documentation]    Sprawdza, czy mozna zalozyc konto.
    ${wynik}=    System.Stworz Konto    Jan    Testowy    jan@test.pl    haslo123    Wroclaw
    Should Be Equal As Strings    ${wynik}    True

Logowanie Poprawne
    [Documentation]    Sprawdza logowanie poprawnymi danymi.
    ${wynik}=    System.Sprawdz Logowanie    jan@test.pl    haslo123
    Should Be Equal As Strings    ${wynik}    True

Logowanie Bledne Haslo
    [Documentation]    Sprawdza logowanie zlym haslem.
    ${wynik}=    System.Sprawdz Logowanie    jan@test.pl    zlehaslo
    Should Be Equal As Strings    ${wynik}    False

# ==========================================
# 2. ZARZADZANIE KATALOGIEM (CRUD)
# ==========================================

Dodanie Ksiazki Do Katalogu
    [Documentation]    Administrator dodaje nowa ksiazke.
    ${wynik}=    System.Dodaj Ksiazke    Wiedzmin    50.0    9781111111111
    Should Be Equal As Strings    ${wynik}    True

Wyszukiwanie Ksiazki
    [Documentation]    Klient szuka ksiazki w katalogu.
    ${znaleziono}=    System.Czy Ksiazka Istnieje    Wiedzmin
    Should Be Equal As Strings    ${znaleziono}    True

Edycja Ceny Ksiazki
    [Documentation]    Zmiana ceny istniejacej ksiazki.
    ${wynik}=    System.Edytuj Cene Ksiazki    9781111111111    40.0
    Should Be Equal As Strings    ${wynik}    True

    # Weryfikacja czy cena sie zmienila
    ${nowa_cena}=    System.Pobierz Cene Ksiazki    9781111111111
    Should Be Equal As Strings    ${nowa_cena}    40.0

Zmiana Stanu Magazynowego
    [Documentation]    Dostawa towaru - zwiekszenie ilosci.
    ${wynik}=    System.Zmien Stan    9781111111111    100
    Should Be Equal As Strings    ${wynik}    True

    ${stan}=    System.Pobierz Stan    9781111111111
    Should Be Equal As Integers    ${stan}    100

# ==========================================
# 3. PROCES SKLADANIA ZAMOWIEN
# ==========================================

Zamowienie Jako Zalogowany
    [Documentation]    Uzytkownik 'jan@test.pl' kupuje 2 sztuki Wiedzmina.
    # Stan poczatkowy: 100 sztuk
    ${wynik}=    System.Zloz Zamowienie    jan@test.pl    9781111111111    2    False
    Should Be Equal As Strings    ${wynik}    True

    # Sprawdzenie czy stan zmalał (100 - 2 = 98)
    ${stan}=    System.Pobierz Stan    9781111111111
    Should Be Equal As Integers    ${stan}    98

Zamowienie Jako Gosc
    [Documentation]    Nieznany uzytkownik kupuje ksiazke bez logowania.
    ${wynik}=    System.Zloz Zamowienie    gosc@mail.pl    9781111111111    5    True
    Should Be Equal As Strings    ${wynik}    True

    # Sprawdzenie czy stan zmalał (98 - 5 = 93)
    ${stan}=    System.Pobierz Stan    9781111111111
    Should Be Equal As Integers    ${stan}    93

Próba Kupna Zbyt Duzej Ilosci
    [Documentation]    Proba kupna wiecej niz jest w magazynie.
    ${wynik}=    System.Zloz Zamowienie    jan@test.pl    9781111111111    1000    False
    Should Contain    ${wynik}    Error

# ==========================================
# 4. SPRZATANIE
# ==========================================

Usuniecie Ksiazki
    [Documentation]    Usuniecie ksiazki z oferty.
    ${wynik}=    System.Usun Ksiazke    9781111111111
    Should Be Equal As Strings    ${wynik}    True

    ${szukaj}=    System.Czy Ksiazka Istnieje    Wiedzmin
    Should Be Equal As Strings    ${szukaj}    False

Usuniecie Konta
    [Documentation]    Usuniecie uzytkownika po testach.
    ${wynik}=    System.Usun Uzytkownika    jan@test.pl
    Should Be Equal As Strings    ${wynik}    True