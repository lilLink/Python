import math

x = float(input("Enter x = "))
i = 1
fact = 1
a = list()

while i < 100:
    fact = pow(fact,2)
    math.factorial(fact)
    a.append((pow(x,2*i)*math.sin(pow(x,i)))/fact)
    i+=1
print(a[3])