#틀림
import math
F,S,G,U,D = map(int, input().split())

x = 0
y = 0

if U==0:
    y = (S-G)/D
    int_y = int(y)

    if y==int_y and 0 < D*int_y <= F:
      print(int_y)
    else:
      print("use the stairs")
elif D==0:
  x = (G-S)/U
  int_x = int(x)

  if x==int_x and 0 < U*int_x <= F:
      print(int_x)
  else:
      print("use the stairs")
else:
  x=(G-S) / U
  x = math.ceil(x)
  while True:
    y = (S + (U*x) - G)/D
    int_y = int(y)

    if y == int_y and 0 < U*x <= F and 0 < D*int_y <= F:
      print(x+int_y)
      break
    elif x >= 1000000 or y >= 1000000:
      print("use the stairs")
      break
    else:
      x = x+1





