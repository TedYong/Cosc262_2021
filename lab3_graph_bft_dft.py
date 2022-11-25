#from pprint import pprint
#import operator
#from collections import deque

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
        

#graph_string = """\
#U 7
#1 2
#1 5
#1 6
#2 3
#2 5
#3 4
#4 5
#"""
#print(adjacency_list(graph_string))
#pprint(adjacency_list(graph_string))


#def adjacency_matrix(graph_str):
    #"""another one, but this time won't be as hard as last one"""
    #realg = graph_str.splitlines()
    #label = realg[0].split()
    #table = []
    #for i in realg[1:]:
        #table.append(i.split())
    #if label[0] == "D":
        #if len(label) == 2:
            #result2 = [[0 for y in range(int(label[1]))] for x in  range(int(label[1]))]
            #for j in range(len(table)):
                #row = int(table[j][0])
                #column = int(table[j][1])
                #result2[row][column] = 1
            #return result2
        #else:
            #result2 = [[None for y in range(int(label[1]))] for x in  range(int(label[1]))]
            #for j in range(len(table)):
                #row = int(table[j][0])
                #column = int(table[j][1])
                #result2[row][column] = int(table[j][2])
            #return result2
    #elif label[0] == "U":
        #if len(label) == 2:
            #result2 = [[0 for y in range(int(label[1]))] for x in  range(int(label[1]))]
            #for j in range(len(table)):
                #row = int(table[j][0])
                #column = int(table[j][1])
                #result2[row][column] = 1
                #result2[column][row] = 1
            #return result2  
        #else:
            #result2 = [[None for y in range(int(label[1]))] for x in  range(int(label[1]))]
            #for j in range(len(table)):
                #row = int(table[j][0])
                #column = int(table[j][1])
                #result2[row][column] = int(table[j][2])
                #result2[column][row] = int(table[j][2])
            #return result2                    
        
                    
        
    
##graph_string = """\
##D 3 W
##0 1 55
##1 0 56
##0 2 57
##"""

##print(adjacency_matrix(graph_string))

#from pprint import pprint

#graph_string = """\
#U 17
#1 2
#1 15
#1 6
#12 13
#2 15
#13 4
#4 5
#"""
#pprint(adjacency_matrix(graph_string))




#thanks to Zahid Khan, this question is finally over. here is his incompleted contribution.
#def ZK_adjacency_matrix(graph_str):
    
    #graph_ln = graph_str.splitlines()
    
    #for line in graph_ln:
        #if line[0] in {"U", "D"}:
            #matrix = [[0] * int(line[2])] * int(line[2])
            ##matrix = [[[0] * int(line[2])] * int(line[2]) for i in range(len(line)) if i == 2]
        #else:
            #row = int(line[0])
            #col = int(line[2])
            #matrix[row][col] = 1
        #print('A')
    #return matrix
#print(ZK_adjacency_matrix(graph_string))



#Question 12:
#I'll try to solve this question in the reference of lecture notes.

#def bfs_tree(adj_list, start):
    #"""This function is a rough replication of pseudocodes on lecture note"""
    #numv = len(adj_list)
    #state = ["U" for i in range(numv)]
    #parent = [None for j in range(numv)]
    #queue = deque([])
    #state[start] = "D"
    #queue.append(start)
    #return bfs_loop(adj_list, queue, state, parent)

#def bfs_loop(adj, queue, state, parent):
    #while len(queue) != 0:
        #h = queue.popleft() 
        #for k in adj[h]:
            #g = k[0]
            #if state[g] == "U":
                #state[g] = "D"
                #parent[g] = h
                #queue.append(g)
        #state[h] = "P"
    #return parent


#adj_list = [
    #[(1, None)],
    #[(0, None), (2, None)],
    #[(1, None)]
#]
#print(bfs_tree(adj_list, 0))
#print(bfs_tree(adj_list, 1))

#adj_list = [
#[(1, None)],
#[]
#]

#print(bfs_tree(adj_list, 0))
#print(bfs_tree(adj_list, 1))
    
#graph_string = """\
#D 2
#0 1
#"""

#print(bfs_tree(adjacency_list(graph_string), 0))

#graph_string = """\
#D 2
#0 1
#1 0
#"""

#print(bfs_tree(adjacency_list(graph_string), 1))

#graph_string = """\
#U 7
#1 2
#1 5
#1 6
#2 3
#2 5
#3 4
#4 5
#"""

#print(bfs_tree(adjacency_list(graph_string), 1))


#graph_string = """\
#D 2 W
#0 1 99
#"""

#print(bfs_tree(adjacency_list(graph_string), 0))

#def dfs_tree(adj_list, start):
    #"""this is also heavily based on lecture notes"""
    #numv = len(adj_list)
    #state = ["U" for i in range(numv)]
    #parent = [None for j in range(numv)]
    #state[start] = "D"
    #dfs_loop(adj_list,start,state,parent)
    #return parent
#def dfs_loop(adj, s, state, parent):
    #for k in adj[s]:
        #g = k[0]
        #if state[g] == "U":
            #state[g] = "D"
            #parent[g] = s
            #dfs_loop(adj,g,state,parent)
    #state[s] = "P"
## an undirected graph

#adj_list = [
    #[],
    #[],
    #[],
    #[(0, None)]
#]

#print(dfs_tree(adj_list, 0))
#print(dfs_tree(adj_list, 1))
#print(dfs_tree(adj_list, 2))
#print(dfs_tree(adj_list, 3))

            