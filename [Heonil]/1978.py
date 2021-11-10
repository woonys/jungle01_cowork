def check(n : int):
    if n==1 or n==0:
        return False
    elif n==2:
        return True
    
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    
    return True
    

if __name__ == "__main__":
    N= int(input())
    li = list(map(int, input().split()))
    cnt = 0
    for i in li:
        if(check(i)):
            cnt+=1
    
    print(cnt)
    
