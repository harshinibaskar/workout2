n,d=map(int,input().split())
n=n*d
for i in range(0,n+1):
 if(i**2==0):
  print("yes")
  break
else:
 print("no")
