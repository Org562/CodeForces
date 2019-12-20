def solve():
    n  =int(input())
    nums = list(map(int, input().split(' ')))
    sum = []
    for i in range(len(nums)):
        if nums[i]==2:
            nums[i]=-1
    tem = 0
    pos = {}
    pos[0] = -1
    for i in range(len(nums)):
        tem += nums[i]
        sum.append(tem)
        if i<n:
            pos[tem] = i
    ans = 2*n
    for i in range(n-1,len(nums)):
        if sum[i]-sum[-1] in pos:
            ans = min(ans, i-pos[sum[i]-sum[-1]])
    print(ans)
 
 
 
 
N = int(input())
for _ in range(N):
    solve()
