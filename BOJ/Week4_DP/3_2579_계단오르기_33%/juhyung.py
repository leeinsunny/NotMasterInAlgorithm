n = int(input())
stair = [0]*(n+1) #계단 라스트
dp = [0]*(n+1) #해당 계단만큼 점수의 최댓값

for i in range(1,n+1):
  stair[i] = int(input())


for i in range(1,n+1):
  if i == 1:
    dp[i] = stair[i]
  elif i == 2:
    dp[i] = stair[i]+stair[i-1]
  elif i == 3:
    dp[i] = max(stair[i]+stair[i-1] , stair[i]+stair[i-2])
  else:
    dp[i] = max(dp[i-3]+stair[i]+stair[i-1] , dp[i-2]+stair[i])

print(dp[n])