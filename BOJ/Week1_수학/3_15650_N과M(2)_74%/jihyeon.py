N,M=map(int, input().split())
answer=[]

def dfs(n,s,seq):
    if n==M:
        answer.append(seq)
        return

    for j in range(s, N+1):
        dfs(n+1, j+1, seq+[j])

dfs(0,1,[])
for seq in answer:
    print(*seq)