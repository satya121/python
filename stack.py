class stack:
    def __init__(self):
        self.mstack=[]
    def isempty(self):
        return self.mstack==[]
    def push(self,item):
        self.mstack.append(item)
        print("inserted ite,:{}".format(item))
    def pop(self):
        if self.isempty()==False:
            item=self.mstack.pop()
            print("removed item:{}".format(item))
        else:
            print("no item is found")
    def view(self):
        if self.isempty()==False:
            for item in self.mstack:
                print(item)
        else:
            print("no item in stack")
    def size(self):
        return len(self.mstack)
    def top(self):
        if self.isempty()==False:
            return self.mstack[len(self.mstack)-1]
        else:
            return "no item is found"
if __name__=="__main__":
    mstack=stack()
    print("_______")
    print("implementation of stack in python")
    print("______________")
    print("menu items")
    print("1.view the stack")
    print("2.push item into stack")
    print("3.pop item into stack")
    print("4.get the size of stack")
    print("5.get the pop item of stack")
    print("6.quit the program")
    while True:
        a=int(input("enter the option:"))
        if a==1:
            mstack.view()
        elif a==2:
            item=input("enter insert")
            mstack.push(item)
        elif a==3:
            mstack.pop()
        elif a==4:
            print(mstack.size())
        elif a==5:
            print(mstack.top())
        elif a==6:
            break
