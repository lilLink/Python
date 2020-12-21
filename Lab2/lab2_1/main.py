import numpy as np

n = int(input("Enter size of matrix: "))
X = np.array([[int(v) for v in input().split()] for _ in range(n)])
Y = [[X[i].dot(X[:,j]) for j in range(n)]  for i in range(n)]
print(Y)
