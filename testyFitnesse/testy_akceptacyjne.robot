*** Settings ***
Library    KlasyTestujace.py

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

    # Zmiana stanu
    ${stan_mag}=    Zmien Stan    12345    50
    Should Be Equal As Integers    ${stan_mag}    50

PU_RABAT: Naliczanie Rabatu Lojalnosciowego
    [Documentation]    Sprawdzenie czy dekorator nalicza rabat
    ${czy_rabat}=    Czy Rabat Zostal Naliczony    100.0
    Should Be Equal As Strings    ${czy_rabat}    True

    # Dokladna cena (zakladajac 10% rabatu)
    ${cena}=    Oblicz Cene Dla Klienta    True    100.0
    Should Be Equal As Strings    ${cena}    90.0