###This file is about solutions of 262 assignment 1 in 2021###

###Some functions here is extracted from previous labs###

###adjacency_list is from lab3###
#def adjacency_list(graph_str):
    #"""this one is a bit tough, let's drill in"""
    #realg = graph_str.splitlines()
    #if len(realg) == 0:
        #return []
    #elif len(realg) == 1:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #return result
    #else:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #table= []
        #j = 0
        #l = 0
        #for i in realg[1:]:
            #table.append(i.split())
        #if label[0] == "D":
            #if len(label) == 2:   
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), None)]
                    #j+=1
                #return result
            #else:
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), int(table[k][2]))]
                    #j+=1
                #return result 
        #elif label[0] == "U":
            #if len(label) == 2:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), None)]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), None)]                
                    #l+=1
                #return result  
            #else:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), int(table[h][2]))]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), int(table[h][2]))]                
                    #l+=1
                #return result  
###Question 1###
#def format_sequence(converters_info, source_format, destination_format):
    #realg = converters_info.splitlines()
    #result = []
    #if len(realg) == 0:
        #result = []
    #elif len(realg) == 1:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
    #else:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #table= []
        #j = 0
        #l = 0
        #for i in realg[1:]:
            #table.append(i.split())
        #if label[0] == "D":
            #if len(label) == 2:   
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), None)]
                    #j+=1
            #else:
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), int(table[k][2]))]
                    #j+=1
        #elif label[0] == "U":
            #if len(label) == 2:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), None)]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), None)]                
                    #l+=1
            #else:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), int(table[h][2]))]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), int(table[h][2]))]                
                    #l+=1    
    #solutions = []
    #final_result = []
    #dfs_backtrack((source_format, ), result, destination_format, solutions)
    #if len(solutions) == 0:
        #return "No solution!"
    #else:
        #for i in solutions:
            #final_result.append(list(i))
        #smallest = final_result[0]
        #for j in final_result:
            #if len(smallest) > len(j):
                #smallest = j
        #return smallest

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



#converters_info_str = """\
#D 2
#0 1
#"""

#print(format_sequence(converters_info_str, 0, 1))
#converters_info_str = """\
#D 2
#0 1
#"""

#print(format_sequence(converters_info_str, 1, 1))

#converters_info_str = """\
#D 2
#0 1
#"""

#print(format_sequence(converters_info_str, 1, 0))

#converters_info_str = """\
#D 5
#1 0
#0 2
#2 3
#1 2
#"""

#print(format_sequence(converters_info_str, 1, 2))

#converters_info_str = """\
#D 1
#"""

#print(format_sequence(converters_info_str, 0, 0))

###Question2###
#def bubbles(physical_contact_info):
    #"""a varied version of original adjcency list"""
    #reali = physical_contact_info.splitlines()
    #result = []
    #if len(reali) == 0:
        #return []
    #if len(reali) == 1:
        #label = reali[0].split()
        #for i in range(int(label[1])):
            #result.append([i])
        #return result
    #else:
        #result = []
        #table = []
        #label = reali[0].split()
        #for j in reali[1:]:
            #table.append(j.split())
        #real_table = [[] for i in range(len(table))]
        #for x in range(len(real_table)):
            #for y in table[x]:
                #real_table[x].append(int(y))
        #real_table = sorted(real_table)
        #i = 0
        #while i < len(real_table):
            #for k in real_table[i+1:]:
                #if k[0] in real_table[i] and k[1] in real_table[i]:
                    #real_table.remove(k)
                #elif k[0] in real_table[i]:
                    #real_table[i].append(k[1])
                    #real_table.remove(k)
                #elif k[1] in real_table[i]:
                    #real_table[i].append(k[0])   
                    #real_table.remove(k)

            #i+=1
        
        #tester = []
        #for a in real_table:
            #for b in a:
                #tester.append(b)
        #for c in range(int(label[1])):
            #if c not in tester:
                #real_table.append([c])
        #return real_table

