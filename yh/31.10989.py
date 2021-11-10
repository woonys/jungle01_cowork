from sys import stdin
rpt = int(stdin.readline())
li = [0] * 10001

for _ in range(rpt) :
     li[int(stdin.readline())] += 1
     print(li[int(stdin.readline())])

for i in range(10001):
     for j in li :
          while j > 0 :
               print(i)
               j -= 1
          else:
               break