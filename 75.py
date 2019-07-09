sky=list(input())
if len(sky)%2==0:
    sky[int(len(sky)/2)] ='*'
    sky[int(len(sky)/2)-1]='*'
else:
    sky[int(len(sky)/2)] ='*'
for i in range(0,len(sky)):
    print(sky[i],end='')
