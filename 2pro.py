from itertools import combinations
numb ,ra1 = input().split()
ra1 = int(ra1)
ra2 = []
hj = combinations(numb,len(numb)-ra1)
for d in hj:
    ra2.append("".join(d))
print(min(ra2))
