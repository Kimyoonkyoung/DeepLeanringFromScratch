# coding: utf-8
from and_gate import AND
from or_gate import OR

def NOT(x):
    if x == 1:
        x = 0
    elif x == 0:
        x = 1

    return x

def exercise(x1, x2):
    notX1 = NOT(x1)
    notX2 = NOT(x2)

    s1 = AND(x1, notX2)
    s2 = AND(notX1, x2)

    y = OR(s1, s2)

    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = exercise(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))