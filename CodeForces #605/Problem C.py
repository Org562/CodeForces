N = list(map(int,input().split(' ')))
s = list(input())
Q = input().split(' ')
dic = {}
for i in range(N[1]):
    if Q[i] not in dic:
        dic[Q[i]] = True
ans = 0
tem = 0
for i in range(N[0]):
    if s[i] not in dic:
        ans += int((tem*(tem+1))/2)
        tem = 0
    else:
        tem += 1
if tem!=0:
    ans += int((tem*(tem+1))/2)
print(ans)
