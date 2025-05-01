n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
happy=0

def is_rhappy(r):
    stack=[]
    stack.append(grid[r][0])
    for i in range(1,n):
        cur=grid[r][i]
        if stack and stack[-1]!=cur:
                stack=[]
        stack.append(cur)
        if len(stack)==m:
            return True
    return False

def is_chappy(c):
    stack=[]
    stack.append(grid[0][c])
    for i in range(1,n):
        cur=grid[i][c]
        if stack and stack[-1]!=cur:
                stack=[]
        stack.append(cur)
        if len(stack)==m:
            return True
    return False


if m==1:
    print(2*n)
else:
    for i in range(n):
        if is_chappy(i):
            happy+=1
        if is_rhappy(i):
            happy+=1
        
    print(happy)