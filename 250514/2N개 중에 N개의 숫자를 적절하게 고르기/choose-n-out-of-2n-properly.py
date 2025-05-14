n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
min_diff=1000
curr_diff=0
def choose_n(curr_i,r):
    global curr_diff, min_diff
    if curr_i==2*n:
        min_diff=min(min_diff,abs(curr_diff))
        return
    if r>0:
        curr_diff-=num[curr_i]
        choose_n(curr_i+1,r-1)
        curr_diff+=num[curr_i]
    if r<=2*n-curr_i-1:
        curr_diff+=num[curr_i]
        choose_n(curr_i+1,r)
        curr_diff-=num[curr_i]
choose_n(0,n)
print(min_diff)
    