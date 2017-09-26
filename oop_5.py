import math

class Point(object):
        """docstring for Point"""
        def __init__(self, x=0,y=0):
                self.x = x
                self.y = y
        def __str__(self):
                s = str(self.x)+" "+str(self.y)
                return s
        def quadrant(self):
                temp = 0
                if (self.x <0):
                        if (self.y < 0):
                                temp = 3
                        else:temp=2
                elif (self.y < 0):
                        temp = 4
                else:
                        temp = 1
                print(temp)
        def distance(self,p2):
            d = 0
            d = math.sqrt((p2.x-self.x)**2+(p2.y-self.y)**2)
            return d

class Cloud(object):
    """docstring for Cloud"""
    def __init__(self, limit):
        self.max_limit = limit
        self.point_list = []

    def is_full(self):
        return (len(self.point_list) >= self.max_limit)

    def is_empty(self):
        return (len(self.point_list) <= 0)
    def extreme(self):
        pass
    def add_point(self,p):
        if not(self.is_full()):
            self.point_list.append(p)
        else:
            print("Cloud is Full.")
        



p = []

for i in range(6):
    temp = Point(i**2,i**3)
    p.append(temp)
c = Cloud(3)
for x in p:
    c.add_point(x)
    #print(c.is_full())
#print(p.distance(p2))
