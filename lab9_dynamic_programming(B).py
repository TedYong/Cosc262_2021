###Question 1###

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
        
#def max_value(items, capacity):
    #n_items = len(items)
    #caps = capacity
    #cache = [[0 for i in range(caps+1)] for j in range(n_items)]
    #for j in range(n_items):
        #for i in range(caps + 1):
            #if items[j].weight <= i:
                #new_value = cache[j-1][i-items[j].weight] + items[j].value
                #cache[j][i] = max(cache[j-1][i], new_value)
            #else:
                #cache[j][i] = cache[j - 1][i] 
    
    #x = len(items)-1
    #y = capacity
    #result=[]
    #while x >= 0 and y > 0:
    	#if x == 0 and cache[x][y] != 0:
    	    #result.append(items[x])
    	#elif cache[x][y] != cache[x-1][y]:
    	    #result.append(items[x])
    	    #y-=items[x].weight
    	#x-=1	    
    #return cache[-1][-1], result
    

#items = [Item(45, 3),
         #Item(45, 3),
         #Item(80, 4),
         #Item(80, 5),
         #Item(100, 8)]
#print(max_value(items, 10)) 

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
        
        
s1 = "abcde"
s2 = "qbxxd"
lcs = lcs(s1, s2)
print(lcs)

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
    #table = [[0] * (capacity + 1) for _ in range(len(items))]
    #for item in range(len(items)):
        #for i in range(capacity+1):
            #if items[item].weight <= i:
                #table[item][i] = max(table[item-1][i-items[item].weight] + items[item].value, table[item-1][i])
            #else:
                #table[item][i] = table[item-1][i]
    #i = len(items) - 1
    #j = capacity
    ##for v in table:
     ##   print(v)
    #alist = []
    #while i >= 0 and j > 0:
        #if i == 0 and table[i][j] != 0:
            #alist.append((items[i]))
        #elif table[i][j] != table[i - 1][j]:
            #alist.append(items[i])
            #j -= items[i].weight
        #i -= 1
    #return table[-1][-1], alist
#items = [Item(45, 3),
         #Item(45, 3),
         #Item(80, 4),
         #Item(80, 5),
         #Item(100, 8)]
#maximum, selected_items = max_value(items, 10)
#print(maximum, selected_items)