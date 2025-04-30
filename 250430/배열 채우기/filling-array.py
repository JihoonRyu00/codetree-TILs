arr=list(map(int,input().split()))
if arr[-1]==0:
    arr.pop()
while arr:
    print(arr.pop(),end=" ")