w,h = input().split()
w_list = [0, int(w)]
h_list= [0, int(h)]

T =int(input())

for _ in range(T):
    direction, num = map(int, input().split())
    if direction == 0:
        h_list.append(num)
    else : 
        w_list.append(num)
        
        
h_list.sort()
w_list.sort()
answer = 0
for i in range(1, len(w_list)):
    for j in range(1, len(h_list)):
        answer = max(answer, (w_list[i]-w_list[i-1]) * (h_list[j]-h_list[j-1])  )
        
print(answer)