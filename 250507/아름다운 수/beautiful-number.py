n = int(input())

# Please write your code here.
def beut(r):
    count=0
    if r==0:
        return 1
    rr=min(r+1,5)
    for i in range(1,rr):
        count+=beut(r-i)
    return count
print(beut(n))
