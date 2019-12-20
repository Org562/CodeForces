def solve():
    s = input()
    s = sorted(s)
    t = input()
    for i in range(len(t)-len(s)+1):
        S = []
        for j in range(i, i + len(s)):
            S.append(t[j])
        if sorted(S) == s:
            print('YES');return
    print('NO');return


N = int(input())
for _ in range(N):
    solve()

