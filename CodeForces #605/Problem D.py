N = int(input())
s = list(map(int,input().split(' ')))
dp = [[0]*2 for _ in range(N)]
ans = 1
dp[0][0] = 1;dp[0][1] = 1
dp[1][1] = 1;dp[1][0] = 1
if s[1]>s[0]:dp[1][0] = 2;ans = 2
 
for i in range(2,N):
    if s[i]>s[i-1] :
        dp[i][0] = dp[i-1][0]+1
        if s[i]>s[i-2]:
            dp[i][1] = max(dp[i-1][1], dp[i-2][0])+1
        else: dp[i][1] = dp[i-1][1]+1
    else:
        dp[i][0] = 1
        if s[i]>s[i-2]:
            dp[i][1] = dp[i-2][0]+1
        else:
            dp[i][1] = 1
    ans = max(ans,dp[i][0],dp[i][1])
 
print(ans)
