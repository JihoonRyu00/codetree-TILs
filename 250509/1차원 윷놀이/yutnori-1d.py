n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
ans=0
m=m-1
found=False
nums.sort()
visited=[False]*n

def func(r):
    global ans, k, found
    if r==0:
        ans+=1
        k-=1
        found=True
        return
    for i in range(n-1,-1,-1):
        if not visited[i] and nums[i]<=r:
            visited[i]=True
            func(r-nums[i])
            if found==True:
                return
            visited[i]=False

while(k>0):
    found=False
    total=0
    for i in range(n):
        if not visited[i]:
            total+=nums[i]
    if total<m:
        break
    elif total==m:
        ans+=1
        break
    elif total>m:
        func(m)
    if not found:
        m+=1

print(ans)