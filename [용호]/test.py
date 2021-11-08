n = int(input()) # 테스트 개수 입력받기
results= [0]*n  # 결과 값을 저장할 0으로 이루어진 results 생성
for i in range(n):
  s=0 # 연속되는 점수를 저장할 S
  j=0 # 인덱스 값을 저장할 j
  ox_result = input() # 테스트 케이스를 입력받는다
  scores = [0]*len(ox_result) # 테스트 길이만큼 점수를 저장할 scores 생성
  for r in ox_result: # 문제의 답을 하나씩 가져온다
    if r == "O": # "O"라면
      s+=1 # 1을 더해준다
      scores[j] += s # 현재 점수를 배열에 저장한다
    elif r =="X":
      s=0 # 틀린 문제이기에 0점이다 
      scores[j]+=s # 그 값을 배열에 저장한다.
    j+=1 # 다음 문제의 답을 가져오기 위해 인덱스 값을 하나 더해준다
  results[i]+=sum(scores) # 스코어에 저장된 값을 저장해 results에 더해준다
    
for i in range(n): # for문으로 results 값을 출력
  print(results[i]) 