dirs = input()

# Please write your code here.
dx=[0,1,0,-1]
dy=[1,0,-1,0]

cur_dir=0
o=[0,0]

for dir in dirs:
    if dir == "F":
        o=[o[0]+dx[cur_dir],o[1]+dy[cur_dir]]
    elif dir == "L":
        cur_dir=(cur_dir+3)%4
    elif dir == "R":
        cur_dir=(cur_dir+1)%4

print(o[0],o[1])