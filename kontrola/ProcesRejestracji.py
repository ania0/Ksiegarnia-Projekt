# W pliku ProcesRejestracji.py

from encje.IEncjeFasada import IEncjeFasada
from encje.Klient import Klient  # Klient dziedziczy z Uzytkownik, więc używamy bardziej specyficznej klasy


class ProcesRejestracji:

    # KOREKTA 1: Konstruktor musi przyjąć Fasade Encji, zgodnie z diagramem
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji
        # Usunięcie zbędnych i błędnych atrybutów: self.___fasada_encji__IEncjeFasada, self._uzytkownik

    # KOREKTA 2: Sygnatura musi przyjąć email i haslo, aby usunąć błąd TypeError
    def wykonajRejestracje(self, email: str, haslo: str) -> None:
        """
        Tworzy obiekt Klient z podanych danych i rejestruje go poprzez Fasade Encji.
        """
        # 1. Walidacja (opcjonalnie)
        if self._fasada_encji.czyIstnieje(email):
            raise ValueError("Konto o podanym adresie email już istnieje.")

        # 2. BEZPOŚREDNIE TWORZENIE ENCJ (Zamiast Fabryki)
        # Zakładamy, że klasa Klient przyjmuje email i hashHasla w konstruktorze
        # Używamy Klienta, ponieważ to on jest rejestrowany.

        # WAŻNE: Musisz upewnić się, że konstruktor Klienta jest poprawny!
        # Poniżej zakładam, że Klient dziedziczy z Uzytkownik i wymaga: imie, nazwisko, email, hashHasla
        # W teście użyjemy prostych wartości, bo mamy tylko email i haslo:

        nowy_klient = Klient(
            imie="Nowy",
            nazwisko="Klient",
            email=email,
            hashHasla=haslo
        )

        # 3. Przekazanie encji do Fasady Encji (rejestrujUzytkownika(uzytkownik: Uzytkownik))
        self._fasada_encji.rejestrujUzytkownika(nowy_klient)

        print(f"Pomyślnie zarejestrowano nowego klienta: {email}")