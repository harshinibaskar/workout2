eva=list(input())
i=[]
for j in eva:
   if j not in i:
      i.append(j)
if eva==i:
   print("Yes")
else:
   print("No")
