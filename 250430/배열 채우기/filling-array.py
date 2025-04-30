arr=list(map(int,input().split()))
ans=[]
while arr:
    if arr[-1]==0:
        ans=[]
        arr.pop()
    else:
        ans.append(arr.pop())
    # x=arr.pop()
    # if x==0:
    #     ans=[]
    # else:
    #     ans.append(x)
    

print(*ans)