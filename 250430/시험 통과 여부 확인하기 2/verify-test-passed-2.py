n=int(input())
students=[list(map(int,input().split())) for _ in range(n)]
ans=0
for student in students:
    if sum(student)/4>=60:
        print('pass')
        ans+=1
    else:
        print('fail')
print(ans)