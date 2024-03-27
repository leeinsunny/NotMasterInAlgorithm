# N : 자연수 범위
# M : 수열의 길이

# 사용자가 입력한 값을 정수로 받아 넣기
N, M = map(int, input().split())

seq = [] #수열 초기화
start = 1 # 1부터 시작해서 작은 수 부터 수열에 넣기

def program(N, M, start, seq):
    
    #수열의 길이가 0이 되면 반복문 종료
    if M==0:
        print(" ".join(map(str, seq)))
        return
    
    #수열에 넣기 반복

    for i in range(start, N+1):
        seq.append(i)
        program(N,M-1, i+1, seq) # 재귀
        seq.pop() #직전에 추가한 수를 제거해서 다른 수를 선택할 수 있게 하기


program(N,M,start, seq)