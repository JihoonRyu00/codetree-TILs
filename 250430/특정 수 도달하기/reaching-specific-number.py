arr=list(map(int,input().split()))
sum=0
ans=0
cnt=0
for elem in arr:
    if elem>=250:
        break
    sum+=elem
    cnt+=1
ans=sum/cnt

print(sum,f"{ans:.1f}")