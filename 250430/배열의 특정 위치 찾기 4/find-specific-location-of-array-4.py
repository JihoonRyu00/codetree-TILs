arr=list(map(int,input().split()))
sum=0
cnt=0
for elem in arr:
    if elem==0:
        break
    if elem%2==0:
        sum+=elem
        cnt+=1
print(cnt,sum)