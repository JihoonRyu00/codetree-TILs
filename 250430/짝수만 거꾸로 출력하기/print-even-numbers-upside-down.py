N=int(input())
arr=list(map(int,input().split()))
for i in range(N-1,-1,-1):
    if arr[i]%2==0:
        print(arr[i],end=" ")