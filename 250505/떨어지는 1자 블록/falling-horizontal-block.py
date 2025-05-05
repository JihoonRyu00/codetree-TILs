n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
k=k-1
maxh=n
for c in range(k,k+m):
    for r in range(n):
        if grid[r][c]==1:
            maxh=min(maxh,r)
            break
for c in range(k,k+m):
    grid[maxh-1][c]=1
for r in range(n):
    print(*grid[r])
