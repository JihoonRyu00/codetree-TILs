K, N = map(int, input().split())

# Please write your code here.
answer=[]

def choose(curr_num):
    if curr_num==N+1:
        print(*answer)
        return
    for i in range(K):
        answer.append(i+1)
        choose(curr_num+1)
        answer.pop()

choose(1)