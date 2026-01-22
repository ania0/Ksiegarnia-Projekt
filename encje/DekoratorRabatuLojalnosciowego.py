from encje.DekoratorCenyZamowienia import DekoratorCenyZamowienia
from encje.Klient import Klient

class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):
    def __init__(self, komponent):
        super().__init__(komponent)

    def obliczCene(self) -> float:
        baza = self._komponent.obliczCene()
        print(f">>> DekoratorRabatuLojalnosciowego: nakładam testowy rabat 10% na {baza}")
        return baza * 0.9
