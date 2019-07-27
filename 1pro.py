ra1=int(input())
ra2=[]
for h in range(0,ra1):
 pan=input()
 ra2.append(pan)
ra3=[]
for h in zip(*ra2):
 if(h.count(h[0])==len(h)):
  r3.append(h[0])
 else:
  break
print(''.join(ra3))
