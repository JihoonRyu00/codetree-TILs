n = int(input())

# Please write your code here.
visited=[False for _ in range(n+1)]
ans=[]
def choose(curr_num,v):
    if curr_num==n+1:
        print(*ans)
        return
    for i in range(1,n+1):
        if not v[i]:
            ans.append(i)
            v[i]=True
            choose(curr_num+1,v)
            v[i]=False
            ans.pop()
choose(1,visited)