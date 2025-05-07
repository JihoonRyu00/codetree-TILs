from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
drs=[1,0,-1,0]
dcs=[0,1,0,-1]
q=deque()
possible=False
dis=0
def bfs():
    global dis
    global possible
    while q:
        r,c,d=q.popleft()
        for dr, dc in zip(drs, dcs):
            rr=r+dr
            cc=c+dc
            if 0<=rr<n and 0<=cc<m and a[rr][cc]==1:
                if rr==n-1 and cc==m-1:
                    possible=True
                    dis=d+1
                    return
                q.append([rr,cc,d+1])
                a[rr][cc]=0

q.append([0,0,0])
bfs()

if possible:
    print(dis)
else:
    print(-1)