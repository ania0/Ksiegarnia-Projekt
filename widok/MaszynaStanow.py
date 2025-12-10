def widok_maszyna_stanow(fasada_kontroli, encje_fasada):
    STAN = "START"

    while True:

        # -----------------------------------------
        # START → STRONA_GŁÓWNA
        # -----------------------------------------
        if STAN == "START":
            print("\n[START] Uruchomiono aplikację.")
            STAN = "STRONA_GŁÓWNA"
            continue

        # -----------------------------------------
        # STRONA GŁÓWNA
        # -----------------------------------------
        elif STAN == "STRONA_GŁÓWNA":
            print("\n=== STRONA GŁÓWNA ===")
            print("1. Logowanie")
            print("2. Zarządzanie katalogiem")
            print("3. Zamknij program")

            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                STAN = "LOGOWANIE"
                continue
            elif wybor == "2":
                STAN = "ZARZĄDZANIE_KATALOGIEM"
                continue
            elif wybor == "3":
                STAN = "KONIEC"
                continue
            else:
                print("Niepoprawny wybór!")
                continue

        # -----------------------------------------
        # LOGOWANIE
        # -----------------------------------------
        elif STAN == "LOGOWANIE":
            print("\n=== LOGOWANIE ===")

            print("1. Cofnij")
            print("2. Zamknij program")
            print("3. Zaloguj")

            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                STAN = "STRONA_GŁÓWNA"
                continue
            elif wybor == "2":
                STAN = "KONIEC"
                continue
            elif wybor == "3":
                email = input("Email: ")
                haslo = input("Hasło: ")
                try:
                    wynik = fasada_kontroli.zalogujKlienta(haslo, email)
                    print(f"Zalogowano: {wynik.imie} {wynik.nazwisko}")
                except:
                    print("BŁĄD: Niepoprawne dane logowania.")
                continue
            else:
                print("Niepoprawny wybór!")
                continue

        # -----------------------------------------
        # ZARZĄDZANIE KATALOGIEM
        # -----------------------------------------
        elif STAN == "ZARZĄDZANIE_KATALOGIEM":
            print("\n=== ZARZĄDZANIE KATALOGIEM ===")

            print("1. Cofnij")
            print("2. Zamknij program")
            print("3. (PRZYKŁAD) Wyświetl wszystkie książki")

            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                STAN = "STRONA_GŁÓWNA"
                continue
            elif wybor == "2":
                STAN = "KONIEC"
                continue
            elif wybor == "3":
                try:
                    ksiazki = fasada_kontroli.przegladajKsiazki()
                    print("Książki w katalogu:")
                    for k in ksiazki:
                        print(f" - {k.tytul} ({k.ISBN})")
                except:
                    print("Brak implementacji PU04.")
                continue
            else:
                print("Niepoprawny wybór!")
                continue


        elif STAN == "KONIEC":
            print("\nZamknięto program.")
            break
