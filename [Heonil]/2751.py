from sys import stdin
N= int(stdin.readline())
li = []
for _ in range(N):
    li.append(int(stdin.readline()))

li.sort()

for a in li:
    print(a)