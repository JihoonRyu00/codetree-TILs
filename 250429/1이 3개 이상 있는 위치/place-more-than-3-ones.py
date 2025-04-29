n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans=0
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return r>=0 and r<n and c>=0 and c<n

def check(r,c):
    cnt=0
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if in_range(rr,cc) and grid[rr][cc]==1:
            cnt+=1
    return cnt>=3

for row in range(n):
    for col in range(n):
        if check(row,col):
            ans+=1

print(ans)
