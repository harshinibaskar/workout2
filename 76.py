high=int(input())
if(high>1):
 for i in range(2,high):
  if(high%i==0):
   print("yes")
   break
 else:
   print("no")
