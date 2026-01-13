from typing import Optional


class Uzytkownik:

    def __init__(self, imie: str,
                 nazwisko: str,
                 email: str,
                 hashHasla: Optional[str] = None,
                 adres: Optional[str] = None,
                 id: Optional[int] = None):
        self._waliduj_dane(imie, nazwisko, email)

        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.hashHasla: Optional[str] = hashHasla
        self.email: str = email
        self.adres: Optional[str] = adres
        self.id: Optional[int] = id

    def _waliduj_dane(self, imie, nazwisko, email):
        if not imie.strip() or not nazwisko.strip() or not email.strip():
            raise ValueError("Imię, nazwisko i email są wymagane i nie mogą być puste.")

        if not imie[0].isupper() or not nazwisko[0].isupper():
            raise ValueError("Imię i nazwisko muszą zaczynać się od wielkiej litery.")

        self._sprawdz_format_email(email)

    def _sprawdz_format_email(self, email):
        if "@" not in email:
            raise ValueError("Email musi zawierać znak '@'.")

        czesc_domeny = email.split("@")[-1]
        if "." not in czesc_domeny:
            raise ValueError("Email musi zawierać kropkę po znaku '@'.")

    # GETTERY
    def pobierzId(self) -> Optional[int]:
        return self.id

    def pobierzEmail(self) -> Optional[str]:
        return self.email

# SETTERY
    def ustawImie(self, noweImie: str) -> None:
        if not noweImie.strip() or not noweImie[0].isupper():
            raise ValueError("Błędne imię przy edycji.")
        self.imie = noweImie

    def ustawNazwisko(self, noweNazwisko: str) -> None:
        if not noweNazwisko.strip() or not noweNazwisko[0].isupper():
            raise ValueError("Błędne nazwisko przy edycji.")
        self.nazwisko = noweNazwisko

    def ustawEmail(self, nowyEmail: str) -> None:
        self._sprawdz_format_email(nowyEmail)
        self.email = nowyEmail

    def ustawHaslo(self, noweHaslo: str) -> None:
        if not noweHaslo.strip():
            raise ValueError("Błąd: Haslo nie może byś puste.")
        self.hashHasla = noweHaslo

    def ustawAdres(self, nowyAdres: str) -> None:
        """ustawAdres(nowyAdres: String) : void"""
        self.adres = nowyAdres

    # WERYFIKACJA HASŁA
    def weryfikujHaslo(self, podaneHaslo: str) -> bool:
        if self.hashHasla is None:
            return False
        return podaneHaslo == self.hashHasla  # testowa wersja
