#def lcs(s1, s2, cache=None):
    #x= len(s1)
    #y= len(s2)
    #if cache==None:
        #cache=[[None for i in range(y+1)] for j in range(x+1)]
    #if cache[x][y] != None:
        #return cache[x][y] 
    #if x == 0 or y == 0:
        #return ''
    #elif s1[x-1] == s2[y-1]:
        #cache[x][y] = lcs(s1[:-1], s2[:-1], cache) + s1[x-1]
        #return cache[x][y]
    #else:
        #one = lcs(s1[:-1], s2, cache)
        #two = lcs(s1, s2[:-1], cache)
        #if len(one) > len(two):
            #cache[x][y] = one
            #return one
        #else:
            #cache[x][y] = two
            #return two
#def lcs(s1, s2):
    #x = len(s1)
    #y = len(s2)
    #cache = [[0 for j in range(y+1)] for i in range(x+1)]
    #for i in range(1,x+1):
        #for j in range(1,y+1):
            #if s1[i-1] == s2[j-1]:
                #cache[i][j] = cache[i-1][j-1] + 1
            #else:
                #one = cache[i-1][j]
                #two = cache[i][j-1]
                #if one > two:
                    #cache[i][j] = one
                #else:
                    #cache[i][j] = two
    #a = x
    #b = y
    #result = []
    #while a > 0 and b > 0:
        #if s1[a-1] == s2[b-1]:
            #result.append(s1[a-1])
            #a-=1
            #b-=1
        #else:
            #if cache[a-1][b] > cache[a][b-1]:
                ##result.append(s1[a-1])
                #a-=1
            #else:
                ##result.append(s2[b-1])
                #b-=1
    #return ''.join(reversed(result))

def print_shows(show_list):
    """haskdhaksjdak"""
    new_list = []
    for i in show_list:
        new_list.append((i[0], i[1], i[2]))
    new_list = sorted(new_list, key=lambda x:x[2])
    return new_list
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4), 
    ('h', 8, 3)])
