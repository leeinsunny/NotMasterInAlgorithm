
class Member:
  def __init__(self,age,name):
    self.age = age
    self.name = name

members = []

n = int(input())
for i in range(0,n):
  input_str = input()
  age, name = input_str.split()
  age = int(age)

  member = Member(age,name)
  members.append(member)

# 정렬하기 
# list.sort() : list 객체 자체를 정렬해주는 함수 /  key: sort함수에서 key 매개변수를 사용하여 어떤 속성을 기준으로 정렬할지를 지정할 수 있다
# lamda x : x.age - x는 list의 객체 하나(참조값)
members.sort(key=lambda x: x.age)

# 정렬된 회원 정보를 출력합니다.
for member in members:
    print(member.age , " " , member.name)
