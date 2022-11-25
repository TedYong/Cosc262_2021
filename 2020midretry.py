###Question14###
class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)


def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0 

def leftmost_vertex(polygon, p):
    new_p = sorted(polygon, key= lambda p:(p.x, p.y))
    result = new_p[0]
    for i in range(len(new_p)):
        if is_ccw(p, result, new_p[i]):
            result = new_p[i]
    return result
	          
square = [Vec(0, 0), Vec(100, 0), Vec(100, 100), Vec(0, 100)]
p = Vec(-50, 50)
leftmost = leftmost_vertex(square, p)
print(leftmost)

