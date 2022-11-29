class Table:
    def __init__(self):
        self.a=int(input("enter up to which you want :"))

    def multi (self):
        for i in range (2,self.a+1):
            for j in range (1, 11):
                print(i,"*",j,"=",i*j)
                j+=1
            print("************")
            i+=1
ob1=Table()
ob1.multi()

