import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀 최대 깊이 조절 #PyPy로는 안됨

n = int(input())

# # Dictionary 사용해서 root를 key , left/right 자식들을 value로 할당
tree = {}
for i in range(n):
    root, left, right = map(str, input().split())  # 루트, 왼쪽자식, 오른쪽 자식
    tree[root] = left, right  # {'A': ('B', 'C')}

def preorder(root):  # 전위순회
    if root != ".":  # 루트 노드가 .이 아니면 (자식이 있다면)
        print(root, end="") #root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right

def inorder(root):  # 중위순회
    if root != ".":  # 루트 노드가 .이 아니면 (자식이 있다면)
        inorder(tree[root][0])  # left
        print(root, end="") #root
        inorder(tree[root][1])  # right

def postorder(root):  # 전위순회
    if root != ".":  # 루트 노드가 .이 아니면 (자식이 있다면)
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end="") #root

#루트노드 'A'
preorder('A')
print()
inorder('A')
print()
postorder('A')