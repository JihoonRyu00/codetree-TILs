N=int(input())
scores=list(map(float,input().split()))
mean=sum(scores)/N
print(f"{mean:.1f}")
if mean>=4.0:
    print("Perfect")
elif mean>=3.0:
    print("Good")
else:
    print("Poor")