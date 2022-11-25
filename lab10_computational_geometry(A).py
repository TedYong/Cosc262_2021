###Question 4###
#class Vec:
    #"""A simple vector in 2D. Also used as a position vector for points"""
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y
        
    #def __add__(self, other):
        #return Vec(self.x + other.x, self.y + other.y)
        
    #def __sub__(self, other):
        #return Vec(self.x - other.x, self.y - other.y)
    
    #def __mul__(self, scale):
        #"""Multiplication by a scalar"""
        #return Vec(self.x * scale, self.y * scale)
        
    #def dot(self, other):
        #return self.x * other.x + self.y * other.y
        
    #def lensq(self):
        #return self.dot(self)

    #def __str__(self):
        #return "({}, {})".format(self.x, self.y)
        
        
#def signed_area(a, b, c):
    #"""Twice the area of the triangle abc.
       #Positive if abc are in counter clockwise order.
       #Zero if a, b, c are colinear.
       #Otherwise negative.
    #"""
    #p = b - a
    #q = c - a
    #return p.x * q.y - q.x * p.y

#def is_on_segment(p, a, b):
    #result = False
    #c = b.__sub__(a)
    #first = (p.__sub__(a)).lensq()
    #second = (p.__sub__(b)).lensq()
    #if signed_area(p, a, b) == 0 and (first <= c.lensq() and second <= c.lensq()):
        #result = True
    #return result

###Question 5###
    
#class Vec:
    #"""A simple vector in 2D. Can also be used as a position vector from
       #origin to define points.
    #"""
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y

    #def __repr__(self):
        #"""Return this point/vector as a string in the form "(x, y)" """
        #return "({}, {})".format(self.x, self.y)

    #def __add__(self, other):
        #"""Vector addition"""
        #return Vec(self.x + other.x, self.y + other.y)

    #def __sub__(self, other):
        #"""Vector subtraction"""
        #return Vec(self.x - other.x, self.y - other.y)
    
    #def __mul__(self, scale):
        #"""Multiplication by a scalar"""
        #return Vec(self.x * scale, self.y * scale)

    #def dot(self, other):
        #"""Dot product"""
        #return self.x * other.x + self.y * other.y

    #def lensq(self):
        #"""The square of the length"""
        #return self.dot(self)


#def is_ccw(a, b, c):
    #"""True iff triangle abc is counter-clockwise."""
    #p = b - a
    #q = c - a
    #area = p.x * q.y - q.x * p.y
    ## May want to throw an exception if area == 0
    #return area > 0

#def classify_points(line_start, line_end, points):
    #left = 0
    #right = 0
    #for i in points:
        #if is_ccw(line_start, line_end, i):
            #left += 1
        #else:
            #right += 1
    #return (right, left)

###Question 6###
#class Vec:
    #"""A simple vector in 2D. Also use for points (position vector)"""
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y
        
    #def __add__(self, other):
        #return Vec(self.x + other.x, self.y + other.y)
        
    #def __sub__(self, other):
        #return Vec(self.x - other.x, self.y - other.y)
    
    #def __mul__(self, scale):
        #"""Multiplication by a scalar"""
        #return Vec(self.x * scale, self.y * scale)
        
    #def dot(self, other):
        #return self.x * other.x + self.y * other.y
        
    #def lensq(self):
        #return self.dot(self)
        
        
#def is_ccw(a, b, c):
    #"""True iff triangle abc is counter-clockwise"""
    #p = b - a
    #q = c - a
    #area = p.x * q.y - q.x * p.y
    ## May want to throw an exception if area == 0
    #return area > 0 

#def intersecting(a, b, c, d):
    #result = False
    #ver1 = is_ccw(a, c, b) != is_ccw(a, d, b)
    #ver2 = is_ccw(c, a, d) != is_ccw(c, b, d)
    #if ver1 and ver2:
        #result = True
    #return result

