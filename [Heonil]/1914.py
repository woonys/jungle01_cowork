def Hanoi_count(n):
    if n==1:
        return 1
    
    return 1+ 2* Hanoi_count(n-1)



def Hanoi(f, t, through, n):
    if n==1:
        print(f,t)
        return
    
    Hanoi(f, through, t, n-1)
    Hanoi(f, t, through, 1)
    Hanoi(through, t, f, n-1)
    
    
    
inp = int(input())

print(Hanoi_count(inp))
if inp<=20:
    Hanoi(1,3,2,inp)