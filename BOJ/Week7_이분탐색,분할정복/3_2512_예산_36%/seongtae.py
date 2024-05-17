import sys

input = sys.stdin.readline

N = int(input())
budget_requests = list(map(int, input().split()))
total_budget = int(input())

def limited_sum(limit):
    total = 0
    for budget_request in budget_requests:
        total += min(budget_request, limit)
    return total

left, right = 1, max(budget_requests)
while left < right:
    quotient, remainder = divmod(right - left, 2)
    mid = left + quotient
    if remainder:
        mid += 1

    total = limited_sum(mid)

    if total_budget >= limited_sum(mid):
        left = mid
    else:
        right = mid - 1

print(left)