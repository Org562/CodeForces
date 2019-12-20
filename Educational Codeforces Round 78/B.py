t = int(input())
 
for _ in range(t):
    nums = input().split(' ')
    a = int(nums[0]); b = int(nums[1])
    d = abs(a-b)
    sum = 0
    i = 0
    while True:
        sum += i
        if sum>=d and sum%2 == d%2:
            print(i);break
        i += 1
