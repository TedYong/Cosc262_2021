#So here we go again, this is lab 2 quiz at week 2, in this week we gonna revise 
#our recursive implemental skill while learning a concpet named "divide and conquer"
#(*like hell I know what the f*ck is this!), hope this week won't be so tough and 
#we start here


#Question 1:
#For a number n, the Collatz cycle-length of n is the number of numbers generated in the Collatz sequence up to 1 (including n and 1). In the example above, the cycle length of 22 is 16.

#Write a recursive function cycle_length(n) to compute the Collatz cycle-length without any of the following:

#>importing a module
#>using any types of loop (for, while, list comprehension, ...)
#Assume that n will always be an integer greater than or equal to 1.

#def cycle_length(n):
    ##again,we need to do this recursively
    
    #if n == 1:
        #return 1
    #else:
        #if n%2 == 0:
            #return 1 + (cycle_length(n/2))
        #else:
            #return 1 + (cycle_length((3*n)+1))

#Question 2:
#Another excellent practice about understanding recursive function

#Write a recursive function recursive_divide(x, y) to perform integer division without any of the following:

#>importing a module
#>using operators *, / or //
#>using any types of loop (for, while, list comprehension, ...)
#The function must return what x//y would return in Python 3. Assume x >= 0 and y > 0 is true.

#Question 6:
#import sys
#sys.setrecursionlimit(100000)

#def dumbo_func(data, index=0):
    #"""Takes a list of numbers and does weird stuff with it"""
    #if index >= len(data):
        #return 0
    #else:
        #if (data[index] // 100) % 3 != 0:
            #return 1 + dumbo_func(data, index+1)
        #else:
            #return dumbo_func(data, index+1)





#Question 7:
#def all_pairs(list1, list2, i=0):
    #if i >= len(list1):
        #return []
    #else:
        #return help_pairs(list1[i], list2) + all_pairs(list1,list2, i+1)
    
#def help_pairs(i, list2, j=0):
    #if j >= len(list2):
        #return []
    #else:
        #return [(i,list2[j])] + help_pairs(i, list2, j+1)

#print(all_pairs([1, 2], [10, 20, 30]))
    

#def recursive_fib(n):
    #"""another cursed function to create.
    #this is recursive fib function, time 
    #complexity is O(2^n), pretty trash here"""
    #if n <= 1:
        #return n
    #else:
        #return fib(n-1) + fib(n-2)

#def fib(n):
    #"""definitely better than what we did above"""
    #result = [0] * (n + 1)
    #result[0] = 0
    #result[1] = 1
    #for i in range(2, n + 1):
    
        #if i <= n :
            #result[i] = result[i-1] + result[i-2]
            
        #else:
            #break
    #return result[-1]
        

#print(fib(100))

#Question 12:
#first attempt:
#def perms(items, i=0):
    #if items == []:
        #return ([])
    #if i >= len(items):
        #return ([])
    #else:
        #return help_perms(items[i], items) + perms(items, i+1)
#def help_perms(i, items, j=0):
    #if items == []:
        #return ([])
    #if j >= len(items):
        #return ([])
    #else:
        #return ([i, items[j]]) + help_perms(i, items, j+1)
#print(perms([1,2,3]))

#second attempt:

def perms(items):
    result = []
    word = items[0]
    length = len(items)
    return helper_perms(items, word, result, length)

def helper_perms(items, result, length):
    if length == 0:
        return ()
    else:
        for i in range(length):
            result = (items[i], items[(i+1)%length], items[(i+2)%length])
        return result + helper_perms(items, result, length-1)
                                 
print(helper_perms([1,2,3],[],3))

# Fibonacci Series using 
# Optimized Method
 
# function that returns nth 
# Fibonacci number 
#def fib(n):
     
    #F = [[1, 1],
         #[1, 0]]
    #if (n == 0):
        #return 0
    #power(F, n - 1)
         
    #return F[0][0]
     
#def multiply(F, M):
     
    #x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    #y = (F[0][0] * M[0][1] +
         #F[0][1] * M[1][1])
    #z = (F[1][0] * M[0][0] +
         #F[1][1] * M[1][0])
    #w = (F[1][0] * M[0][1] +
         #F[1][1] * M[1][1])
     
    #F[0][0] = x
    #F[0][1] = y
    #F[1][0] = z
    #F[1][1] = w

#def power(F, n):
 
    #if( n == 0 or n == 1):
        #return;
    #M = [[1, 1],
         #[1, 0]];
         
    #power(F, n // 2)
    #multiply(F, F)
         
    #if (n % 2 != 0):
        #multiply(F, M)
     
## Driver Code
#if __name__ == "__main__":
    #n = 7
    #print(fib(n))
 
# This code is contributed 
# by ChitraNayal
#MAX = 1000
#lists = [0] * MAX
#def fib(n) :
    #if (n == 0) :
        #return 0
    #if (n == 1 or n == 2) :
        #lists[n] = 1
        #return (lists[n])
 
    ## If fib(n) is already computed
    #if (lists[n]) :
        #return lists[n]
 
    #if( n & 1) :
        #k = (n + 1) // 2
    #else : 
        #k = n // 2
 
    ## Applying above formula [Note value n&1 is 1
    ## if n is odd, else 0.
    #if((n & 1) ) :
        #f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    #else :
        #f[n] = (2*fib(k-1) + fib(k))*fib(k)
 
    #return f[n]
#print(fib(7))

#MAX = 1000
#lists = [0] * 1000
#def fib(n):
    #if n == 0:
        #return 0
    #if n == 0 or n == 1:
        #lists[n] = 1
        #return lists[n]
    
    #if lists[n]:
        #return lists[n]
    
    #if n%2 == 0:
        #k = n//2
    #else:
        #k = (n + 1)//2
        
    #if n%2 == 0:
        #lists[n] = (2 * fib(k-1) + fib(k)) * fib(k)
    #else:
        #lists[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    #return lists[n]

#print(fib(10**4) % 10**10)