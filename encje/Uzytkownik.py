# #!/usr/bin/python

class Uzytkownik:
    """Encja użytkownika"""

    def __init__(self, imie=None, nazwisko=None, hashHasla=None, email=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.hashHasla = hashHasla
        self.email = email
