ma=int(input())
cu=0
ta=[]
for i in range(1,ma+1):
  ta.append(i)
for i in range(len(ta)):
  for i in range(i+1,len(ta)):
    cu+=1
print(cu)
