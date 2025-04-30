N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

dr=[-1,0,1,0]
dc=[0,1,0,-1]
d=0
r=c=int((N-1)/2)
cnt=board[r][c]


for s in str:
    if s=='L':
        d=(d+3)%4
    elif s=='R':
        d=(d+1)%4
    else:
        rr=r+dr[d]
        cc=c+dc[d]
        if rr<0 or rr>=N or cc<0 or cc>=N:
            continue
        r=rr
        c=cc
        cnt+=board[r][c]

print(cnt)