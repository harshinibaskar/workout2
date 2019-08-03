w=int(input())
m=0
for v in range(0,w):
  if(pow(2,v)>w):
    break
  m=w-pow(2,v)
print(m)
