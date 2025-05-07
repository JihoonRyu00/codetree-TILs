from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr=[-1,0,1,0]
dc=[0,1,0,-1]
ans=0
def bfs(r,c):
    global ans
    q=deque()
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<n and 0<=cc<m and a[rr][cc]==1:
            if rr==n-1 and cc==m-1:
                ans=1
                return
            a[rr][cc]=0
            q.append([rr,cc])
    while q:
        r,c=q.popleft()
        for i in range(4):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<n and 0<=cc<m and a[rr][cc]==1:
                    if rr==n-1 and cc==m-1:
                        ans=1
                        return
                    a[rr][cc]=0
                    q.append([rr,cc])

bfs(0,0)
print(ans)