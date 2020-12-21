from datetime import date


class Person:
    first_name = "name"
    last_name = "surname"
    father_name = "father_name"
    birth_date = date.today()

    def __init__(self):
        self.first_name = "Ivan"
        self.last_name = "Ivanov"
        self.father_name = "Ivanovich"
        self.birth_date = date.today()

    def __init__(self, name, surname, father_name, birth_date):
        self.first_name = name
        self.last_name = surname
        self.father_name = father_name
        self.birth_date = birth_date

    def get_age(self):
        return str(date.today().year - self.birth_date.year)

