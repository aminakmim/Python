class Parent(object):
    def __init__(self,x):
        self.weight = x
    def print_(self):
        print(self.weight)

class Child(Parent):
    def __init__(self,x,y):
        super().__init__(x)
        self.height = y
        
me = Child(4,5) # weight 4 height 5
print(me.weight)
