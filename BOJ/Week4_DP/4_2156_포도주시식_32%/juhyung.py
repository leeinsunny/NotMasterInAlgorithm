n = int(input())

wine = [0]*(n+1) # 와인잔 개수
dp = [0]*(n+1) # 각 와인잔까지 최대로 마실 수 있는 양

for i in range(1,n+1):
  wine[i] = int(input())

for i in range(1,n+1):
  if i == 1:
    dp[i] = wine[i]
  elif i == 2:
    dp[i] = wine[i] + wine[i-1]
  elif i == 3:
    dp[i] = max(wine[i]+wine[i-1], wine[i]+wine[i-2], wine[i-1]+wine[i-2])
  elif i == 4:
    dp[i] = max(wine[i]+wine[i-2]+wine[i-3], wine[i]+wine[i-1]+wine[i-3])
  else: 
    dp[i] = max(dp[i-3]+wine[i]+wine[i-1], dp[i-2]+wine[i], dp[i-4]+wine[i-1]+wine[i-2])

print(dp[n])