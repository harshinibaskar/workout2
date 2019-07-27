ra1,ra2=map(str,input().split())
ra3=0
if len(ra1)>len(ra2):
  ra1,ra2=ra2,ra1
r=0
while r<len(ra1):
  ra3+=(ord(ra2[r])-ord(ra1[r]))
  r+=1
for r in range(r,len(ra2)):
  ra3+=ord(ra2[r])-ord('a')+1
print(ra3)
