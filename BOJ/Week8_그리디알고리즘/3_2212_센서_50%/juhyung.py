N = int(input())
K = int(input())

location = list(map(int,input().split()))
distance = [0]*(len(location) - 1)

location.sort()

for i in range (0,len(location)-1):
  distance[i] = location[i+1] - location[i]

distance.sort()
num = len(distance) - (K-1)
sum = 0


for i in range(0,num):
  sum = sum + distance[i]

print(sum)

