T = int(input())
for _ in range(T):
    s = str(input())
    sum_ = 0
    cnt = 0
    for si in s: 
        if si=='O':
            cnt +=1
            sum_ +=cnt
        else:
            cnt = 0
    print(sum_)
        
    
    