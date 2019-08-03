mat,rat=list(map(int,input().split()))
lis1=list(map(int,input().split()))
for i in range(rat):
  uat1,vat1=list(map(int,input().split()))
  print(sum(lis1[uat1-1:vat1]))
