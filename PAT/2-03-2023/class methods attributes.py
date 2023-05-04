class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("Var1 is:",self.var1)
        print("Var2 is:",self.var2)
obj=abc(10,12)
obj.display()
print("object.__dict__",obj.__dict__)
print("obj.__doc__",obj.__doc__)
print("class.__name__",abc.__name__)
print("object.__module__",obj.__module__)
print("class.__bases__",abc.__bases__)
