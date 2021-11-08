from sys import stdin
import sys
sys.setrecursionlimit(10**8)

N = int(stdin.readline())
moveDir = [[0 , 1], [0,-1], [1,0],[-1,0]]
Map_ = []
Tmp_list = []
s = set()

visit = []
for i in range(N):
    visit.append([False]*N)

for i in range(N):
    tmp = list(map(int, stdin.readline().split()))
    Map_.append(tmp)
    for t in tmp:
        s.add(t)
        
def dfs(y, x):
    visit[y][x] = True
    
    for i in range(4):
        nextY = y + moveDir[i][0]
        nextX = x + moveDir[i][1]
        
        if 0<= nextY and nextY<N and 0<=nextX and nextX<N:
            if visit[nextY][nextX] == False and Tmp_list[nextY][nextX] !=-1:
                dfs(nextY, nextX)
    
    
    

answer = 1
for num in s:
    # 여기서 시작을 해야겠네
    Tmp_list = Map_
    
    # 물에 잠구기
    for i in range(N):
        for j in range(N):
            if Tmp_list[i][j] <= num:
                Tmp_list[i][j] = -1
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False and Tmp_list[i][j] !=-1:
                dfs(i,j)
                cnt +=1
            
            
    answer = max(answer, cnt)
    # visit 초기화
    for i in range(N):
        for j in range(N):
            visit[i][j] = False


print(answer)