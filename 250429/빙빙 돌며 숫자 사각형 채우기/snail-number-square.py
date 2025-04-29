n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dr=[-1,0,1,0]
dc=[0,1,0,-1]
d=1
r=0
c=0

def is_blocked(r,c):
    rr=r+dr[d]
    cc=c+dc[d]
    return rr<0 or rr>=n or cc<0 or cc>=m or arr[rr][cc]!=0

arr[0][0]=1
for i in range(2,n*m+1):
    if is_blocked(r,c):
        d=(d+1)%4
    r=r+dr[d]
    c=c+dc[d]
    arr[r][c]=i

for i in range(n):
    print(*arr[i])