###honorable mention from Zahid### 
#def adjacency_list(graph_str):
    #graph_text = graph_str.splitlines()
    
    #num_of_lists = graph_text[0].split()
    #matrix = [[] for _ in range(int(num_of_lists[1]))]
    
    #if graph_text[0][0] == "D":
        #for i in range(1, len(graph_text)):
            #line = graph_text[i].split()
            #if len(line) == 3:
                #weight = int(line[2])
            #else:
                #weight = None
            #matrix[int(line[0])].append((int(line[1]), weight))
    #else:
        #for i in range(1, len(graph_text)):
            #line = graph_text[i].split()
            ##print(line)
            #if len(line) == 3:
                #weight = int(line[2])
            #else:
                #weight = None            
            #matrix[int(line[0])].append((int(line[1]), weight))
            #matrix[int(line[1])].append((int(line[0]), weight))
    
    #return matrix

#def bubbles(physical_contact_info):
    #test_result = adjacency_list(physical_contact_info)
    #result = dfs_tree(test_result)
    #return result
    
#def dfs_tree(adj_list):
    #length = len(adj_list)
    #states = ["U" for _ in range(length)]
    #parents = [None for _ in range(length)]
    
    #result = []
    #while 'U' in states:
        #sub_list = []
        #start = states.index("U")
        #states[start] = "D"        
        #dfs_loop(adj_list, start, states, parents)
        ##print(states)
        #for i in range(len(states)):
            #if states[i] in {'P', "D"}:
                #sub_list += [i]
                #states[i] = 'F'
        #result.append(sub_list)
    #return result

#def dfs_loop(adj_list, index, states, parents):
    #for col_index in adj_list[index]:
        #if states[col_index[0]] == "U":
            #states[col_index[0]] = "D"
            #parents[col_index[0]] = index
            #dfs_loop(adj_list, col_index[0], states, parents)
        #states[index] = "P"

###Question3###

def build_order(dependencies):
    """this is adopted from q2"""
    reald = dependencies.splitlines()
    result = []
    if len(reald) == 0:
        return []
    if len(reald) == 1:
        label = reald[0].split()
        for i in range(int(label[1])):
            result.append(i)
        return result  
    else:
        result = []
        table = []
        label = reald[0].split()
        for j in reald[1:]:
            table.append(j.split())
        real_table = [[] for i in range(len(table))]
        for x in range(len(real_table)):
            for y in table[x]:
                real_table[x].append(int(y))
        #real_table = sorted(real_table)   
        final_result = real_table[0]
        for y in real_table[1:]:
            if y[0] not in final_result and y[1] not in final_result:
                for g in y:
                    final_result.append(g)
            if y[0] in final_result and y[1] not in final_result:
                #num = final_result.index(y[0])
                #if num == len(final_result)-1:
                final_result.append(y[1])
                #else:
                    #final_result.insert(num, y[1])
            if y[0] not in final_result and y[1] in final_result:
                num = final_result.index(y[1])
                final_result.insert(num, y[0])            
            if y[0] in final_result and y[1] in final_result:
                num1 = final_result.index(y[0])
                num2 = final_result.index(y[1])
                if num1 > num2:
                    #final_result[num1] = y[1]
                    #final_result[num2] = y[0]
                    final_result.remove(y[0])
                    final_result.insert(num2, y[0])
            for z in real_table:
                if z[0] in final_result and z[1] in final_result:
                    num3 = final_result.index(z[0])
                    num4 = final_result.index(z[1])
                    if num3 > num4:
                        #final_result[num1] = y[1]
                        #final_result[num2] = y[0]
                        final_result.remove(z[0])
                        final_result.insert(num4, z[0])                
            tester = []
            for a in final_result:
                tester.append(a)
            for c in range(int(label[1])):
                if c not in tester:
                    final_result.append(c)
        return final_result      

###Question4###
###failed attempts###
#from itertools import combinations
#def which_segments(city_map):
    #"""another version of adjacency list function"""
    #realc = city_map.splitlines()
    #if len(realc) == 1:
        #return []
    #elif len(realc) == 2:
        #return [(0, 1)]
    #else:
        #result = []
        #table = []
        #label = realc[0].split()
        #for j in realc[1:]:
            #table.append(j.split())
        #real_table = []
        #for i in table:
            #if int(i[0]) > int(i[1]):
                #real_table.append([(int(i[1]), int(i[0])), int(i[2])])
            #else:
                #real_table.append([(int(i[0]), int(i[1])), int(i[2])])
        #comb_table = []
        #for k in range(int(label[1])):
            #comb_table.append(k)
        #comb = combinations(comb_table, int(label[1])-1)
        #dup = list(comb).copy()
        #path_table = []
        #tester = []
        #for h in dup:
            #total = 0
            #test = []
            #for g in h:
                #test.append(real_table[g][0])
                #total += real_table[g][1] 
            #path_table.append(total)
            #tester.append(test)
        #true_tester=tester.copy()
        #for a in range(len(tester)):
            #te = []
            #for b in tester[a]:
                #te += b
            #for c in range(int(label[1])):
                #if c not in te:
                    #true_tester.remove(tester[a])
                    #path_table.remove(path_table[a])
                    
        #num = min(path_table)
        #ind = path_table.index(num)
        #true_result = []
        #for f in dup[ind]:
            #true_result.append(real_table[f][0])
        #return true_result

