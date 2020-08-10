Debug = False
def solve(x):
    c = 1
    cat = 1
    c_ = 1
    while c < x:
        c_ = c
        c += cat + 1
        cat += 1
        if Debug:
            print("c =",c)
            print("cat=", cat)
    ans = (1 << cat)
    dop_ans = 1
    if Debug:
        print("after while c=", c_)
        print("current ans=", ans)
    for i in range(x - c_ - 1):
        dop_ans = dop_ans << 1
    ans += dop_ans
    return ans % 35184372089371

if __name__ == "__main__":
    x = int(input())
    ans = []
    for i in range(x):
        _ans = solve(int(input()))
        ans.append(_ans)
    for i in ans:
        print(i)
