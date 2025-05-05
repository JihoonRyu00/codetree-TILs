n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
r=r-1
c=c-1
range_=grid[r][c]-1
up_r=max(r-range_,0)
down_r=min(n-1,r+range_)
right_c=min(n-1,c+range_)
left_c=max(c-range_,0)


for col in range(left_c,c):
    if r>0:
        for row in range(r,0,-1):
            grid[row][col]=grid[row-1][col]
    grid[0][col]=0


for row in range(down_r,-1,-1):
    new_r=up_r-(down_r-row+1)
    if new_r>=0:
        grid[row][c]=grid[new_r][c]
    else:
        grid[row][c]=0


if c<n-1:
    for col in range(c+1,right_c+1):
        if r>0:
            for row in range(r,0,-1):
                grid[row][col]=grid[row-1][col]
    grid[0][col]=0

for i in range(n):
    print(*grid[i])