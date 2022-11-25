"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    for row_num in range(1, n_rows):
        for col_num in range(n_cols):
            if col_num == 0:
                grid[row_num][col_num] += min(grid[row_num-1][col_num:col_num+2])
            elif col_num == n_cols-1:
                grid[row_num][col_num] += min(grid[row_num-1][col_num-1:col_num])
            else:
                grid[row_num][col_num] += min(grid[row_num-1][col_num-1:col_num+2])
    return min(grid[n_rows-1])
    
                                              
            
    # **** Your code goes here. It must compute a value 'best', which is
    # the minimum cost from the top of the grid to the bottom.    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension"""
    true_result = []
    result = dict()
    for coin in coinage:
        result[coin] = 0
    numCoins = [0] * (value + 1)
    parent = [0] * (value + 1)
    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if amt >= c:
                coin_count = numCoins[amt - c]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    parent[amt] = amt - c
        numCoins[amt] = 1 + minimum
    i = value
    while i > 0:
        diff = i - parent[i]
        result[diff] += 1
        i -= diff
    for i in result:
        if result[i] != 0:
            true_result.append((i, result[i]))
    return sorted(true_result, key= lambda x:x[0], reverse=True)
    
#import sys
#sys.setrecursionlimit(2000)

#class Item:
    #"""An item to (maybe) put in a knapsack. Weight must be an int."""
    #def __init__(self, value, weight):
        #self.value = value
        #self.weight = weight

    #def __repr__(self):
        #"""The representation of an item"""
        #return f"Item({self.value}, {self.weight})"
        
#def max_value(items, capacity, cache=None):
    #"""find the max value by using Top_down DP"""
    #if cache == None:
        #cache = dict()
    #if len(items) == 0:
        #return 0
    #elif items[-1].weight > capacity:
        #return max_value(items[:-1], capacity, cache)
    #else:
        #if (len(items), capacity) not in cache:
            #cache[(len(items), capacity)] = max(max_value(items[:-1], capacity, cache), 
                   #items[-1].value + max_value(items[:-1], capacity - items[-1].weight, cache))
        #return cache[(len(items), capacity)] 

#class Item:
    #"""An item to (maybe) put in a knapsack"""
    #def __init__(self, value, weight):
        #self.value = value
        #self.weight = weight
        
    #def __repr__(self):
        #return f"Item({self.value}, {self.weight})"
        
        
#def max_value(items, capacity):
    #"""The maximum value achievable with a given list of items and a given
       #knapsack capacity."""
    
    #n = len(items)
    #cache = [[0 for i in range(capacity+1)] for j in range(n+1)]
    
    #for i in range(1, n+1):
        #for j in range(1, capacity+1):
            #if items[i-1].weight <= j:
                #new_value = items[i-1].value + cache[i-1][j - items[i-1].weight]
                #cache[i][j] = max(new_value, cache[i-1][j])
            #else:
                #cache[i][j] = cache[i-1][j-1]
    #return cache[-1][-1]

import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
	
def max_value(items, capacity):
    n_items = len(items)
    caps = capacity
    cache = [[0 for i in range(caps+1)] for j in range(n_items+1)]
    for i in range(1,n_items+1):
        for j in range(1,caps + 1):
            if items[i-1].weight <= j:
                new_value = cache[i-1][j-items[i-1].weight] + items[i-1].value
                cache[i][j] = max(cache[i-1][j], new_value)
            else:
                cache[i][j] = cache[i-1][j] 
    
    x = len(items)
    y = capacity
    result=[]
    
    while x>0 and y>0:
        if cache[x][y] != cache[x-1][y]:
            result.append(items[x-1])
            y-=items[x-1].weight
        x -= 1
    return result
   
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
for capacity in range(26):
    print(f"{capacity:2}: {max_value(items, capacity)}")
    
    
#def lcs(s1, s2):
    #"""bottom up practice"""
    #result = []
    #x = len(s1)
    #y = len(s2)
    #cache = [[0 for i in range(y+1)] for j in range(x+1)]
    #for i in range(1,x+1):
        #for j in range(1,y+1):
            #if s1[i-1] == s2[j-1]:
                #cache[i][j] = cache[i-1][j-1]+1
            #elif s1[i-1] != s2[j-1]:
                #value1 = cache[i-1][j] 
                #value2 = cache[i][j-1]
                #cache[i][j] = max(value1, value2)
    #a = x
    #b = y
    #point = cache[a][b]
    #while a > 0 and b > 0:
        #if s1[a-1] == s2[b-1]:
            #point = cache[a-1][b-1]
            #result.append(s1[a-1])
            #a-=1
            #b-=1
        #else:
            #point = max(cache[a-1][b], cache[a][b-1])
            #if point == cache[a-1][b]:
                #a-=1
            #else:
                #b-=1
    #return ''.join(reversed(result))

def lcs(s1, s2, cache=None):
    n_s1 = len(s1)
    n_s2 = len(s2)
    if cache is None:
        cache = [[None for j in range(n_s2 + 1)] for i in range(n_s1+1)]
    if cache[n_s1][n_s2] != None:
        return cache[n_s1][n_s2] 
    if s1 == '' or s2 == '':
        return ''
    elif s1[-1] == s2[-1]: # Last chars match
        cache[n_s1][n_s2] = lcs(s1[:-1], s2[:-1], cache) + s1[-1]
        
        return cache[n_s1][n_s2]    
    else:
       # Drop last char of each string in turn.
       # Choose best outcome. 
        soln1 = lcs(s1[:-1], s2, cache)
        soln2 = lcs(s1, s2[:-1], cache)
        if len(soln1) > len(soln2):
            cache[n_s1][n_s2] = soln1
            return soln1
        else:
            cache[n_s1][n_s2] = soln2
            return soln2          

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))