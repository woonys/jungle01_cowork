W = []
N = int(input())
for _ in range(N):
    tmp = list(map(int, input().split()))
    W.append(tmp)
    
result = 987654321

visit = [False] * 11
arr = [0] * 11


def check(i,j)-> bool:
    if W[i][j] == 0:
        return False
    else:
        return True

def dfs(m):
    global N, result
    if m==N:
        arr[N] = arr[0]
        for i in range(N):
            if check(arr[i], arr[i+1]) == False:
                return
        
        sum_ = 0
        for i in range(N):
            sum_ += W[arr[i]][arr[i+1]]
        
        result = min(result, sum_)
        return
    
    for i in range(N):
        if visit[i] ==False:
            visit[i] = True
            arr[m] = i
            dfs(m+1)
            visit[i] = False

    
        
dfs(0)
print(result)
