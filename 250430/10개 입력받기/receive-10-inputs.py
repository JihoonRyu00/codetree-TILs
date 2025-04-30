arr=list(map(int,input().split()))
sum=0
cnt=0
for elem in arr:
    if elem==0:
        break
    sum+=elem
    cnt+=1
print(sum,f"{sum/cnt:.1f}")