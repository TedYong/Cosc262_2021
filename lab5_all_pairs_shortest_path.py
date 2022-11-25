#from math import inf

def adjacency_list(graph_str):
    """this one is a bit tough, let's drill in"""
    realg = graph_str.splitlines()
    if len(realg) == 0:
        return []
    elif len(realg) == 1:
        label = realg[0].split()
        result = [[]] * int(label[1])
        return result
    else:
        label = realg[0].split()
        result = [[]] * int(label[1])
        table= []
        j = 0
        l = 0
        for i in realg[1:]:
            table.append(i.split())
        if label[0] == "D":
            if len(label) == 2:   
                while j <= len(result):
                    for k in range(len(table)):
                        if str(j) == table[k][0]:
                            result[j] = result[j] + [(int(table[k][1]), None)]
                    j+=1
                return result
            else:
                while j <= len(result):
                    for k in range(len(table)):
                        if str(j) == table[k][0]:
                            result[j] = result[j] + [(int(table[k][1]), int(table[k][2]))]
                    j+=1
                return result 
        elif label[0] == "U":
            if len(label) == 2:
                while l <= len(result):
                    for h in range(len(table)):
                        if str(l) == table[h][0]:
                            result[l] = result[l] + [(int(table[h][1]), None)]
                        elif str(l) == table[h][1]:
                            result[l] = result[l] + [(int(table[h][0]), None)]                
                    l+=1
                return result  
            else:
                while l <= len(result):
                    for h in range(len(table)):
                        if str(l) == table[h][0]:
                            result[l] = result[l] + [(int(table[h][1]), int(table[h][2]))]
                        elif str(l) == table[h][1]:
                            result[l] = result[l] + [(int(table[h][0]), int(table[h][2]))]                
                    l+=1
                return result  

def distance_matrix(adj_list):
    """this one must conform Floyd's algorithm"""
    length = len(adj_list)
    result = [[float('inf') for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            if i == j:
                result[i][j] = 0
    for k in range(length):
        for l in adj_list[k]:
            index = l[0]
            weight = l[1]
            result[k][index] = weight
    return result

###Great exmaple of this question form Mr Zahid###
#def distance_matrix(adj_list) :
    #result = [[float('inf') for _ in range(len(adj_list))] for _ in range(len(adj_list))]
    
    #for i in range(len(adj_list)):
        #for j in range(len(adj_list)):
            #if i == j:
                #result[i][j] = 0
            #if j < len(adj_list[i]):
                #result[i][adj_list[i][j][0]] = adj_list[i][j][1]
                
    #return result
#graph_str = """\
#U 3 W
#0 1 5
#2 1 7
#"""

#adj_list = adjacency_list(graph_str) 
#print(distance_matrix(adj_list))

#print("\nEach row on a new line:")
#print("\n".join(str(lst) for lst in distance_matrix(adj_list)))

#graph_str = """\
#D 2 W
#0 1 4
#"""

#adj_list = adjacency_list(graph_str)
#print(distance_matrix(adj_list))

def floyd(distance):
    """this shit is super complex to crack up at the begining but I'm glad I made it"""
    numv = len(distance)
    for k in range(numv):
        for i in range(numv):
            for j in range(numv):
                if distance[i][j] > (distance[i][k] + distance[k][j]):
                    distance[i][j] = (distance[i][k] + distance[k][j])
    return distance
#graph_str = """\
#D 3 W
#0 1 1
#1 2 2
#2 0 4
#"""

#adj_list = adjacency_list(graph_str)
#dist_matrix = distance_matrix(adj_list)
#print("Initial distance matrix:", dist_matrix)
#dist_matrix = floyd(dist_matrix)
#print("Shortest path distances:", dist_matrix)

import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))

###now we have come to backtracking section###

#def permutations(s):
    #solutions = []
    #dfs_backtrack((), s, solutions)
    #return solutions


#def dfs_backtrack(candidate, input_data, output_data):
    #if should_prune(candidate):
        #return
    #if is_solution(candidate, input_data):
        #add_to_output(candidate, output_data)
    #else:
        #for child_candidate in children(candidate, input_data):
            #dfs_backtrack(child_candidate, input_data, output_data)

    
#def add_to_output(candidate, output_data):
    #output_data.append(candidate)

    
#def should_prune(candidate):
    #return False

####as for this question, we only need to fill up two blank functions to make permutaton work###

#def is_solution(candidate, input_data):
    #"""Returns True if the candidate is complete solution"""
    #if len(candidate) == len(input_data):
        #return True


#def children(candidate, input_data):
    #"""Returns a collestion of candidates that are the children of the given
    #candidate."""
    #can = list(candidate)
    #inp = list(input_data).copy()
    #if len(can) != 0:
        #for i in can:
            #inp.remove(i)
    #result = [can for i in range(len(inp))]
    #for i in range(len(inp)):
        #result[i] = can + [inp[i]]
        #result[i] = tuple(result[i])
    #return result
        

