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

        
#class PointSortKey:
    #"""A class for use as a key when sorting points wrt bottommost point"""
    #def __init__(self, p, bottommost):
        #"""Construct an instance of the sort key"""
        #self.direction = p - bottommost
        #self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    #def __lt__(self, other):
        #"""Compares two sort keys. p1 < p2 means the vector the from bottommost point
           #to p2 is to the left of the vector from the bottommost to p1.
        #"""
        #if self.is_bottommost:
            #return True   # Ensure bottommost point is less than all other points
        #elif other.is_bottommost:
            #return False  # Ensure no other point is less than the bottommost
        #else:
            #area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            #return area > 0
#def simple_polygon(points):
    #"""construct a simply polygon"""
    #bottommost = points[0]
    #for i in points:
        #if i.y < bottommost.y:
            #bottommost = i
        #elif i.y == bottommost.y:
            #if i.x < bottommost.x:
                #bottommost = i
    #return sorted(points, key=lambda p: PointSortKey(p, bottommost))

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
#class PointSortKey:
    #"""A class for use as a key when sorting points wrt bottommost point"""
    #def __init__(self, p, bottommost):
        #"""Construct an instance of the sort key"""
        #self.direction = p - bottommost
        #self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    #def __lt__(self, other):
        #"""Compares two sort keys. p1 < p2 means the vector the from bottommost point
           #to p2 is to the left of the vector from the bottommost to p1.
        #"""
        #if self.is_bottommost:
            #return True   # Ensure bottommost point is less than all other points
        #elif other.is_bottommost:
            #return False  # Ensure no other point is less than the bottommost
        #else:
            #area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            #return area > 0
#def is_ccw(a, b, c):
    #"""True iff triangle abc is counter-clockwise"""
    #p = b - a
    #q = c - a
    #area = p.x * q.y - q.x * p.y
    ## May want to throw an exception if area == 0
    #return area > 0    

#def graham_scan(points):
    #"""another better way"""
    #bottom = points[0]
    #for i in points:
        #if i.y < bottom.y:
            #bottom = i
        #elif i.y == bottom.y:
            #if i.x < bottom.x:
                #bottom = i     
    #result = sorted(points, key=lambda p: PointSortKey(p, bottom))
    #stacc = [result[0], result[1], result[2]]
    #for i in range(3, len(result)):
        #while not is_ccw(stacc[-2], stacc[-1], result[i]):
            #stacc.pop()
        #stacc.append(result[i])
    #return stacc
# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, start=None, end=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
    n = len(nums)
    if start == None:
        start = 0
        end = n
    if end-start == 1:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        mid = (start+end)// 2  # Halfway (approx)
        left = binary_search_tree(nums, True, start, mid)
        right = binary_search_tree(nums, True, mid, end)
        tree = Node(nums[mid - 1], left, right)
    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)


nums = [22, 41, 19, 27, 12, 35, 14, 20,  39, 10, 25, 44, 32, 21, 18]
tree = binary_search_tree(nums)
print_tree(tree)
            
