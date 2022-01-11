from urllib import request
print(2**48)
class Point:
    mini = 3
    maxi = 5

    @classmethod
    def get_mini_maxi(cls):
        return cls.maxi, cls.mini

    @classmethod
    def increase_mini_maxi(cls):
        cls.maxi += 1
        cls.mini += 1

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


print(Point.get_mini_maxi())
p = Point(2, 3)

print(p.get_mini_maxi())
p.increase_mini_maxi()
print(p.get_mini_maxi())
