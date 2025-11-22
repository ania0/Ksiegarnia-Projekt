from encje.IKsiazka import IKsiazka

class MagazynKsiazek:
    def __init__(self):
        self._ksiazki = []

    def dodaj(self, ksiazka: IKsiazka):
        self._ksiazki.append(ksiazka)

    def usun(self, id_ksiazki: int):
        self._ksiazki = [k for k in self._ksiazki if getattr(k, 'id', None) != id_ksiazki]

    def pobierz_wszystkie(self):
        return self._ksiazki

    def znajdz_po_id(self, id: int):
        for k in self._ksiazki:
            if getattr(k, 'id', None) == id:
                return k
        return None

    def aktualizuj(self, ksiazka: IKsiazka):
        for i, k in enumerate(self._ksiazki):
            if getattr(k, 'id', None) == getattr(ksiazka, 'id', None):
                self._ksiazki[i] = ksiazka
                return