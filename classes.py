class Points:  # pascal naming convention is used

    def move(self):
        print( "move" )

    def draw(self):
        print( "draw" )


p1 = Points()
p1.x = 10
p1.y = 20
print( p1.x )
p1.draw()

p2 = Points()
p2.x = 1
print( p2.x )
p2.move()


class PointNew:  # pascal naming convention is used

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print( "move" )

    def draw(self):
        print( "draw" )

point = PointNew(10, 20)
print(point.x)
point.x = 11
print(point.x)


class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John")
john.talk()

bob = Person("Bob")
bob.talk()