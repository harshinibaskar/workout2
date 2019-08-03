val=int(input())
rate=list(map(int,input().split()))
point=0
for i in range(0,val):
  for j in range(0,i):
    if(rate[j]<rate[i]):
      point=point+rate[j]
print(point)
