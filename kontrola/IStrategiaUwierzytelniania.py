from abc import ABC, abstractmethod
from typing import Optional
from encje.Uzytkownik import Uzytkownik


class IStrategiaUwierzytelniania(ABC):

    @abstractmethod
    def uwierzytelnij(self, email: str, hashHasla: str) -> Uzytkownik:
        """
        Próbuje uwierzytelnić użytkownika.
        Zwraca:
        - obiekt Uzytkownik, jeśli dane logowania są poprawne
        - None, jeśli uwierzytelnienie się nie powiodło
        """
        pass
