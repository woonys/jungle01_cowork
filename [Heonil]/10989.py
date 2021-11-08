from sys import stdin

arr = [0]*10001
n = int(stdin.readline())
for _ in range(n):
    tmp = int(stdin.readline())
    arr[tmp] += 1
    
for i in range(len(arr)):
    if arr[i]>0:
        for j in range(arr[i]):
            print(i)
    