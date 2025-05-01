n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# con=u+d
# k=t%(2*n)
# for i in range(n):
#     print(con[i-k],end=" ")
# print("")
# for i in range(n,2*n,1):
#     print(con[i-k],end=" ")

for _ in range(t):
    uu=u[-1]
    dd=d[-1]
    for i in range(-1,-n,-1):
        u[i]=u[i-1]
        d[i]=d[i-1]
    u[0]=dd
    d[0]=uu

print(*u)
print(*d)