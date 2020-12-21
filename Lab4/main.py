import datetime

from Retiree import Retiree


def avg_age(sex):
    gen = people[sex]
    avg_a = 0
    for p in gen:
        avg_a += p.ret_age
    return avg_a / len(gen)


people = {}
print('How many people you wold like to add')
n = int(input())
a = []
b = []
for i in range(0, n):
    print('Person number ', i)
    print('Enter Name: ')
    name = input()
    print('Enter Surname: ')
    surname = input()
    print('Enter Fathers name: ')
    father_name = input()

    print('Enter Ret age: ')
    ret_age = input()
    print('Enter sex: ')
    sex = input()
    print('Enter pension: ')
    pension = input()
    print('Enter experience: ')
    experience = input()
    print('Enter Birth day: ')
    birth_day = datetime.datetime.strptime(input(), '%d.%m.%Y').date()
    if sex == 'female':
        a.append(Retiree(name, surname, father_name, birth_day, ret_age, sex, pension, experience))
        people['female'] = b
    else:
        b.append(Retiree(name, surname, father_name, birth_day, ret_age, sex, pension, experience))
        people['male'] = b


print('Which gender you would like to inspect? ')
gender = input()
temp = people['male'][0]
print('Average age: ', avg_age(gender))
print('Pension: ', temp.get_pension())
