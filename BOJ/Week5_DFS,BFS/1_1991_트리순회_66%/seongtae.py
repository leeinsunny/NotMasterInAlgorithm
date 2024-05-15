#1991 트리 순회
import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    name, left, right = input().strip().split()
    tree[name] = (left, right)

def dfs_preorder(name):
    if name == '.':
        return
    
    left, right = tree[name]
    
    print(name, end="")
    dfs_preorder(left)
    dfs_preorder(right)

def dfs_inorder(name):
    if name == '.':
        return
    
    (left, right) = tree[name]
    
    dfs_inorder(left)
    print(name, end="")
    dfs_inorder(right)

def dfs_postorder(name):
    if name == '.':
        return
    
    (left, right) = tree[name]
    
    dfs_postorder(left)
    dfs_postorder(right)
    print(name, end="")


dfs_preorder('A')
print()

dfs_inorder('A')
print()

dfs_postorder('A')
print()