###second try###  
#def adjacency_list(graph_str):
    #"""this one is a bit tough, let's drill in"""
    #realg = graph_str.splitlines()
    #if len(realg) == 0:
        #return []
    #elif len(realg) == 1:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #return result
    #else:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #table= []
        #j = 0
        #l = 0
        #for i in realg[1:]:
            #table.append(i.split())
        #if label[0] == "D":
            #if len(label) == 2:   
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), None)]
                    #j+=1
                #return result
            #else:
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), int(table[k][2]))]
                    #j+=1
                #return result 
        #elif label[0] == "U":
            #if len(label) == 2:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), None)]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), None)]                
                    #l+=1
                #return result  
            #else:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), int(table[h][2]))]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), int(table[h][2]))]                
                    #l+=1
                #return result  
#def next_vertex(in_tree, distance):
    #"""this actually takes me a whole week, time to settle this"""
    #result = 0
    #lists = []
    #index = []
    #haha = 0
    #for i in range(len(in_tree)):
        #if in_tree[i] == True:
            #result = distance[i]
        #else:
            #lists.append(distance[i])
            #index.append(i)
            #haha = i
    #dis = min(lists)
    #if type(dis) == float:
        #return haha
    #else:
        #for j in range(len(lists)):
            #if dis == lists[j]:
                #return index[j]
#def which_segments(city_map):
    #adj = adjacency_list(city_map)
    #result = []
    #for i in range(len(adj)):
        #result.append(prims(adj, i))
    #mid_result = []
    #for j in result:
        #if sorted(j) not in mid_result:
            #mid_result.append(sorted(j))
    
    #tester = [True for i in range(len(mid_result))]
    #for k in range(len(mid_result)):
        #for l in mid_result[k]:
            #if mid_result[k].count(l) > 1:
                #tester[k] = False
    #final = []
    #for g in range(len(tester)):
        #if tester[g] is True:
            #final = mid_result[g]
    #return final
#def prims(adj_list, start):
    #"""a simple replica"""
    #numv = len(adj_list)
    #in_tree = [False for i in range(numv)]
    #distance = [float('inf') for i in range(numv)]    
    #parent = [None for i in range(numv)]
    #distance[start] = 0
    #while False in in_tree:
        #u = next_vertex(in_tree, distance)
        #in_tree[u] = True
        #for v, weight in adj_list[u]:
            #if in_tree[v] + weight < distance[v]:
                #distance[v] = weight
                #parent[v] = u
        #final_result = []
        #for i in range(len(parent)):
            #if parent[i] != None:
                #if parent[i] < i:
                    #final_result.append((parent[i], i))
                #else:
                    #final_result.append((i, parent[i]))
    #return final_result
###Third attempt###
    
#def adjacency_list(graph_str):
    #"""this one is a bit tough, let's drill in"""
    #realg = graph_str.splitlines()
    #if len(realg) == 0:
        #return []
    #elif len(realg) == 1:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #return result
    #else:
        #label = realg[0].split()
        #result = [[]] * int(label[1])
        #table= []
        #j = 0
        #l = 0
        #for i in realg[1:]:
            #table.append(i.split())
        #if label[0] == "D":
            #if len(label) == 2:   
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), None)]
                    #j+=1
                #return result
            #else:
                #while j <= len(result):
                    #for k in range(len(table)):
                        #if str(j) == table[k][0]:
                            #result[j] = result[j] + [(int(table[k][1]), int(table[k][2]))]
                    #j+=1
                #return result 
        #elif label[0] == "U":
            #if len(label) == 2:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), None)]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), None)]                
                    #l+=1
                #return result  
            #else:
                #while l <= len(result):
                    #for h in range(len(table)):
                        #if str(l) == table[h][0]:
                            #result[l] = result[l] + [(int(table[h][1]), int(table[h][2]))]
                        #elif str(l) == table[h][1]:
                            #result[l] = result[l] + [(int(table[h][0]), int(table[h][2]))]                
                    #l+=1
                #return result  
