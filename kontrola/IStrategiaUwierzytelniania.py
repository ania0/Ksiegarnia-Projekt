from abc import ABC, abstractmethod
from encje.Uzytkownik import Uzytkownik


class IStrategiaUwierzytelniania(ABC):
    @abstractmethod
    def uwierzytelnij(self, daneLogowania: str, haslo: str) -> Uzytkownik:
        pass