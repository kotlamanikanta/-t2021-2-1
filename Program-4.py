s=list(map(int,input().split(",")))
l={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,}
for i in s:
    for j in range(1,10):
        if(i%j==0):
           l[j] +=1
print(l) 