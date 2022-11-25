# First and foremost, we have a look at our classic and simple iterative function
# to create a basic example for recursion and get a better understanding of it 

# Here is our example:
#def sum(data):
    #result = 0
    #for i in data:
        #result += i
    #return result

#Ted_iterative = [1,1,1]
#print(sum(Ted_iterative))

#And next we converse it in recursive way

#That's our first attempt:
#def recursive_sum1(data):
    #if len(data) == 0:
        #return 0
    #else:
        #return data[len(data)-1] + sum(data[:(len(data)-1)])

#Ted_recursive = [1,1,1]
#print(recursive_sum1(Ted_recursive))

#Similiarly we can also do this:
#def recursive_sum2(data):
    #if len(data) == 0:
        #return 0
    #else:
        #return data[0] + sum(data[1:])

#Ted_recursive = [1,1,1]
#print(recursive_sum2(Ted_recursive))

#Finally I changed a bit about first try and here's my version to do recursive:)

#I am glad it worked:
#def recursive_sum3(data):
    #if len(data) == 0:
        #return 0
    #else:
        #return data.pop() + sum(data)

#Ted_recursive = [1,1,1]
#print(recursive_sum3(Ted_recursive))

# it carried out great but codes are not as formally concise and succinct as pros
# Let's fix that then:

#def recursive_finalsum(data):
    #return 0 if len(data) == 0 else data.pop() + recursive_finalsum(data)

#Ted_recursive = [1,1,1]
#print(recursive_finalsum(Ted_recursive))

# it looks better now, and thus the warm-up is over, we can get down to study 
# something cooler. If you like to organize and categorize your schedule and 
# study, I have a good news for you: we will apply a standard Divide and Conquer 
# pattern to manage our code to improve the quality of programming, right down 
# below is an example and you will understand once you look through it

#def recursive_func(strings_params):
    #if is_trivial_case(input_params): # Is it the base case?
        #return trivial_solution(input_params)
    #else:
        #subproblem1, subproblem2 = subdivide_problem(input_params)
        #soln1 = recursive_func(subproblem1)
        #soln2 = recursive_func(subproblem2)
        #return combined_soln(soln1, soln2)

# utill this moment, you prolly know this is not finished yet, nonethless it 
# still explains itself by showing you the separation between trival and 
# significant part of function

#"The subdivision in the above problem was into the first element and the rest. The sum of a single element - referred so as the base case is trivial so we didn't bother recursing on the first bit, only on the rest."

#"It turns out that the above implementation has quadratic complexity because evaluating data[1:] involves copying the entire list. We can improve the efficiency (to linear time) by instead writing the recursive code as below."

#Now it's about time we start our lab quiz:

#Part B:
#Question 1:
#Write a function concat_list(strings) that takes a list of strings as a parameter and returns a single string made up of all the individual strings in strings concatenated together, in order. Your implementation must not use loops, the 'join' method of a string, or any imports. Also (and this applies to all questions in this quiz unless otherwise specified) it shouldn't use list comprehensions as they are loops (or recursions) in disguise, which do all the work for you!


#def concat_list(strings):
    #result = ""
    #if len(strings) == 0:
        #return result
    #else:
        #result = strings[0] + concat_list(strings[1:])
        #return result
#ans = concat_list(['a', 'hot', 'day'])
#print(ans)
#ans = concat_list(['x', 'y', 'z'])
#print(ans)
#print(concat_list([]))

#Question 2:
#Write a function product(data) that returns the product of the elements in the list data, or 1 if the list is empty. Your code must not use for or while, must not import anything and must be pylint compliant except that docstrings are optional.
#def product(data):
    #if len(data) == 0 :
        #return 1
    #else:
        #return data.pop() * product(data)
#print(product([1, 13, 9, -11]))
#print(product([]))

#Question 3:
#Write a function backwards(s) that returns its parameter string s in reverse. Obviously you're not allowed to call the reverse method of the string nor the reversed function. 
#You also cannot use loops or use imports, and using slices with negative increments is cheating! 

#def backwards(s):
    #result = ""
    #if len(s) == 0:
        #return result
    #else:
        #return s[-1] + backwards(s[:-1])
#print(backwards("Hi there!"))
#print(backwards(""))

#Question 4:
#Write a function odds(data) that takes a list of ints, data, as a parameter and returns a new list that contains just the odd elements from data, i.e. those elements that are not exactly divisible by two. Your code must not use for or while and must not import anything.

#def odds(data):
    #result = []
    #if len(data) == 0:
        #return result
    #else:
        #if data[0]%2 != 0:
            #return [data[0]] + odds(data[1:])
        #else:
            #return odds(data[1:])
#print(odds([0, 1, 12, 13, 14, 9, -11, -20]))

#Question 5:
#Write a function squares(data) that takes a list of ints, data, as a parameter and returns a new list that contains the squares of all the numbers in data. Your code must not use for or while, must not import anything and must be pylint compliant. Also, your function must not alter the list it is given as a parameter. [This is a general programming style rule: never modify the input data you are given unless the function is explicitly specified to do so.]

#def squares(data):
    #result = []
    #if len(data) == 0:
        #return result
    #else:
        #return [data[0]**2] + squares(data[1:])

#print(squares([1, 13, 9, -11]))

#Question 6:
#Write a function find(data, value) that returns the subscript of the first occurrence of value in data, or -1 if the value is not found. Your function cannot use loops or list comprehensions and also cannot use the index method of a list.

#def find(data, value):
    #result = -1
    #total = 0
    #if value not in data:
        #return result
    #else:
        
        #if data[0] != value:
            #total += 1
            #return 1 + find(data[1:], value)
        #else:
            #return 1 + find(data[:total], value)
            
#print(find(["hi", "there", "you", "there"], "there"))
#print(find([10, 20, 30], 0))
#print(find(["hi", "you", "there"], "there"))

#Funk it, I fell asleep in the middle
#nvm, let us proceed

#Part A:
#Question 1:
#pfft didnt notice its an elective question
#same with Question 2

#now move on to our Question 3:
#this part I will write on paper to solve it, and the question itself it too long to put here

#and here we are now, all the way to Question 8
#Write an asymptotically most efficient implementation of the function almost_all(numbers) mentioned above.

#this is the original version which is not asymptotically most efficient implementation of it. 
#def almost_all(numbers): 
    #return [sum(numbers) - x for x in numbers] 
#We gonna change that

#def Ted(alpha):
    #result = []
    #for i in alpha:
        #for j in alpha:
            #result.append(i + j)
    #return result

#print(Ted(["1", "2", "3"]))

#Question11:
#CAUTION: this is not my personal solution, I copied this solution from Zahid Khan,
#so if it's not on deadline, don't use this, you better come up with your own solution

#Zahid's version:
#def sort_of(numbers):
    #result = []
    #if len(numbers) > 0:
        #result.append(numbers[-1])
    #for i in range(len(numbers)-2, -1, -1):
        #if numbers[i] > result[-1]:
            #result.append(result[-1])
        #else:
            #result.append(numbers[i])
    #result.reverse()
    #return result
