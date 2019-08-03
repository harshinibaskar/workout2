ready=int(input())
steady=list(map(int,input().split()))
go=0
for one1 in range(ready):
    for two2 in range(one1,ready):  
        for three3 in range(two2,ready):
            if steady[one1]<steady[two2]<steady[three3]:
                go+=1
print(go)
