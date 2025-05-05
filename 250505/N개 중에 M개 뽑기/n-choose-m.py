N, M = map(int, input().split())

# Please write your code here.
answer=[]
def choose(curr_num,maxn,r):
    if curr_num==M+1:
        print(*answer)
        return
    for i in range(maxn+1,N+1-r+1):
        answer.append(i)
        choose(curr_num+1,i,r-1)
        answer.pop()
choose(1,0,M)
