n= int(input())
i=1
if(n%2==0):
    n=n-1
    while(n>0):
        print(i)
        i=i+2
        n=n-1
else:
    while(n>0):
        print(i)
        i=i+2
        n=n-1 