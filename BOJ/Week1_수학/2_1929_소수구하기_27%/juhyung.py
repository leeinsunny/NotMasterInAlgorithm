inputs = input().split()

M = int(inputs[0])

N = int(inputs[1])


for a in range(M,N+1):
  is_prime = True
  for i in range(2,a):
    if a % i == 0:
      is_prime = False
  if is_prime:
    print(a)
