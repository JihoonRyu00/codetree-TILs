n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dr=[-1,1,0,0]
dc=[0,0,-1,1]

visit=[a[r][c]]

while True:
    max_next=visit[-1]
    past_max=max_next
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if rr<1 or rr>n or cc<1 or cc>n:
            continue
        if a[rr][cc]>max_next:
            max_next=a[rr][cc]
            r=rr
            c=cc
            visit.append(a[r][c])
            break
    if max_next==past_max:
        break

print(*visit)      