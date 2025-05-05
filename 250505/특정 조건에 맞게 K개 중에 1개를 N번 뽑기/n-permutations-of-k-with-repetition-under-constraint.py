K, N = map(int, input().split())

# Please write your code here.
answer=[]
def choose(curr_num):
    if curr_num==N+1:
        print(*answer)
        return
    for i in range(1,K+1):
        if curr_num>=3 and answer[-1]==answer[-2]==i:
            continue
        answer.append(i)
        choose(curr_num+1)
        answer.pop()
choose(1)