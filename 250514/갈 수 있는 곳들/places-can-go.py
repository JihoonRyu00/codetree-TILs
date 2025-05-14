n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
drs=[1,0,-1,0]
dcs=[0,1,0,-1]
ans=0
def dfs(curr_pos):
    count=1
    for dr,dc in zip(drs,dcs):
        next_r=curr_pos[0]+dr
        next_c=curr_pos[1]+dc
        if 0<=next_r<n and 0<=next_c<n and grid[next_r][next_c]==0:
            grid[next_r][next_c]=1
            count+=dfs([next_r,next_c])
    return count


for r,c in points:
    if grid[r-1][c-1]==0:
        grid[r-1][c-1]=1
        ans+=dfs([r-1,c-1])

print(ans)