class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.x = y
    
    def get(self):
        return self.x, self.y

    def movie(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

p = Point()
print(p)

p.movie(3, -5)
print(p)

q = Point(3, 4)
print(q)
