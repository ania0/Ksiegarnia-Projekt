from abc import ABC, abstractmethod
from encje.modele import Uzytkownik # Ważny import!

class IStrategiaUwierzytelniania(ABC):
    @abstractmethod
    def uwierzytelnij(self, daneLogowania: str, haslo: str) -> Uzytkownik:
        pass