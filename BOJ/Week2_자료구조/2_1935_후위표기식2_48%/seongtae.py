import sys

N = int(sys.stdin.readline())

formula = sys.stdin.readline().strip()

operands = {}
for i in range(N):
    operands[chr(ord('A') + i)] = int(sys.stdin.readline())

stack = []
for char in formula:
    if char in operands:
        stack.append(operands[char])
        continue

    a, b = stack.pop(), stack.pop()
    
    if char == '+':
        stack.append(a + b)
    elif char == '-':
        stack.append(b - a)
    elif char == '*':
        stack.append(a * b)
    elif char == '/':
        stack.append(b / a)

print(f'{stack[0]:.2f}')