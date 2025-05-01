n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# def is_in_grid(r,c):
#     return r>=0 and r<n and c>=0 and c<n

def get_adj(r,c):
    x=0
    for i in range(3):
        for j in range(3):
            if grid[r+i-1][c+j-1]==1:
                x+=1
    return x

ans=0

for i in range(1,n-1):
    for j in range(1,n-1):
        ans=max(ans,get_adj(i,j))

print(ans)