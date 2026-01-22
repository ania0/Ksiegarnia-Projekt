*** Settings ***
Library    KlasyTestujace.py    WITH NAME    KlasyTestujace

*** Test Cases ***

PU01 & PU03: Zarzadzanie Uzytkownikami
    [Documentation]    Rejestracja i usuwanie konta
    ${wynik}=    Stworz Konto    Anna    Kuras    a@k.pl    h123    Wroc
    Should Be Equal As Strings    ${wynik}    True
    ${stan}=    Stan Uzytkownikow
    Should Be Equal As Integers    ${stan}    1

    # Test usuwania
    ${usun}=    Usun Uzytkownika    a@k.pl
    Should Be Equal As Strings    ${usun}    True
    ${stan_final}=    Stan Uzytkownikow
    Should Be Equal As Integers    ${stan_final}    0

PU09 & PU11: Katalog i Magazyn
    [Documentation]    Dodawanie ksiazki i zmiana jej ilosci
    ${dodaj}=    Dodaj Ksiazke    papier    Clean Code    Martin    60.0    12345    IT
    Should Be Equal As Strings    ${dodaj}    True

    # Zmiana stanu - Python musi zwrocic nowa ilosc (50), a nie "True"
    ${stan_mag}=    Zmien Stan    12345    50
    Should Be Equal As Integers    ${stan_mag}    50

PU_RABAT: Naliczanie Rabatu Lojalnosciowego
    [Documentation]    Sprawdzenie czy dekorator nalicza rabat. Argumenty: CzyLojalny Cena
    # Sprawdzamy cene dla Klienta Lojalnego (True) dla ksiazki za 100.0
    ${cena_lojalny}=    Oblicz Cene Dla Klienta    True    100.0
    # Oczekujemy 90.0 (zakladajac 10% rabatu)
    Should Be Equal As Strings    ${cena_lojalny}    90.0

    # Sprawdzamy cene dla Goscia (False) dla ksiazki za 100.0
    ${cena_gosc}=    Oblicz Cene Dla Klienta    False    100.0
    # Oczekujemy 100.0 (brak rabatu)
    Should Be Equal As Strings    ${cena_gosc}    100.0