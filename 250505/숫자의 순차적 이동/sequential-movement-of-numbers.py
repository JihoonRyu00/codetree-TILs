n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]

def get_pos(x):
    for r in range(n):
        for c in range(n):
            if grid[r][c]==x:
                return r,c

def tick(x):
    maxx=0
    r,c=get_pos(x)
    new_r=0
    new_c=0
    for i in range(8):
        rr=r+dr[i]
        cc=c+dc[i]
        if rr<0 or rr>=n or cc<0 or cc>=n:
            continue
        if grid[rr][cc]>maxx:
            maxx=grid[rr][cc]
            new_r=rr
            new_c=cc
    grid[r][c]=grid[new_r][new_c]
    grid[new_r][new_c]=x

def turn():
    for i in range(1,n**2+1):
        tick(i)

for i in range(m):
    turn()

for r in range(n):
    print(*grid[r])