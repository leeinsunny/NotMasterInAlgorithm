n=int(input())

for i in range(n):
  N = int(input())
  dp = [0] * (N+1) # N+1 크기의 배열
  
  for i in range(1,N+1):
    if i == 1:
      dp[i] = 1
    elif i == 2:
      dp[i] = 2
    elif i == 3:
      dp[i] = 4
    else:
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  
  print(dp[N])


# dp[N] 구하는 방법
# (N-1) + 1 : dp[N-1]
# (N-2) + 2 : dp[N-2]
# (N-3) + 3 : dp[N-3]
