###Time to do some work after two weeks break###

###Question 6 and 7###
#import operator
#def key_positions(seq, key):
    #"""this is based on lecture notes
    #thanks to brother Yoseph, he helped me sort this one out"""
    #line1 = []
    #for i in seq:
        #line1.append(key(i))
    #k = max(line1)
    #line2 = [0] * (k+1)
    #for j in seq:
        #line2[key(j)] += 1 
    #total = 0
    #for l in range(0, k+1):
        #line2[l], total = total, line2[l] + total
    #return line2
    
#print(key_positions([0, 1, 2], lambda x: x))
#print(key_positions([2, 1, 0], lambda x: x))
#print(key_positions([1, 2, 3, 2], lambda x: x))
#print(key_positions([5], lambda x: x))
#print(key_positions(range(-3,3), lambda x: x**2))
#print(key_positions(range(1000), lambda x: 4))
#print(key_positions([1] + [0] * 100, lambda x: x))

#def sorted_array(seq, key, positions):
    #"""still a replica"""
    #result = [0] * len(seq)
    #for i in seq:
        #result[positions[key(i)]] = i
        #positions[key(i)] += 1
    #return result
#print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
#print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
#print(sorted_array([100], lambda x: x, [0]*101))
#"""Counting Sort"""

#def counting_sort(iterable, key):
    #positions = key_positions(iterable, key)
    #return sorted_array(iterable, key, positions)
    
#objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

#key = operator.itemgetter(1)
#print(", ".join(object[0] for object in counting_sort(objects, key)))


###Question 8###
#def radix_sort(numbers, d):
    #B = numbers
    #for i in range(d):
        #n = numbers[i] 
        #B = counting_sort(B, lambda n: n//(10**i) % 10)
    #return B
        
    
#print(counting_sort([9,7,7,9,6,0,5], lambda x: x))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))