T = int(input())

for i in range(T):
  N = int(input())
  num_list = [0]*(N+1)

  for i in range(1,N+1):

    if i == 1 or i == 2 or i ==3:
      num_list[i] = 1
    elif i == 4 or i == 5:
      num_list[i] = 2
    elif i in [6,7,8]:
      num_list[i] = num_list[i-1] + 1
    elif i in [9,10]:
      num_list[i] = num_list[i-1] + 2
    else:
      num_list[i] = num_list[i-1] + num_list[i-5]

  print(num_list[N])
    
