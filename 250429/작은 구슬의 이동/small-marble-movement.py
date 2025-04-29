n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dirnum={"U":0,"R":1,"D":2,"L":3}
numdir=["U","R","D","L"]
dr=[-1,0,1,0]
dc=[0,1,0,-1]

for i in range(t):
    rr=r+dr[dirnum[d]]
    cc=c+dc[dirnum[d]]
    if rr>=1 and rr<n+1 and cc>=1 and cc<n+1:
        r=rr
        c=cc
    else:
        d=numdir[(dirnum[d]+2)%4]

print(r,c)