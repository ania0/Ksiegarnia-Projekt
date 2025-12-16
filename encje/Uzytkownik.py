from typing import Optional


class Uzytkownik:

    def __init__(self, imie: str,
                 nazwisko: str,
                 email: str,
                 hashHasla: Optional[str] = None,
                 adres: Optional[str] = None,
                 id: Optional[int] = None):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.hashHasla: Optional[str] = hashHasla
        self.email: str = email
        self.adres: Optional[str] = adres
        self.id: Optional[int] = id

    # GETTERY
    def pobierzId(self) -> Optional[int]:
        return self.id

    def pobierzEmail(self) -> Optional[str]:
        return self.email

# SETTERY
    def ustawImie(self, noweImie: str) -> None:
        """ustawImie(noweImie: String) : void"""
        self.imie = noweImie

    def ustawNazwisko(self, noweNazwisko: str) -> None:
        """ustawNazwisko(noweNazwisko: String) : void"""
        self.nazwisko = noweNazwisko

    def ustawEmail(self, nowyEmail: str) -> None:
        """ustawEmail(nowyEmail: String) : void"""
        self.email = nowyEmail

    def ustawHaslo(self, noweHaslo: str) -> None:
        """ustawHaslo(noweHaslo: String) : void"""
        self.hashHasla = noweHaslo

    def ustawAdres(self, nowyAdres: str) -> None:
        """ustawAdres(nowyAdres: String) : void"""
        self.adres = nowyAdres

    # WERYFIKACJA HASŁA
    def weryfikujHaslo(self, podaneHaslo: str) -> bool:
        if self.hashHasla is None:
            return False
        return podaneHaslo == self.hashHasla  # testowa wersja
