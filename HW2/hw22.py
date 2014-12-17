#Hayden Crockett

#2014-10-13

from math import sqrt

class Point(object):
    """docstring for Point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)
        
        return sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Point(%f, %f)' % (self.x, self.y)
    
    
    
    
    
    def cw(self, p, rad):
        if p is None:
            p = Point(0.0, 0.0)
        
        self.x = self.x - p.x
        self.y = self.y - p.y
        
        
        s, c = [f(-rad) for f in (math.sin, math.cos)]
        x, y = (c*self.x - s*self.y +p.x, s*self.x + c*self.y + p.y)
        

        
        return Point(x, y)
    

    
    
    
if __name__ == '__main__':
    p1 = Point(3.0, 4.0)
    p2 = Point(5.0, 8.0)
    
    p3 = p1 + p2
    p4 = Point(1.0, 1.0)
    #print p3.x, p3.y
    #print p1.distance()
    #print p1.distance(p2)
   
    p = Point(0, 0)
    p5 = Point(1,0)
    print p5.cw(p, (pi/2))

