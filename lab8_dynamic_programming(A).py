###Question 2, 3 and 4###
#from functools import lru_cache
import numpy as np
"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

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

###Question 2 part###
#def grid_cost(grid):
    #"""The cheapest cost from row 1 to row n (1-origin) in the given
       #grid of integer weights.
    #"""
    #n_rows = len(grid)
    #n_cols = len(grid[0])
    ##@lru_cache(maxsize=None)
    #def cell_cost(row, col):
        #"""The cost of getting to a given cell in the current grid."""
        #if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            #return INFINITY  # Off-grid cells are treated as infinities
        #else:
            #cost = grid[row][col]            
            #if row != 0:
                #cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
            #return cost
            
    #best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    #return best
    
###Question 3 part###
#def grid_cost(grid):
    #"""The cheapest cost from row 1 to row n (1-origin) in the given
       #grid of integer weights.
    #"""
    #cashe = [[None for x in range(len(grid[0]))] for y in range(len(grid))]
    #n_rows = len(grid)
    #n_cols = len(grid[0])
    
    #def cell_cost(row, col):
        #"""The cost of getting to a given cell in the current grid."""
        #if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            #return INFINITY  # Off grid cells are treated as infinities
        #elif cashe[row][col] is None:
            #cost = grid[row][col]
            #if row != 0:
                #cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
            #cashe[row][col] = cost
            #return cashe[row][col]
        #else:
            #return cashe[row][col]
            
    #best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    #return best
###Question 4###
#def grid_cost(grid):
    #"""The cheapest cost from row 1 to row n (1-origin) in the given
       #grid of integer weights.
    #"""
    #n_rows = len(grid)
    #n_cols = len(grid[0])
    #cache = np.zeros((n_rows, n_cols), int)
    #for i in range(n_rows):
        #for j in range(n_cols):
            #cache[i, j] = grid[i][j]
    #for row_num in range(1, n_rows):
        #for col_num in range(0, n_cols):
            #if col_num == 0:
                #cache[row_num, col_num] += min(cache[row_num - 1, 0:2]) 
            #elif col_num == n_cols - 1:
                #cache[row_num, col_num] += min(cache[row_num - 1, col_num-1:]) 
            #else:
                #cache[row_num, col_num] += min(cache[row_num - 1, col_num-1:col_num+2]) 
         
    #best = min(cache[n_rows-1])
    #return best
    
#def file_cost(filename):
    #"""The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       #weights read from the given file
    #"""
    #return grid_cost(read_grid(filename))
#print(read_grid('lab8testf.py'))
#print(file_cost('checkerboard.trivial.in'))
#print(file_cost('checkerboard.small.in'))
#print(file_cost('lab8testf.py'))

###Question 8###
#def coins_reqd(value, coinage):
    #"""The minimum number of coins to represent value assuming a 1-unit coin"""
    #num_coins = [0] * (value + 1)
    #for amt in range(1, value + 1):
        #num_coins[amt] = 1 + min(num_coins[amt - c] for c in coinage if amt >= c)

    ## The value of the num_coins array is displayed at this point.
    #return num_coins[value]

###Question 10###
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
    #n_items = len(items)
    #if cache == None:
        #cache = dict()
    #if n_items == 0:
        #return 0
    #elif items[0].weight > capacity:
        #return max_value(items[1:], capacity, cache)
    #else:
        #if (n_items, capacity) not in cache:
            #cache[(n_items, capacity)] = max(max_value(items[1:], capacity, cache),
                                             #items[0].value + max_value(items[1:], 
                                                                        #capacity - items[0].weight,cache))
        #return cache[(n_items, capacity)]


#items = [
    #Item(45, 3),
    #Item(45, 3),
    #Item(80, 4),
    #Item(80, 5),
    #Item(100, 8)]

#print(max_value(items, 10))

###Question 9 ###
#def coins_reqd(value, coinage):
    #"""A version that doesn't use a list comprehension"""
    #numCoins = [0] * (value + 1)
    #coin = [0] * (value + 1)
    #result = {}
    #for num in coinage:
        #result[num] = 0
    #for amt in range(1, value + 1):
        #minimum = None
        #for c in coinage:
            #if amt >= c:
                #coin_count = numCoins[amt - c]  # Num coins required to solve for amt - c
                #if minimum is None or coin_count < minimum:
                    #minimum = coin_count
                    #coin[amt] = amt - c
        #numCoins[amt] = 1 + minimum
    #index = value
    #while value > 0:
        #gap = value - coin[value]
        #result[gap] += 1
        #index -= gap
        #value -= gap
    #final_result = []
    #for coin, num in result.items():
        #if num != 0:
            #final_result.append((coin, num))
            
    #return sorted(final_result, key=lambda x: x[0], reverse=True)
#print(coins_reqd(32, [1, 10, 25]))
#def coins_reqd(value, coinage):
    #"""The minimum number of coins to represent value"""
    #numCoins = [0] * (value + 1)
    #for amt in range(min(coinage), value + 1):
        #numCoins[amt] = 1 + min(numCoins[amt - c] for c in coinage if  amt >=  c)
    #return numCoins[value]
#print(coins_reqd(32, [1, 10, 25]))

#def coins_reqd(value, coinage):
    #"""The minimum number of coins to represent value"""
    #num_coins = [0] * (value + 1)
    #path_list = [None for x in range(value + 1)]
    #for amt in range(min(coinage), value + 1):
        #min_coin = float('inf')
        #for c in coinage:
            #if amt >=c:
                #if num_coins[amt - c] < min_coin:
                    #min_coin = num_coins[amt - c]
                    #path_list[amt] = c
        #num_coins[amt] = 1 + min_coin
    #coin_used = [[coin, 0] for coin in coinage]
    #cvalue = value
    #while cvalue > 0:

        #coin = path_list[cvalue]
        #for used in coin_used:
            #if used[0] == coin:
                #used[1] += 1
        #cvalue -= coin
    #coin_final = coin_used[:]
    #for coin in coin_used:
        #if coin[1] == 0:
            #coin_final.remove([coin[0], 0])
    #coin_tuple = []
    #for coins in coin_final:
        #coin_tuple.append(tuple(coins))
    #coin_tuple.sort(reverse=True, key=lambda x: x[0])
    #return coin_tuple

#print(coins_reqd(32, [1, 10, 25]))

###Jessie's work###
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

##Your function must use a top-down DP approach, 
##so any use of loops or list comprehensions is disallowed.  

     
#def max_value(items, capacity, n = None, cache=None):
    ## Return the maximum value achievable with the first
    ##  n items and the given capacity of knapsack

      
    #if n == None: #first call
        #n = len(items)
        #cache = [[-1] * (capacity+1) for row in range(0, n+1)]
   
    #if n == 0 or capacity == 0: # Base case    
        #return 0
    
    #elif items[n-1].weight > capacity:  # Item too heavy to fit?
        #return max_value(items, capacity, n-1, cache)
    #else:
        #item = items[n-1]
        #if cache[n][capacity] == -1:
            #take = item.value + max_value(items, capacity - item.weight, n-1, cache)
            #cache[n][capacity] = max(max_value(items, capacity, n-1, cache), take)
        
        ## Try both with and without the last item. Return the best of the two outcomes.
        #return cache[n][capacity]

