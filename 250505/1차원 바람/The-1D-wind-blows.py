n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def shift(r,d):
    orig_row=a[r]
    new_row=[]
    pivot=0
    if d=="L":
        pivot=m-1
    elif d=="R":
        pivot=1
    new_row=orig_row[pivot:m]+orig_row[0:pivot]
    a[r]=new_row

def is_matched(r1,r2):
    for i in range(m):
        if a[r1][i]==a[r2][i]:
            return True
    return False


for r,d in winds:
    r=r-1
    shift(r,d)

    orig_r=r
    next_r=orig_r-1
    next_d="L" if d=="R" else "R"

    while(next_r>=0):
        if is_matched(next_r,next_r+1):
            shift(next_r,next_d)
            next_r-=1
            next_d="L" if next_d=="R" else "R"
        else:
            break
    
    next_r=orig_r+1
    next_d="L" if d=="R" else "R"

    while(next_r<n):
        if is_matched(next_r,next_r-1):
            shift(next_r,next_d)
            next_r+=1
            next_d="L" if next_d=="R" else "R"
        else:
            break

for i in range(n):
    print(*a[i])