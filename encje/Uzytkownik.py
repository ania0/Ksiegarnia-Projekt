# #!/usr/bin/python

class Uzytkownik:

    def __init__(self, imie=str, nazwisko=str, hashHasla=str, email=str):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.hashHasla: str = hashHasla
        self.email: str = email
