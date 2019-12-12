N = int(input())
for _ in range(N):
    nums = list(input())
    l=0;r=0;u=0;d=0
    ln = len(nums)
    for i in range(ln):
        if nums[i]=='L':l += 1
        if nums[i]=='R':r += 1
        if nums[i]=='U':u += 1
        if nums[i]=='D':d += 1
    l = min(l,r);u = min(u,d)
    if l>0 and u>0:
        a = ['D']*u;b = ['U']*u
        c = ['L']*l;d = ['R']*l
        ans = b+c+a+d
        ans = ''.join(ans)
        print(len(ans))
        print(ans)
    elif l>0:
        print(2)
        print('LR')
    elif u>0:
        print(2)
        print('UD')
    else:
        print(0)
        print()
 
