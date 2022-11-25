#def lcs(s1, s2, cache=None):
    #"""yoyoyo"""
    #x=len(s1)
    #y=len(s2)
    #if cache == None:
        #cache=[[None for i in range(y+1)] for j in range(x+1)]
    #if cache[x][y] != None:
        #return cache[x][y]
    #if x == 0 or y == 0:
        #return ''
    #elif s1[x-1] == s2[y-1]:
        #cache[x][y] = lcs(s1[:-1],s2[:-1],cache) + s1[x-1]
        #return cache[x][y]
    #else:
        #one = lcs(s1[:-1],s2,cache)
        #two = lcs(s1, s2[:-1], cache)
        #if len(one) > len(two):
            #cache[x][y] = one
            #return cache[x][y]
        #else:
            #cache[x][y] = two
            #return cache[x][y]

#def lcs(s1, s2):
    #x = len(s1)
    #y = len(s2)
    #cache = [[0 for i in range(y+1)] for j in range(x+1)]
    
    #for i in range(1,x+1):
        #for j in range(1,y+1):
            #if s1[x-1] == s2[y-1]:
                #cache[i][j] = cache[i-1][j-1] + 1
            #else:
                #one = cache[i-1][j]
                #two = cache[i][j-1]
                #if one > two:
                    #cache[i][j] = one
                #else:
                    #cache[i][j] = two
    #result = []
    #while x > 0 and y > 0:
        #if s1[x-1] == s2[y-1]:
            #result.append(s1[x-1])
            #x-=1
            #y-=1
        #else:
            #if cache[x-1][y] > cache[x][y-1]:
                #x-=1
            #else:
                #y-=1
    #return ''.join(reversed(result))

#def lcs(s1, s2):
    #"""hahah"""
    #x = len(s1)
    #y = len(s2)
    #cache = [[0 for j in range(y+1)] for i in range(x+1)]
    #for i in range(1,x+1):
        #for j in range(1,y+1):
            #if s1[i-1] == s2[j-1]:
                #cache[i][j] = cache[i-1][j-1] + 1
            #else:
                #one = cache[i-1][j]
                #two = cache[i][j-1]
                #if one > two:
                    #cache[i][j] = one
                #else:
                    #cache[i][j] = two
    #a = x
    #b = y
    #result = []
    #while a > 0 and b > 0:
        #if s1[a-1] == s2[b-1]:
            #result.append(s1[a-1])
            #a-=1
            #b-=1
        #else:
            #if cache[a-1][b] > cache[a][b-1]:
                #a-=1
            #else:
                #b-=1
    #return ''.join(reversed(result))
#def line_edits(s1, s2):
    #n1 = str.splitlines(s1)
    #n2 = str.splitlines(s2)
    #x = len(n1)
    #y = len(n2)
    #cache = [[0 for i in range(y+1)] for j in range(x+1)]
    
    #for i in range(x+1):
        #for j in range(y+1):
            #if i == 0 or j == 0:
                #cache[i][j] = max(i,j)
            #elif n1[i-1] == n2[j-1]:
                #cache[i][j] = cache[i-1][j-1]
            #else:
                #one = cache[i-1][j]
                #two = cache[i][j-1]
                #three = cache[i-1][j-1]
                #value = min(one, two, three)
                #cache[i][j] = value + 1                
    #result = []
    #while x > 0 or y > 0:
        #one = cache[x-1][y]
        #two = cache[x][y-1]
        #three = cache[x-1][y-1]  
        #value = min(one, two, three)        
        #if (x>0 and y>0) and n1[x-1] == n2[y-1]:
            #result.append(('C', n1[x-1], n2[y-1]))
            #x-=1
            #y-=1
        #elif (x>0 and y>0) and value == three:
            #common = lcs(n1[x-1], n2[y-1])
            #for i in range(len(n1[x-1])):
                #if n1[x-1][i] not in common:
                    #new1 = n1[x-1].replace(n1[x-1][i], "[["+n1[x-1][i]+"]]")
            #for i in range(len(n2[y-1])):
                #if n2[y-1][i] not in common:
                    #new2 = n2[y-1].replace(n2[y-1][i], "[["+n2[y-1][i]+"]]")            
            ##result.append(('S', n1[x-1], n2[y-1]))
            #result.append(('S', new1, new2))
            #x-=1
            #y-=1    
        #elif (x > 0) and value == one:
            #result.append(('D', n1[x-1], ''))
            #x-=1 
        #elif (y > 0) and value == two:
            #result.append(('I', '', n2[y-1]))
            #y-=1
    #return reversed(result)

                    
#s1 = "Line1\nLine2\nLine3\nLine4\n"
#s2 = "Line5\nLine4\nLine3\n"
#table = line_edits(s1, s2)
#for row in table:
    #print(row)
#from collections import defaultdict  
#def change_greedy(amount, coinage):
    #result = defaultdict(int)
    #coinage = sorted(coinage, reverse=True) #[25, 10, 5, 1]
    #final = []
    #i = 0
    #while amount > 0:
        #if i > len(coinage) - 1:
            #return None  
        #else:
            #while coinage[i] > amount:
                #if i > len(coinage) - 1:
                    #return None     
                #else:
                    #i += 1
            #result[coinage[i]] += 1
            #amount -= coinage[i]
        
  
    #for i in result:
        #final.append((i, result[i])) 
    #return final 
#print(change_greedy(82, [10, 25, 5]))

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
#def simple_polygon(points):
    #"""hahahhaahha"""
    #bottommost = min(points, key= lambda x: (x.y, x.x))
    #result = sorted(points, key= lambda x: PointSortKey(x, bottommost))
    #return result
def graham_scan(points):
    """construct the graham algorithm YEAH"""
    bottommost = min(points, key= lambda x: (x.y, x.x))
    n_points = sorted(points, key= lambda x: PointSortKey(x, bottommost))
    stacc = [n_points[0], n_points[1], n_points[2]]
    for i in range(3, len(n_points)):
        while not is_ccw(stacc[-2], stacc[-1], n_points[i]):
            stacc.pop()
        stacc.append(n_points[i])
    return stacc
points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = graham_scan(points)
for v in verts:
    print(v)
    