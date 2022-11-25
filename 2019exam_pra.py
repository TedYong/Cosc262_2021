#def path_length(parent, start, end):
    #"""find the distance"""
    #trap = []
    #for i in range(len(parent)):
        #if i != start and parent[i] == None:
            #trap.append(i)
    ##if len(trap) == len(parent)-1 and start != end:
        ##return float('inf')
    #current = end
    #path = []
    #distance = 0
    #if current not in trap and parent[current] == None:
        #return distance
    #elif current not in trap and parent[current] not in path:
        #current = parent[current]
        #path.append(current)
        #return path_length(parent, start, current) + 1
    #else:
        #return float('inf')
#def adjacency_list(graph_string):
    #header, *edges = [s.split() for s in graph_string.splitlines()]
    #directed = header[0] == 'D'
    #weighted = len(header) == 3 and header[2] == 'W'
    #num_vertices = int(header[1])
    #adj_list = [[] for _ in range(num_vertices)]
    #for edge in edges:
        #edge_data = map(int, edge)
        #if weighted:
            #source, target, weight = edge_data
        #else:
            #source, target = edge_data
            #weight = None
        #adj_list[source].append((target, weight))
        #if not directed:
            #adj_list[target].append((source, weight))
    #return adj_list    

#def dijkstra(adj_list, start):
    #n = len(adj_list)
    #in_tree = [False for i in range(n)]
    #distance = [float('inf') for i in range(n)]
    #parent = [None for i in range(n)]
    #distance[start] = 0
    #while False in in_tree:
        #u = next_vertex(in_tree, distance)
        #in_tree[u] = True
        #for v, weight in adj_list[u]:
            #if not in_tree[v] and distance[u] + weight < distance[v]:
                #distance[v] = distance[u] + weight
                #parent[v] = u
    #return parent,distance
#def next_vertex(in_tree, distance):
    #maximum = max(distance)
    #result = 0
    #for i in range(len(distance)):
        #if in_tree[i] == False:
            #if distance[i] <= maximum:
                #maximum = distance[i]
                #result = i
    #return result

def fractional_knapsack(capacity, items):
    """practice for knapsack"""
    #cap = capacity
    #n = len(items)
    #cache = [[0 for i in range(cap+1)] for j in range(n+1)]
    #for i in range(1, n+1):
        #for j in range(1, cap+1):
            #if items[i-1][2] <= j:
                #new_value = cache[i-1][items[i-1][2]-j] + items[i-1][1]
                #cache[i][j] = max(cache[i-1][j], new_value)
            #else:
                #cache[i][j] = cache[i-1][j]
    #return cache
    new_list = []
    for i in items:
        new_list.append((i[0], i[1]/i[2], i[2]))
    new_list = sorted(new_list, key= lambda x: x[1], reverse=True)
    total = 0
    value = 0
    for i in range(len(new_list)):
        if total + new_list[i][2] < capacity:
            total += new_list[i][2]
            value += new_list[i][1] * new_list[i][2]
        elif total + new_list[i][2] == capacity:
            total += new_list[i][2]
            value += new_list[i][1] * new_list[i][2]
            break
        elif total + new_list[i][2] > capacity:
            diff = capacity - total
            total += diff
            value += new_list[i][1] * diff
            break
    return value
        
def longest_common_subsequence(list1, list2):
    """find the longest come subsequence"""
    x = len(list1)
    y = len(list2)
    if x == 0 or y == 0:
        return []
    elif list1[-1] == list2[-1]:
        return longest_common_subsequence(list1[:-1], list2[:-1]) + [list1[-1]]
    else:
        one = longest_common_subsequence(list1[:-1], list2)
        two = longest_common_subsequence(list1, list2[:-1])
        #choose = max(len(one), len(two))
        if len(one) > len(two):
            return one
        else:
            return two

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

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __lt__(self, other):
        """For convenience we define '<' to mean
           "less than with respect to angle", i.e.
           the direction of self is less than the
           direction of other in a CCW sense."""
        area = self.x * other.y - other.x * self.y
        return area > 0
        
def is_ccw(p0, p1, p2):
    """True if triangle p0, p1, p2 has vertices in counter-clockwise order"""
    return (p1 - p0) < (p2 - p0)
    
        
def gift_wrap(points):
    """ Given a list of points (Vec objects), return a list of those points
        that lie on the convex hull in CCW order using the Gift Wrap algorithm"""

    # Get the bottom-most and if necessary leftmost point
    #bottommost = points[0]
    #for i in points:
        #if bottommost.y < i.y:
            #bottommost = i
        #elif bottommost.y == i.y:
            #if bottommost.x < bottommost.x:
                #bottommost = i
    bottommost = min(sorted(points, key= lambda x: (x.y, x.x)))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull. When the loop terminates, the
        # variable 'candidate' should be that point.
        for p in points:
            if p == hull[-1]:
                continue
            if candidate == None or is_ccw(hull[-1], p, candidate):
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)
    return hull

def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list    
def next_vertex(in_tree, distance):
    maximum = max(distance)
    result = 0
    for i in range(len(distance)):
        if in_tree[i] == False:
            if distance[i] <= maximum:
                maximum = distance[i]
                result = i
    return result

def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v]= distance[u] + weight
                parent[v]=u
    return parent,distance
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

