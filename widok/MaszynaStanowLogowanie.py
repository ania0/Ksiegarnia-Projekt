def maszyna_logowania(fasada_kontroli):

    STAN = "START"

    while True:

        # ============================
        # START
        # ============================
        if STAN == "START":
            print("\n=== START ===")
            print("1. Logowanie")
            print("2. Wyjście")
            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "PANEL_LOGOWANIA"
            elif wybor == "2":
                print("Zamknięto program.")
                return
            else:
                print("Nieprawidłowy wybór!")
            continue


        # ============================
        # PANEL LOGOWANIA
        # ============================
        if STAN == "PANEL_LOGOWANIA":
            print("\n=== PANEL LOGOWANIA ===")
            print("1. Cofnij")
            print("2. Zaloguj klienta")
            print("3. Zaloguj administratora")
            print("4. Stwórz konto")

            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "START"

            elif wybor == "2":
                STAN = "LOGOWANIE_KLIENTA"

            elif wybor == "3":
                STAN = "LOGOWANIE_ADMINA"

            elif wybor == "4":
                STAN = "REJESTRACJA"

            else:
                print("Nieprawidłowy wybór!")
            continue


        # ============================
        # PANEL REJESTRACJI
        # ============================
        if STAN == "REJESTRACJA":
            print("\n=== REJESTRACJA ===")
            print("1. Cofnij")
            print("2. Zarejestruj konto")

            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "PANEL_LOGOWANIA"
                continue

            elif wybor == "2":
                email = input("Podaj email: ")
                haslo = input("Podaj hasło: ")

                try:
                    fasada_kontroli.stworzKonto(haslo, email)
                    print("\nKonto utworzone poprawnie!")
                    STAN = "SUKCES"
                except Exception as e:
                    print(f"\nBłąd podczas rejestracji: {e}")
                    STAN = "BLAD"

            continue


        # ============================
        # LOGOWANIE KLIENTA
        # ============================
        if STAN == "LOGOWANIE_KLIENTA":
            print("\n=== LOGOWANIE KLIENTA ===")
            print("1. Cofnij")
            print("2. Zaloguj")

            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "PANEL_LOGOWANIA"
                continue

            elif wybor == "2":
                email = input("Email: ")
                haslo = input("Hasło: ")

                try:
                    fasada_kontroli.zalogujKlienta(haslo, email)
                    print("\nZalogowano klienta!")
                    STAN = "SUKCES"
                except Exception as e:
                    print(f"\nBłąd logowania: {e}")
                    STAN = "BLAD"

            continue


        # ============================
        # LOGOWANIE ADMINISTRATORA
        # ============================
        if STAN == "LOGOWANIE_ADMINA":
            print("\n=== LOGOWANIE ADMINISTRATORA ===")
            print("1. Cofnij")
            print("2. Zaloguj")

            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "PANEL_LOGOWANIA"
                continue

            elif wybor == "2":
                email = input("Email: ")
                haslo = input("Hasło: ")

                try:
                    fasada_kontroli.zalogujAdministratora(haslo, email)
                    print("\nZalogowano administratora!")
                    STAN = "SUKCES"
                except Exception as e:
                    print(f"\nBłąd logowania: {e}")
                    STAN = "BLAD"

            continue


        # ============================
        # SUKCES
        # ============================
        if STAN == "SUKCES":
            print("\n=== SUKCES ===")
            print("1. OK (powrót do panelu logowania)")
            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "PANEL_LOGOWANIA"
            else:
                print("Nieprawidłowy wybór!")

            continue


        # ============================
        # BŁĄD
        # ============================
        if STAN == "BLAD":
            print("\n=== BŁĄD ===")
            print("1. OK (powrót do panelu logowania)")
            wybor = input("Wybór: ")

            if wybor == "1":
                STAN = "PANEL_LOGOWANIA"
            else:
                print("Nieprawidłowy wybór!")

            continue
