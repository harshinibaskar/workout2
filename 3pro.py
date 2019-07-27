ra1,ra2=input().split()
ra3=abs(len(ra2)-len(ra1))
for g in range(len(ra1)):
    if(len(ra2)==1 and ra2[g] in ra1):
        break
    if (ra1[g]!=ra2[g]):
        ra3=ra3+1
print(ra3)
