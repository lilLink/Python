def G(k, x):
    if (k == 0):
        return 1
    if (k == 1):
        return x
    return (x - 2 * k + 1) * G(k -1, x) - pow(k- 1, 2) * G(k-2, x)

x = int(input("Input x: "))
while True:
    n = int(input("Input n: "))
    if (n >= 0 and n <= 200):
        break

y = [0 for i in range(n)]
for i in range(n):
    y[i] = int(input("Input y[" + str(i) + "]: "))

for k in range(n):
    val = pow(- y[k], k) * G(k, x)
    print("k = " + str(k) + ", " + "y = " + str(y[k]) + " | Value is: " + str(val))