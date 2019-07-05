bounce=int(input())
if(bounce>1):
   for i in range(2,bounce):
      if(bounce%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
