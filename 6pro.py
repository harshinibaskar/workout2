s1=int(input())
s2=list(map(int,input().split()))
s3=0
for one1 in range(s1):
    for two2 in range(one1,s1):  
        for three3 in range(two2,s1):
            if s2one1]<s2two2]<s2three3]:
                s3+=1
print(s3)
