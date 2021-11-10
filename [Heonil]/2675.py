T = int(input())

for _ in range(T):
    n, s = input().split()
    ans = ""
    for s_i in s:
        for _ in range(int(n)):
            ans +=s_i
    
    print(ans)