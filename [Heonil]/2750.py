N = int(input())
li = []
for _ in range(N):
    tmp = int(input())
    li.append(tmp)

li.sort()

for a in li:
    print(a)