###Question 7###
#class Vec:
    #"""A simple vector in 2D. Also use for points (position vector)"""
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y
        
    #def __add__(self, other):
        #return Vec(self.x + other.x, self.y + other.y)
        
    #def __sub__(self, other):
        #return Vec(self.x - other.x, self.y - other.y)
    
    #def __mul__(self, scale):
        #"""Multiplication by a scalar"""
        #return Vec(self.x * scale, self.y * scale)
        
    #def dot(self, other):
        #return self.x * other.x + self.y * other.y
        
    #def lensq(self):
        #return self.dot(self)
        
        
#def is_ccw(a, b, c):
    #"""True iff triangle abc is counter-clockwise"""
    #p = b - a
    #q = c - a
    #area = p.x * q.y - q.x * p.y
    ## May want to throw an exception if area == 0
    #return area > 0
#def is_strictly_convex(vertices):
    #result = True
    #i = 0
    #while i < len(vertices):
        #a = vertices[i]
        #b = vertices[(i+1) % len(vertices)]
        #c = vertices[(i+2) % len(vertices)]
        #if not is_ccw(a, b, c):
            #result = False
        #i+=1
    
    #return result

###Question 10###
#class Vec:
    #"""A simple vector in 2D. Can also be used as a position vector from
       #origin to define points.
    #"""
    #def __init__(self, x, y):
	#self.x = x
	#self.y = y

    #def __repr__(self):
	#"""Return this point/vector as a string in the form "(x, y)" """
	#return "({}, {})".format(self.x, self.y)

    #def __add__(self, other):
	#"""Vector addition"""
	#return Vec(self.x + other.x, self.y + other.y)

    #def __sub__(self, other):
	#"""Vector subtraction"""
	#return Vec(self.x - other.x, self.y - other.y)
    
    #def __mul__(self, scale):
	#"""Multiplication by a scalar"""
	#return Vec(self.x * scale, self.y * scale)

    #def dot(self, other):
	#"""Dot product"""
	#return self.x * other.x + self.y * other.y

    #def lensq(self):
	#"""The square of the length"""
	#return self.dot(self)


#def is_ccw(a, b, c):
    #"""True iff triangle abc is counter-clockwise."""
    #p = b - a
    #q = c - a
    #area = p.x * q.y - q.x * p.y
    ## May want to throw an exception if area == 0
    #return area > 0 

#def gift_wrap(points):
    #""" Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    ## Get the bottom-most point (and left-most if necessary).
    #assert len(points) >= 3
    #bottommost = min(points, key=lambda p: (p.y, p.x))
    #hull = [bottommost]
    #done = False
    
    ## Loop, adding one vertex at a time, until hull is (about to be) closed.
    #while not done:
	#candidate = None
	## Loop through all points, looking for the one that is "rightmost"
	## looking from last point on hull
	#for p in points:
	    #if p is hull[-1]:
		#continue
	    #if candidate == None or is_ccw(hull[-1], p, candidate):
		#candidate = p
	#if candidate is bottommost:
	    #done = True    # We've closed the hull
	#else:
	    #hull.append(candidate)
    #return hull
#points = [
    #Vec(1, 99),
    #Vec(0, 100),
    #Vec(50, 0),
    #Vec(50, 1),
    #Vec(50, 99),
    #Vec(50, 50),
    #Vec(100, 100),
   #Vec(99, 99)]
#verts = gift_wrap(points)
#for v in verts:
    #print(v)

###Question 12###
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

	
class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
	"""Construct an instance of the sort key"""
	self.direction = p - bottommost
	self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
	
    def __lt__(self, other):
	"""Compares two sort keys. p1 < p2 means the vector the from bottommost point
	   to p2 is to the left of the vector from the bottommost to p1.
	"""
	if self.is_bottommost:
	    return True   # Ensure bottommost point is less than all other points
	elif other.is_bottommost:
	    return False  # Ensure no other point is less than the bottommost
	else:
	    area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
	    return area > 0    
def simple_polygon(points):
    bottom = None
    for i in points:
	if PointSortKey.__lt__(i) == True:
	    bottom = i
    return bottom


points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = simple_polygon(points)
for v in verts:
    print(v)