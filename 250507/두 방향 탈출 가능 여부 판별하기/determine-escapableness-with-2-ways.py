n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr=[0,1]
dc=[1,0]
grid[0][0]=0
not_visit=grid
ans=0
def dfs(r,c):
    global ans
    for i in range(2):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<n and 0<=cc<m and not_visit[rr][cc]==1:
            if rr==n-1 and cc==m-1:
                ans=1
                return
            not_visit[rr][cc]=0
            dfs(rr,cc)
dfs(0,0)
print(ans)