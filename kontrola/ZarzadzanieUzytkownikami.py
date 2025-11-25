from kontrola.ProcesZarzadzania import ProcesZarzadzania
from encje.IEncjeFasada import IEncjeFasada
from encje.Uzytkownik import Uzytkownik

"""
class IEncjeFasada(ABC):


    @abstractmethod
    def rejestrujUzytkownika(self, uzytkownik: Uzytkownik):
        pass

    @abstractmethod
    def znajdzUzytkownikaPoLoginie(self, email: str) -> Uzytkownik:
        pass

    @abstractmethod
    def czyIstnieje(self, email: str) -> bool:
        pass

    @abstractmethod
    def usun(self, idUzytkownika: int):
        pass

    @abstractmethod
    def pobierzDaneUzytkownika(self, idUzytkownika: int) -> Uzytkownik:
        pass
"""

class ZarzadzanieUzytkownikami(ProcesZarzadzania):
    """
    Proces zarządzania użytkownikami.
    Implementacja operacji CRUD na użytkownikach.
    """

    def _wykonajOperacjeNaEncji(self):
        print("ZarzadzanieUzytkownikami: Wykonuję operacje na kontach...")

        # 1. Pobranie wszystkich użytkowników
        wszyscy_uzytkownicy = self._fasada_encji.pobierzWszystkie()
        print(f"Liczba użytkowników w bazie: {len(wszyscy_uzytkownicy)}")

        # 2. Wyświetlenie danych każdego użytkownika
        for uzytkownik in wszyscy_uzytkownicy:
            print(f"- {uzytkownik.imie} {uzytkownik.nazwisko}, email: {uzytkownik.email}, id: {uzytkownik.id}")

        # 3. Przykład: usunięcie użytkownika o konkretnym id (tylko jeśli istnieje)
        if wszyscy_uzytkownicy:
            pierwszy_uzytkownik = wszyscy_uzytkownicy[0]
            print(f"Usuwam użytkownika: {pierwszy_uzytkownik.email}")
            self._fasada_encji.usun(pierwszy_uzytkownik.id)
            print("Użytkownik został usunięty.")