#def next_vertex(in_tree, distance):
    #"""this actually takes me a whole week, time to settle this"""
    #result = 0
    #lists = []
    #index = []
    #haha = 0
    #for i in range(len(in_tree)):
        #if in_tree[i] == True:
            #result = distance[i]
        #else:
            #lists.append(distance[i])
            #index.append(i)
            #haha = i
    #dis = min(lists)
    #if type(dis) == float:
        #return haha
    #else:
        #for j in range(len(lists)):
            #if dis == lists[j]:
                #return index[j]
#def which_segments(city_map):
    #adj = adjacency_list(city_map)
    #result = []
    #for i in range(len(adj)):
        #result.append(prims(adj, i))
    #mid_result = []
    #for j in result:
        #if sorted(j) not in mid_result:
            #mid_result.append(sorted(j))
    #k = 0
    #while k < len(mid_result):
        #for l in mid_result[k]:
            #if mid_result[k].count(l) != 1:
                #mid_result.remove(mid_result[k])
                #break
        #k+=1                  
    #return mid_result[0]

#def prims(adj_list, start):
    #"""a simple replica"""
    #numv = len(adj_list)
    #in_tree = [False for i in range(numv)]
    #distance = [float('inf') for i in range(numv)]    
    #parent = [None for i in range(numv)]
    #distance[start] = 0
    #while False in in_tree:
        #u = next_vertex(in_tree, distance)
        #in_tree[u] = True
        #for v, weight in adj_list[u]:
            #if not in_tree[v] and weight < distance[v]:
                #distance[v] = weight
                #parent[v] = u
        #final_result = []
        #for i in range(len(parent)):
            #if parent[i] != None:
                #if parent[i] < i:
                    #final_result.append((parent[i], i))
                #else:
                    #final_result.append((i, parent[i]))
    #return final_result   

#city_map = """\
#U 6 W
#2 0 1
#1 2 3
#0 1 2
#2 3 4
#5 2 7
#3 4 5
#4 5 6
#"""

#print(sorted(which_segments(city_map)))

#city_map = """\
#U 4 W
#0 1 5
#1 3 5
#3 2 5
#2 0 5
#0 3 2
#1 2 1
#"""

#answer = which_segments(city_map)
#print(answer)
#print(len(answer))
#print((0, 3) in answer)
#print((1, 2) in answer)
#print(any(walkway in answer for walkway in {(0, 1), (0, 2), (1, 3), (2, 3)}))



###Question5###
#from math import inf
#def adjacency_list(graph_str):
    #graph_text = graph_str.splitlines()
    
    #num_of_lists = graph_text[0].split()
    #matrix = [[] for _ in range(int(num_of_lists[1]))]
    
    #if graph_text[0][0] == "D":
        #for i in range(1, len(graph_text)):
            #line = graph_text[i].split()
            #if len(line) == 3:
                #weight = int(line[2])
            #else:
                #weight = None
            #matrix[int(line[0])].append((int(line[1]), weight))
    #else:
        #for i in range(1, len(graph_text)):
            #line = graph_text[i].split()
            ##print(line)
            #if len(line) == 3:
                #weight = int(line[2])
            #else:
                #weight = None            
            #matrix[int(line[0])].append((int(line[1]), weight))
            #matrix[int(line[1])].append((int(line[0]), weight))
    
    #return matrix
#def next_vertex(in_tree, distance):
    #"""this actually takes me a whole week, time to settle this"""
    #result = 0
    #lists = []
    #index = []
    #haha = 0
    #for i in range(len(in_tree)):
        #if in_tree[i] == True:
            #result = distance[i]
        #else:
            #lists.append(distance[i])
            #index.append(i)
            #haha = i
    #dis = min(lists)
    #if type(dis) == float:
        #return haha
    #else:
        #for j in range(len(lists)):
            #if dis == lists[j]:
                #return index[j]
