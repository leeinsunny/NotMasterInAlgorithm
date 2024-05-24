
#word, name = input().split()
word = input()
name = input()


i = 0
sum = 0  

while i <= len(word) - len(name):
  if word[i:i+len(name)] == name:
    sum += 1
    i += len(name)
  else:
    i += 1


print(sum)
    




