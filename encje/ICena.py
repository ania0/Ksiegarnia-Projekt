from abc import ABC, abstractmethod  # do tworzenia interf/klas abstrakt

# Klasy implementujące ten interfejs muszą dostarczyć metodę obliczCene().
class ICena(ABC):

    # met abstrakt - brak implementacji
    # każda kl dziedzicząca musi ją nadpisać
    @abstractmethod
    def obliczCene(self) -> float:
        pass

