import numpy as np

X = np.array([[51,55], [14,19], [0,4]])

print(X)

print(X[0])

print(X[0][1])

for row in X:
    print(row)

X = X.flatten()
print(X)

print(X > 15)

print(X[X>15])