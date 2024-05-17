# 1991 트리순회

import sys

input = sys.stdin.readline

N = int(input())


class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


# 전위 순회
def pre_order(node):
    print(node.item, end="")
    if node.left is not None:
        pre_order(tree[node.left])
    if node.right is not None:
        pre_order(tree[node.right])


# 중위 순회
def in_order(node):
    if node.left is not None:
        in_order(tree[node.left])
    print(node.item, end="")
    if node.right is not None:
        in_order(tree[node.right])


# 후위 순회
def post_order(node):
    if node.left is not None:
        post_order(tree[node.left])
    if node.right is not None:
        post_order(tree[node.right])
    print(node.item, end="")


tree = {}

for _ in range(N):
    item, left, right = input().rstrip().split()
    if left == ".":
        left = None
    if right == ".":
        right = None
    tree[item] = Node(item, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
