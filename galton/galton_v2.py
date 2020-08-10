Debug = False
from math import gcd

def pascal(n):
    r1, r2 = [1], [1, 1]
    degree = 1
    res = []
    while degree <= n:
        res.append(r1)
        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
        degree += 1
    return res

def solve(ll):
    # ll - list of lists
    # l -list
    res = 0
    h = 2 ** (len(ll) - 1)
    num_path = h
    pasc = pascal(len(ll))
    for l, pasc_i in zip(ll, pasc):
        res += sum([x*y*h for x,y in zip(pasc_i, l)])
        if Debug:
            print(pasc_i)
            print()
            print(f"iter:",res)
        h = h // 2

    if Debug:
        print("res:", res)
        print("num_path", num_path)
    d = gcd(res, num_path)
    return f"{res // d} {num_path // d}"


if __name__ == "__main__":
    for i in  range(int(input())):
        h = int(input())
        l = []
        for j in range(h):
            l.append(list(map(int, input().split())))
        print(solve(l))