#print(sorted(permutations({1,2,3})))  
#print(sorted(permutations({'a'})))
#perms = permutations(set())
#print(len(perms) == 0 or list(perms) == [()])

###question 5###

#def all_paths(adj_list, source, destination):
    #solutions = []
    #dfs_backtrack((source, ), adj_list, destination, solutions)
    #return solutions

#def dfs_backtrack(candidate_path, adj_list, destination, output_data):
    #if should_prune(candidate_path):
        #return
    #if is_solution(candidate_path, destination):
        #add_to_output(candidate_path, output_data)
    #else:
        #for child_candidate in children(candidate_path, adj_list):
            #dfs_backtrack(child_candidate, adj_list, destination, output_data)

    
#def add_to_output(candidate, output_data):
    #output_data.append(candidate)

#def should_prune(candidate):
    #if len(candidate) != 0:
        #can = list(candidate)
        #current = can[-1]
        #return candidate.count(current) > 1 
    #else:
        #return False

#def is_solution(candidate_path, destination):
    #"""Returns True if the candidate is complete solution"""
    #can = list(candidate_path)
    ##if candidate_path.count(destination) == 1:
    #if can[-1] == destination:
        #return True


#def children(candidate_path, adj_list):
    #"""Returns a collestion of candidates that are the children of the given
    #candidate."""
    #can = list(candidate_path)
    #inp = list(adj_list)
    #current = can[-1]
    #step = inp[current]
    #possible_step = []
    #result = []
    #if len(step) != 0:
        #for i in step:
            #possible_step.append(i[0])
        
        #if len(possible_step) != 0:
            #result = [can for i in range(len(possible_step))]
            #for k in range(len(possible_step)):
                #result[k] = can + [possible_step[k]]
                #result[k] = tuple(result[k])
        #else:
            #result = [tuple(can)]
    #else:
        #result = []
    #return result
###Zahid Khan's contribution, bravo!!###
#def children(candidate, input_data):
    #"""Returns a collestion of candidates that are the children of the given candidate."""
    #candidate = list(candidate)
    #copy_input = list(input_data).copy()
    #result = []

    #for num in (input_data[candidate[-1]]):
        #result.append(tuple(candidate + [num[0]]))
    
    #return result 
            
#triangle_graph_str = """\
#U 3
#0 1
#1 2
#2 0
#"""

#adj_list = adjacency_list(triangle_graph_str)
#print(sorted(all_paths(adj_list, 0, 2)))
#print(all_paths(adj_list, 1, 1))

#graph_str = """\
#U 5
#0 2
#1 2
#3 2
#4 2
#1 4
#"""

#adj_list = adjacency_list(graph_str)
#print(sorted(all_paths(adj_list, 0, 1)))

#from pprint import pprint

## graph used in tracing bfs and dfs
#graph_str = """\
#D 7
#6 0
#6 5
#0 1
#0 2
#1 2
#1 3
#2 4
#2 5
#4 3
#5 4
#"""

#adj_list = adjacency_list(graph_str)
#pprint(sorted(all_paths(adj_list, 6, 3)))

#from pprint import pprint

#graph_str = """\
#D 4
#0 1
#1 2
#0 3
#3 2
#"""

#adj_list = adjacency_list(graph_str)
#pprint(sorted(all_paths(adj_list, 0, 2)))
#pprint(sorted(all_paths(adj_list, 1, 2)))
#pprint(sorted(all_paths(adj_list, 3, 2)))
#pprint(sorted(all_paths(adj_list, 2, 0)))



###This Lab can stop here basically, but we have one more challenging question worth zero mark###

###Feel free to challenge yourself if you wish###

#import copy

#def latin_squares(square):
    #"""Given a square (matrix) computes and returns Latin squares
    #that can be obtained by replacing Nones with digits."""
    #solutions = []
    #dfs_backtrack(square, solutions)
    #return solutions


#def dfs_backtrack(candidate, output_data):
    #if should_prune(candidate):
        #return
    #if is_solution(candidate):
        #add_to_output(candidate, output_data)
    #else:
        #for child_candidate in children(candidate):
            #dfs_backtrack(child_candidate, output_data)

    
#def add_to_output(candidate, output_data):
    #output_data.append(copy.deepcopy(candidate))


#def square_from_str(square_str):
    #"""Takes a string representation of a square and returns a matrix                                                                                                              
    #(list of lists) representation where blanks are replaced with None."""
    #return [[None if c == '-' else int(c) for c in line.strip()] for
            #line in square_str.splitlines()]


#def square_to_str(square):
    #"""Returns the string representation of the given square matrix."""
    #return '\n'.join(''.join(str(c) for c in row) for row in square)