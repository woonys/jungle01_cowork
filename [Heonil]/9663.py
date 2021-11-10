N = 0 
cnt = 0

board = [0]*16

same_column = set()
same_diagonal1 =set()
same_diagonal2 = set()

def check(level):
    # 여기서 O(1)로 만든다면? 
    if board[level] in same_column or level + board[level] in same_diagonal1 or level - board[level] in same_diagonal2:
        return False
    else:
        same_column.add(board[level])
        same_diagonal1.add(level + board[level])
        same_diagonal2.add(level - board[level])
    return True




def nqueen(depth):
    global cnt # 지역 범위에서 전역 변수를 사용하기 위해서는 이렇게 사용을 해줘야 한다.
    if depth==N:
        cnt = cnt +1
        return
    
    for i in range(N):
        board[depth] = i
        if check(depth):
            nqueen(depth+1)
            # 넣어 줬던거 제거
            same_column.remove(board[depth])
            same_diagonal1.remove(depth + board[depth])
            same_diagonal2.remove(depth - board[depth])
            
            
            
        
        
if __name__=='__main__':
    N = int(input())
    nqueen(0)
    print(cnt)