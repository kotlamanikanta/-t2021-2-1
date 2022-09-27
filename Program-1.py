class main:
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def performAction(self,a,b,c):
        if(c=="+"):
            return a+b
        elif(c=="-"):
            return a-b
        elif(c=="*"):
            return a*b
        elif(c=="/"):
            return a/b
        else:
            return "Operator given is worng"
a=float(input())
b=float(input())
c=input()

x=main(a,b,c)
print(x.performAction(a,b,c))
