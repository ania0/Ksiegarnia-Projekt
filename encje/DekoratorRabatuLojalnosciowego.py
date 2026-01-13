from encje.DekoratorCenyZamowienia import DekoratorCenyZamowienia
from encje.Klient import Klient

class DekoratorRabatuLojalnosciowego(DekoratorCenyZamowienia):

    def obliczCene(self) -> float:
        baza = self._komponent.obliczCene()
        print(f">>> DekoratorRabatuLojalnosciowego: nakładam testowy rabat 10% na {baza}")
        return baza * 0.9