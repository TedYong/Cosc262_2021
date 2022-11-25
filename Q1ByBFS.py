'''Assignment - Q1 solve by BFS'''

from collections import deque

def adjacency_list(graph_str):
    graph_text = graph_str.splitlines()
    
    num_of_lists = graph_text[0].split()
    matrix = [[] for _ in range(int(num_of_lists[1]))]
    
    if graph_text[0][0] == "D":
        for i in range(1, len(graph_text)):
            line = graph_text[i].split()
            if len(line) == 3:
                weight = int(line[2])
            else:
                weight = None
            matrix[int(line[0])].append((int(line[1]), weight))
    else:
        for i in range(1, len(graph_text)):
            line = graph_text[i].split()
            #print(line)
            if len(line) == 3:
                weight = int(line[2])
            else:
                weight = None            
            matrix[int(line[0])].append((int(line[1]), weight))
            matrix[int(line[1])].append((int(line[0]), weight))
    
    return matrix


def bfs_tree(adj_list, start):
    length = len(adj_list)
    states = ["U" for _ in range(length)]
    parent = [None for _ in range(length)]
    queue = deque()
    queue.append(start)
    states[start] = "D"
    bfs_loop(adj_list, queue, states, parent)
    return parent

def bfs_loop(adj_list, queue, states, parent):
    while len(queue) > 0:
        row_vertex = queue.popleft()
        for v, w in adj_list[row_vertex]:
            if states[v] == "U":
                states[v] = "D"
                parent[v] = row_vertex
                queue.append(v)
        states[row_vertex] = "P"
    return parent

def shortest_path(parent, start, end):
    if start == end:
        return [start]
    else:
        if (parent[end] != None):
            return [end] + shortest_path(parent, start, parent[end])

def format_sequence(converters_info, source_format, destination_format):
    adj_list = adjacency_list(converters_info)
    parents = bfs_tree(adj_list, source_format)
    result = shortest_path(parents, source_format, destination_format)
    if result == None:
        return "No solution!"
    else:
        result.reverse()
        return result
    

converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

print(format_sequence(converters_info_str, source_format, destination_format))
#[0, 1]
converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 1))
#[1]
converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 0))
#No solution!
converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(format_sequence(converters_info_str, 1, 2))
#[1, 2]
converters_info_str = """\
D 1
"""

print(format_sequence(converters_info_str, 0, 0))
#[0]

#test = [None, None, 1, 2, 5, 1, 1]
#print(shortest_path(test, 1, 1))