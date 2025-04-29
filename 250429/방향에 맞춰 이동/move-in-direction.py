n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dirtonum={"W":0,"S":1,"N":2,"E":3}
dx=[-1,0,0,1]
dy=[0,-1,1,0]
o=[0,0]
for i in range(n):
    o=[o[0]+dx[dirtonum[dir[i]]]*dist[i],o[1]+dy[dirtonum[dir[i]]]*dist[i]]
print(o[0],o[1])