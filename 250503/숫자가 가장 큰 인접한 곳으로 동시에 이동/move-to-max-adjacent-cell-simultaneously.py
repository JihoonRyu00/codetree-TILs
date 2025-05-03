n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.
dr=[0,0,1,-1]
dc=[1,-1,0,0]
# cur_pos=[[0]*n]*n
cur_pos=[[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    cur_pos[r[i]-1][c[i]-1]=1

for tt in range(t):
    next_pos=[[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if cur_pos[row][col]==1:
                maxnum=0
                maxd=0
                for dd in range(4):
                    rr=row+dr[dd]
                    cc=col+dc[dd]
                    if rr<0 or rr>=n or cc<0 or cc>=n:
                        continue
                    if a[rr][cc]>=maxnum:
                        maxnum=a[rr][cc]
                        maxd=dd
                rr=row+dr[maxd]
                cc=col+dc[maxd]
                next_pos[rr][cc]+=1
    cur_pos=next_pos

ans=0
for row in cur_pos:
        for col in row:
            if col==1:
                ans+=1

print(ans)