from datetime import date
from Person import Person


class Retiree(Person):
    ret_age = 1
    sex = 'male'
    pension = 1
    experience = 1

    def __init__(self, name, surname, father_name, birth_date, ret_age, sex, pension, experience):
        self.ret_age = int(ret_age)
        self.sex = sex
        self.pension = int(pension)
        self.experience = experience
        Person.__init__(self, name, surname, father_name, birth_date)

    def get_pension(self):
        if date.today().month < self.birth_date.month:
            a = int(((date.today().year - self.birth_date.year) - self.ret_age - 1)) * 12
            a += int(date.today().month - self.birth_date.month)
            print(a)
            return int(a * self.pension)
        else:
            a = int(((date.today().year - self.birth_date.year) - self.ret_age)) * 12
            a += int(date.today().month - self.birth_date.month)
            print(a * self.pension)
            return int(a * self.pension)

    def print_retiree(self):
        print(self.last_name, ' ', self.first_name, ' ', self.sex, ' ', self.pension)
