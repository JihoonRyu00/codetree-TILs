n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
con=u+d
k=t%(2*n)
for i in range(n):
    print(con[i-k],end=" ")
print("")
for i in range(n,2*n,1):
    print(con[i-k],end=" ")