#def dijkstra(adj_list, start):
    #"""last one, good to go"""
    #numv = len(adj_list)
    #in_tree = [False for i in range(numv)]
    #distance = [float('inf') for i in range(numv)]
    #parent = [None for i in range(numv)]
    #distance[start] = 0
    #while False in in_tree:
        #u = next_vertex(in_tree, distance)
        #in_tree[u] = True
        #for v, weight in adj_list[u]:
            #if not in_tree[v] and distance[u] + weight < distance[v]:
                #distance[v] = distance[u] + weight
                #parent[v] = u
    #return parent, distance
#def min_capacity(city_map, depot_position):
    #city_map2 = adjacency_list(city_map)
    #distance = dijkstra(city_map2, depot_position)[1]
    #for i in range(len(distance)):
        #if distance[i] == float("inf"):
            #distance[i] = 0
    #dist = max(distance)
    #dist2 = dist * 2 * 3 * 6
    #battery = (dist2 * 100) // 80
    #return battery
    
    
#city_map = """\
#U 4 W
#0 2 5
#0 3 2
#3 2 2
#"""

#print(min_capacity(city_map, 0))
#print(min_capacity(city_map, 1))
#print(min_capacity(city_map, 2))
#print(min_capacity(city_map, 3))
###Mohadisa's code for question 5, great help and reference### 
#from math import inf
#def adjacency_list(graph_string):
    #"""It takes the converters_info which is in string and change it to an adjacency list."""
    #lines = graph_string.splitlines()
    #description = lines.pop(0).split(" ")
    #directed = False
    #weighted = False
    
    #number_of_nodes = int(description[1])  
    #if description[0] == "D":
        #directed = True
     

    #if len(description) == 3:
        #weighted = True
    
    #graph_list = []
    #for line in lines:
        #line = line.split(" ")
        #for i in range(len(line)):
            #line[i] = int(line[i])
        #graph_list.append(line)
    
    #adj_list = [[] for i in range(number_of_nodes)]
    #if not weighted:  
        #for i, j in graph_list:
            #if directed:
                #adj_list[i].append((j, None))
            #else:
                #adj_list[i].append((j, None))
                #adj_list[j].append((i, None))
    #else:
        #for i, j, k in graph_list:
            #if directed:
                #adj_list[i].append((j, k))
            #else:
                #adj_list[i].append((j , k))
                #adj_list[j].append((i, k))
    
    #return adj_list

#def min_capacity(city_map, depot_position):
    #"""battery unit is multiplied by two because electric car comes back to depot for each travel
        #it is multiplies by 3 because each distance unit is equivalent to 3 units of battery
        #and multiplied by 6 because the car should be able to travel 6 times before charging
        #battery unit is initially 80 percent so we need to change it to 100 percent 
        #min_battery_for_6_travel is the mimimum battery percentage the car needs to travel all cities 
        #for 6 times 
        #"""
    #adj_list = adjacency_list(city_map)
    #distance = dijkstra(adj_list, depot_position)
    #for i in range(len(distance)):
        #if distance[i] == float("inf"):
            #distance[i] = 0
    #minimum_dis = max(distance)
    #battery_unit = minimum_dis * 2 * 3 * 6 
    #min_battery_for_6_travel = (battery_unit * 100)//80
    #return min_battery_for_6_travel

#def dijkstra(adj, s):
    #"""electric car should travel cities with minimum cost (distance) so we are using dijkstra algorithm 
    #to find the shortest paths from depot"""
    #n = len(adj)
    #in_tree = [False for _ in range(n)]
    #distance = [float("inf") for _ in range(n)]
    #parent = [None for _ in range(n)]
    #distance[s] = 0
    #while False in in_tree:
        #u = next_vertex(in_tree, distance)
        #in_tree[u] = True
        #for v, weight in adj[u]:
            #if not in_tree[v] and distance[u] + weight < distance[v]:
                #distance[v] = distance[u] + weight
                #parent[v] = u 
    #return distance 

#def next_vertex(in_tree, distance):
    #"""finds the next path to the next city"""
    #minimum = float("inf")
    #for i in range(len(distance)):
        #if distance[i] <= minimum and in_tree[i] == False:
            #minimum = distance[i]
            #min_index = i
    #return min_index
