T = int(input())
sum = [0]*T

for i in range(T):
  N = int(input())
  price = list(map(int,input().split()))
  

  max = 0
  #sum = 0
  for j in range(N-1,-1,-1):
    if price[j] > max:
      max = price[j]
    elif price[j] < max:
      sum[i] = sum[i] + max - price[j]
  
  print(sum[i])


