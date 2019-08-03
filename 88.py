import math
walli=[int(i) for i in input().split()]
print(int(((walli[0]*walli[1])/(math.gcd(walli[0],walli[1])))))
