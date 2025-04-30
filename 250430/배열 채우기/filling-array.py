arr=list(map(int,input().split()))
ans=[]
while arr:
    # if arr[-1]==0:
    #     ans=[]
    # else:
    #     ans.append(arr.pop())
    x=arr.pop()
    if x==0:
        ans=[]
    else:
        ans.append(x)
    

print(*ans)


# arr=[]
# for _ in range(10):
#     x=int(input())
#     if x==0:
#         break
#     arr.append(elem)
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i],end=" ")