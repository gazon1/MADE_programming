Debug = False
from collections import defaultdict
from math import factorial as fac


def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom


def solve(dots):
    if Debug:
        print("dots:", dots)
    for key, value in dots.items():
        dots[key] = sorted(value)
    values = list(dots.values())
    res = 0
    for idx1, v1 in enumerate(values[:-1]):
        for v2 in values[idx1+1:]:

            num = len(set(v1).intersection(set(v2)))
            if Debug:
                print("v1=",v1)
                print("v2=", v2)
                print(num)
            if num >= 2:
                res += binomial(num, 2)
    return res


def preprocess(s):
    dots = defaultdict(list)
    for row in s:
        x_y = list(map(int, row.split()))
        dots[x_y[0]].append(x_y[1])
    return dots


if __name__ == "__main__":
    x = int(input())
    # ans = []
    for i in range(x):
        s = int(input())
        l = []
        for j in range(s):
            l.append(input())
        dots = preprocess(l)
        print(solve(dots))
        # ans.append(solve(dots))
    # for i in ans:
    #     print(i)
