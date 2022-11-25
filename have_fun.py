###top_down DP example###
#def common(s1, s2, cashe=None):
    #"""does recursion"""
    #if cashe is None:
        #cashe = {}
    #if (len(s1), len(s2)) not in cashe:
        #if len(s1) == 0 or len(s2) == 0:
            #cashe[(len(s1), len(s2))] = (0, '')
        #elif s1[len(s1) - 1] == s2[len(s2) - 1]:
            #tup = common(s1[:-1], s2[:-1], cashe)
            #cost, lcs = tup
            #cost += 1
            #lcs += s1[-1]
            #cashe[(len(s1), len(s2))] = (cost, lcs)
        #else:
            #tup1 = common(s1[:-1], s2, cashe)
            #tup2 = common(s1, s2[:-1], cashe)
            #cost1, lcs1 = tup1
            #cost2, lcs2 = tup2
            #if cost1 < cost2:
                #cashe[(len(s1), len(s2))] = (cost2, lcs2)
            #else:
                #cashe[(len(s1), len(s2))] = (cost1, lcs1)
    #return cashe[(len(s1), len(s2))]    

#def longest_common_substring(s1, s2):
    #"""calls recursion"""
    #value = common(s1, s2)
    #return value[1]
    

#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(longest_common_substring(s1, s2))

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(longest_common_substring(s1, s2))

#s1 = "balderdash!"
#s2 = "balderdash!"
#print(longest_common_substring(s1, s2))


###bottom_up DP example###
#def longest_common_substring(s1, s2):
    #"""maybe not recursive"""
    #grid = [[0 for y in range(len(s1) + 1)] for x in range(len(s2) + 1)]
    #x = 0
    #for x in range(len(grid)):
        #y = 0
        #while y < len(grid[0]):
            #if x == 0 or y == 0:
                #grid[x][y] = 0
            #elif s1[y - 1] == s2[x - 1]:
                #grid[x][y] = grid[x - 1][y - 1] + 1
            #else:
                #grid[x][y] = max(grid[x][y - 1], grid[x - 1][y])
            #y += 1
    #a = len(s2)
    #b = len(s1)
    #lcs = ''
    #while a > 0 and b > 0:
        #if s1[b - 1] == s2[a - 1]:
            #lcs += s1[b - 1]
            #a -= 1
            #b -= 1
        #elif grid[a][b - 1] > grid[a - 1][b]:
            #b -= 1
        #else:
            #a -= 1
    #return lcs[::-1]

#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(longest_common_substring(s1, s2))

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(longest_common_substring(s1, s2))

#s1 = "balderdash!"
#s2 = "balderdash!"
#print(longest_common_substring(s1, s2))

#s1 = 1500 * 'x'
#s2 = 1500 * 'y'
#print(longest_common_substring(s1, s2))