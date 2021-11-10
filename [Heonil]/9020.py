isPrime = [True]*10001
primeList = []

def go(n):
    return
    
# isPrime - init
isPrime[0] = False
isPrime[1] = False
for i in range(2, 10001):
    if isPrime[i]:
        for j in range(i+i, 10001, i):
            isPrime[j] = False

# primeList - init
for i in range(len(isPrime)):
    if isPrime[i]:
        primeList.append(i)
    
    
T = int(input())
for _ in range(T):
    num = int(input())
    answer =[]
    diff = 987654321
    index = 0
    for primeNum in primeList:
        if primeNum > num:
            break;
        if isPrime[primeNum] and isPrime[num-primeNum]:
            answer.append([primeNum, num-primeNum])
        
    for i in range(len(answer)):
        if diff > abs(answer[i][0] - answer[i][1]):
            index = i
            diff = abs(answer[i][0] - answer[i][1])
            
    
    print(answer[index][0], answer[index][1])
    
    