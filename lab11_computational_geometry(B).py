#Question 2
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
    if start == None:
        start = 0
        end = len(nums)
    if (end - start) == 1:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        mid = (end + start) // 2  # Halfway (approx)
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


#Question 7

#class Vec:
    #"""A simple vector in 2D. Can also be used as a position vector from
       #origin to define points.
    #"""
    #point_num = 0
    #box_calls = 0
    #def __init__(self, x, y):
        #self.x = x
        #self.y = y
        #self.label = 'P' + str(Vec.point_num)
        #Vec.point_num += 1

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

    #def in_box(self, bottom_left, top_right):
        #"""True iff this point (warning, not a vector!) lies within or on the
           #boundary of the given rectangular box area"""
        #Vec.box_calls += 1
        #return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    #def __getitem__(self, axis):
        #return self.x if axis == 0 else self.y

    #def __repr__(self):
        #return "({}, {})".format(self.x, self.y)
        
    #def __lt__(self, other):
        #"""Less than operator, for sorting"""
        #return (self.x, self.y) < (other.x, other.y)
        
    
#class KdTree:
    #"""A 2D k-d tree"""
    #LABEL_POINTS = True
    #LABEL_OFFSET_X = 0.25
    #LABEL_OFFSET_Y = 0.25    
    #def __init__(self, points, depth=0, max_depth=10):
        #"""Initialiser, given a list of points, each of type Vec, the current
           #depth within the tree (0 for the root) and the maximum depth
           #allowable for a leaf node.
        #"""
        #if len(points) < 2 or depth >= max_depth: # Ensure at least one point per leaf
            #self.is_leaf = True
            #self.points = points
        #else:
            #self.is_leaf = False
            #self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            #points = sorted(points, key=lambda p: p[self.axis])
            #halfway = len(points) // 2
            #self.coord = points[halfway - 1][self.axis]
            #self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            #self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)
            
    #def points_in_range(self, query_rectangle):
        #"""Return a list of all points in the tree 'self' that lie within or
           #on the boundary of the given query rectangle, which is defined by
           #a pair of points (bottom_left, top_right), both of which are Vecs.
        #"""
        #bl = query_rectangle[0]
        #tr = query_rectangle[1]
        #if self.is_leaf == True:
            #self.result = []
            #for i in self.points:
                #if i.in_box(bl, tr) == True:
                    #self.result.append(i)
        #else:
            #self.result = []
            #bl_check = False
            #tr_check = False
            #if self.axis == 0:
                #if (self.coord >= bl.x and self.coord <= tr.x) or self.coord == bl.x:
                    #bl_check = True
                    #tr_check = True
                #elif self.coord > bl.x:
                    #bl_check = True 
                #elif self.coord < bl.x:
                    #tr_check = True   
            #else:
                #if (self.coord >= bl.y and self.coord <= tr.y) or self.coord == bl.y:
                    #bl_check = True
                    #tr_check = True
                #elif self.coord > bl.y:
                    #bl_check = True 
                #elif self.coord < bl.y:
                    #tr_check = True                   
            #if self.leftorbottom is not None and bl_check:
                #self.result += self.leftorbottom.points_in_range(query_rectangle)
            #if self.rightortop is not None and tr_check:
                #self.result += self.rightortop.points_in_range(query_rectangle)
        #return self.result             
     
    
    
    #def plot(self, axes, top, right, bottom, left, depth=0):
        #"""Plot the the kd tree. axes is the matplotlib axes object on
           #which to plot, top, right, bottom, left are the coordinates of
           #the bounding box of the plot.
        #"""

        #if self.is_leaf:
            #axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            #if self.LABEL_POINTS:
                #for p in self.points:
                    #axes.annotate(p.label, (p.x, p.y),
                    #xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        #else:
            #if self.axis == 0:
                #axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                #self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                #self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            #else:
                #axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                #self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                #self.rightortop.plot(axes, top, right, self.coord, left, depth+1)
        #if depth == 0:
            #axes.set_xlim(left, right)
            #axes.set_ylim(bottom, top)
       
    
    #def __repr__(self, depth=0):
        #"""String representation of self"""
        #if self.is_leaf:
            #return depth * 2 * ' ' + "Leaf({})".format(self.points)
        #else:
            #s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            #s += self.leftorbottom.__repr__(depth + 1) + '\n'
            #s += self.rightortop.__repr__(depth + 1) + '\n'
            #s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            #return s

#Question 12

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)
    
    def in_rect(self, centre, size):
            """returns true if in rectangle"""
            return (centre.x - size <= self.x < centre.x + size and
                    centre.y - size <= self.y < centre.y + size)    
        

class QuadTree:
    """A QuadTree class for COSC262.
       Richard Lobb, May 2019
    """
    MAX_DEPTH = 20
    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.centre = centre
        self.size = size
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []
        self.points = [point for point in points if point.in_rect(self.centre, self.size / 2)]
        if len(self.points) > self.max_leaf_points:
            self.is_leaf = False
            for i in range(4):
                if i == 0:
                    child_centre = Vec(self.centre.x - self.size / 4,
                                            self.centre.y - self.size / 4)
                elif i == 1:
                    child_centre = Vec(self.centre.x - self.size / 4,
                                            self.centre.y + self.size / 4)
                elif i == 2:
                    child_centre = Vec(self.centre.x + self.size / 4,
                                            self.centre.y - self.size / 4)
                elif i == 3:
                    child_centre = Vec(self.centre.x + self.size / 4,
                                            self.centre.y + self.size / 4)
                child = QuadTree(self.points, child_centre, self.size / 2,
                                 self.depth + 1, self.max_leaf_points)
                self.children.append(child)
        else:
            self.is_leaf = True


    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)
                
    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s

import matplotlib.pyplot as plt
points = [(60, 15), (15, 60), (30, 58), (42, 66), (40, 70)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(50, 50), 100)
print(tree)
