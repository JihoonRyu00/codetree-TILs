n = int(input())

# Please write your code here.
def beut(r):
    count=0
    if r==0:
        return 1
    for i in range(1,r+1):
        count+=beut(r-i)
    return count

print(beut(n))