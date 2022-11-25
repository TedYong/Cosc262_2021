###Question 4###

#num_calls = 0  # Global counter of mat_mul calls

#def mat_mul(m1, m2):
    #"""Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       #as lists of lists.
    #"""
    #global num_calls # Counter of calls (for marking)
    #num_calls += 1   # Increment the count of calls
    #n = len(m1)    # Size of the matrix
    #assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    #mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        #for i in range(n)]
    #return mprod

#def mat_power(m, p):
    #if p == 1:
        #return m
    #else:
        #value = mat_power(m, p//2)
        #if p%2 == 0:
            #return mat_mul(value, value)
        #else:
            #return mat_mul(m, mat_mul(value, value))
###Question 16###

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
    """find the leftmost point based on p"""
    return sorted(polygon, key=lambda p:(p.x, p.y))
    
square = [Vec(0, 0), Vec(100, 0), Vec(100, 100), Vec(0, 100)]
p = Vec(-50, 50)
leftmost = leftmost_vertex(square, p)
print(leftmost)