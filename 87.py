wall1,wall2=map(int,input().split())
n=1
while(n<=wall1 and n<=wall2):
   if(wall1%n==0 and wall2%n==0):
      cctv=n
   n=n+1
print(cctv)
