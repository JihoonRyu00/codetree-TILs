n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visit=[False]*n
max_sum=0

def bt(curr_row, curr_sum):
    global max_sum
    if curr_row==n:
        max_sum=max(max_sum,curr_sum)
        return
    for i in range(n):
        if not visit[i]:
            visit[i]=True
            curr_sum+=grid[curr_row][i]
            bt(curr_row+1,curr_sum)
            visit[i]=False
            curr_sum-=grid[curr_row][i]

bt(0,0)
print(max_sum)