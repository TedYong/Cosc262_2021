### mid_term of 261 is impending over and I must save some time to revise what I have learnt ###
from collections import deque
from math import inf
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

#def transpose(adj_list):
    #"""transpose is the directed graph with opposite directions"""
    #length = len(adj_list)
    #result = [[] for i in range(length)]
    #for i in range(length):
        #for j in adj_list[i]:
            #result[j[0]].append((i, j[1]))

    #return result
##print(transpose(graph_adj_list))

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
    #return state

#def is_strongly_connected(adj_list):
    #"""this is closely related to lecture notes"""
    #for i in range(len(adj_list)):
        #positive_traversal = bfs_tree(adj_list, i)
    #if "U" in positive_traversal:
        #return False
    #else:
        #new_list = transpose(adj_list)
        #for j in range(len(adj_list)):
            #reverse_traversal = bfs_tree(new_list, j)        
        #if "U" in reverse_traversal:
            #return False
        #else:
            #return True
    
    
#graph_string = """\
#D 3
#0 1
#1 0
#0 2
#"""

#print(is_strongly_connected(adjacency_list(graph_string)))
            
#graph_string = """\
#D 3
#0 1
#1 2
#2 0
#"""

#print(is_strongly_connected(adjacency_list(graph_string)))

#graph_string = """\
#D 4
#0 1
#1 2
#2 0
#"""

#print(is_strongly_connected(adjacency_list(graph_string)))

#graph_string = """\
#U 5
#2 4
#3 1
#0 4
#2 1
#"""

#print(is_strongly_connected(adjacency_list(graph_string)))
    
#def prim(adj_list, start):
    #length = len(adj_list)
    #in_tree = [False for i in range(length)]
    #distance = [float('inf') for i in range(length)]
    #parent = [None for i in range(length)]
    #distance[start] = 0
    #while False in in_tree:
        #u = next_vertex(in_tree, distance)
        #in_tree[u] = True
        #for v, weight in adj[u]:
            #if in_tree[v] + weight < distance[v]
            #distance[v] = weight
            #parent[v] = u
    #return parent, distance 
        
#graph_string = """\
#U 5
#2 4
#3 1
#0 4
#2 1
#"""
#haha = adjacency_list(graph_string)
#print(prim(haha, 0))

def next_vertex(in_tree, distance):
    """this actually takes me a whole week, time to settle this"""
    result = 0
    lists = []
    index = []
    haha = 0
    for i in range(len(in_tree)):
        if in_tree[i] == True:
            result = distance[i]
        else:
            lists.append(distance[i])
            index.append(i)
            haha = i
    dis = min(lists)
    if type(dis) == float:
        return haha
    else:
        for j in range(len(lists)):
            if dis == lists[j]:
                return index[j]
        
def dijkstra(adj_list, start):
    """last one, good to go"""
    numv = len(adj_list)
    in_tree = [False for i in range(numv)]
    distance = [float('inf') for i in range(numv)]
    parent = [None for i in range(numv)]
    distance[start] = 0
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] + distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
#graph_string = """\
#U 4 W
#0 2 5
#0 3 2
#3 2 2
#"""

#print(dijkstra(adjacency_list(graph_string), 0))
#print(dijkstra(adjacency_list(graph_string), 2))

###Bnous: prims algorithm###
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
    #return parent, distance        