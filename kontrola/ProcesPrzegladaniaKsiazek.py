from encje.IEncjeFasada import IEncjeFasada
from typing import List
from encje.IKsiazka import IKsiazka
class ProcesPrzegladaniaKsiazek:
    def __init__(self, fasada_encji: IEncjeFasada):
        self._fasada_encji = fasada_encji

    def wykonajPrzegladanieKsiazek(self) -> List[IKsiazka]:
        """
        Pobiera listę wszystkich książek i wyświetla ją w terminalu.
        """
        lista_ksiazek = self._fasada_encji.pobierzWszystkie()

        print("Lista dostępnych książek:")
        for ksiazka in lista_ksiazek: # tu zmienilam bo byl blad
            print(f"tytuł: {ksiazka.tytul} autor: {ksiazka.autor} cena: {ksiazka.cena} zł")

        return lista_ksiazek