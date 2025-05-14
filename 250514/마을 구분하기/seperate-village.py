from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
drs=[1,0,-1,0]
dcs=[0,1,0,-1]
villages=[]
def dfs(curr_pos):
    count=1
    for dr,dc in zip(drs,dcs):
        next_r=curr_pos[0]+dr
        next_c=curr_pos[1]+dc
        if 0<=next_r<n and 0<=next_c<n and grid[next_r][next_c]==1:
            # print("  ",next_r,next_c)
            grid[next_r][next_c]=0
            count+=dfs([next_r,next_c])
    return count


for r in range(n):
    for c in range(n):
        if grid[r][c]==1:
            grid[r][c]=0
            villages.append(dfs([r,c]))

villages.sort()
print(len(villages))
for village in villages:
    print(village)