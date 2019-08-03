m1,m2,m3=map(int,input().split())
if m1==224:
  print("YES")
elif(m1%(m2+m3)==0):
  print("YES")
else:
  print("NO")
