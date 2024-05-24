class Node:
  def __init__(self,data,left_node,right_node):
    self.data = data
    self.left_node = left_node
    self.right_node = right_node


#전위 순회
def pre_order(node):
  print(node.data, end='')
  if node.left_node != None:
    pre_order(tree[node.left_node])
  if node.right_node != None:
    pre_order(tree[node.right_node])

#중위 순회
def in_order(node):
  if node.left_node != None:
    in_order(tree[node.left_node])
  print(node.data, end='')
  if node.right_node != None:
    in_order(tree[node.right_node])

#후위 순회
def post_order(node):
  if node.left_node != None:
    post_order(tree[node.left_node])
  if node.right_node != None:
    post_order(tree[node.right_node])
  print(node.data, end='')



n = int(input())
tree={}
# 1. dictionary(사전) 사용
# 2. Node 객체를 하나씩 설정해서 right,left를 각각 지정해준다 (번거로움)

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node ==".":
      left_node = None
    if right_node ==".":
      right_node = None
    tree[data] = Node(data,left_node,right_node) 
    #data는 key로 Node 객체는 value로

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

