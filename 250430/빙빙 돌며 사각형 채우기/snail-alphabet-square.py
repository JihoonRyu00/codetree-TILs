n, m = map(int, input().split())
arr=[[0]*m for _ in range(n)]
# Please write your code here.

# A 65 Z 90
# ascii to char => chr()
# char to ascii => ord()
dr=[0,1,0,-1]
dc=[1,0,-1,0]

cur_dir=0
r=0
c=0
arr[0][0]='A'

for i in range(1,n*m):
    rr=r+dr[cur_dir]
    cc=c+dc[cur_dir]
    if rr<0 or rr>=n or cc<0 or cc>=m or arr[rr][cc]!=0:
        cur_dir=(cur_dir+1)%4
    r=r+dr[cur_dir]
    c=c+dc[cur_dir]
    arr[r][c]=chr(i%26+65)

for i in range(n):
    print(*arr[i])