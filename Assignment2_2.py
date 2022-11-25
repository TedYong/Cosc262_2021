###Question 4###
def lcs(s1, s2):
    """this is outragous"""
    n_s1 = len(s1)
    n_s2 = len(s2)
    cache = [[0 for i in range(n_s2 + 1)] for j in range(n_s1 + 1)]
    for row in range(1, n_s1+1):
        for col in range(1, n_s2+1):
            if s1[row-1] == s2[col-1]:
                cache[row][col] = cache[row-1][col-1] + 1
            else:
                last_num = cache[row-1][col]
                next_num = cache[row][col-1]
                if last_num >= next_num:
                    cache[row][col] += last_num
                else:
                    cache[row][col] += next_num
    i = n_s1
    j = n_s2
    output = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            output.append(s1[i-1])
            i-=1
            j-=1
        else:
            solution1 = cache[i-1][j]
            solution2 = cache[i][j-1]
            if solution1 > solution2:
                i = i - 1
            else:
                j = j - 1
        
    result = reversed(output)
    return ''.join(result)

def line_edits(s1, s2):
    """diff checker stemed from this"""
    n_s1, n_s2 = len(str.splitlines(s1)), len(str.splitlines(s2))
    result = []
    cach = [[0] * (n_s2+1) for i in range(n_s1+1)]
    for i in range(n_s1+1):
        for j in range(n_s2+1):
            if i == 0 or j == 0:
                cach[i][j] = max(i, j)
            elif str.splitlines(s1)[i-1] == str.splitlines(s2)[j-1]:
                cach[i][j] = cach[i-1][j-1]
            else:
                cach[i][j] = min(cach[i][j-1],cach[i-1][j],cach[i-1][j-1]) + 1
    s1, s2 = str.splitlines(s1), str.splitlines(s2)
    while n_s1 > 0 or n_s2 > 0:
        if (n_s1 > 0 and n_s2 > 0) and s1[n_s1-1] == s2[n_s2-1]:
            result.append(('C', s1[n_s1-1], s2[n_s2-1]))
            n_s1-=1
            n_s2-=1
        elif ((n_s1 > 0 and n_s2 > 0) and
              (min(cach[n_s1-1][n_s2],cach[n_s1][n_s2-1],cach[n_s1-1][n_s2-1])==
               cach[n_s1-1][n_s2-1])):
            e1 = []
            e2 = []
            diff1 = lcs(s1[n_s1-1], s2[n_s2-1])
            for i in range(len(s1[n_s1-1])):
                if len(diff1) != 0 and diff1[0] == (s1[n_s1-1])[i]:
                    diff1 = diff1[1:]
                else:
                    e1.append(i)
            left = list(s1[n_s1-1])
            for i in e1:
                #print(i)
                left[i] = "[["+left[i]+"]]"
            left = ''.join(left)
            diff2 = lcs(s1[n_s1-1], s2[n_s2-1])
            for j in range(len(s2[n_s2-1])):
                if len(diff2) != 0 and diff2[0] == (s2[n_s2-1])[j]:
                    diff2 = diff2[1:]
                else:
                    e2.append(j)
            right = list(s2[n_s2-1])
            for j in e2:
                #print(j)
                right[j] = "[["+right[j]+"]]"   
            right = ''.join(right)
            result.append(('S', left, right))
            n_s1-=1
            n_s2-=1               
        elif (n_s1 > 0 and 
              (min(cach[n_s1-1][n_s2],cach[n_s1][n_s2-1],cach[n_s1-1][n_s2-1])==
               cach[n_s1-1][n_s2])):
            result.append(('D', s1[n_s1-1], ''))
            n_s1-=1
        elif (n_s2 > 0 and 
              (min(cach[n_s1-1][n_s2],cach[n_s1][n_s2-1],cach[n_s1-1][n_s2-1])==
               cach[n_s1][n_s2-1])):
            result.append(('I', '', s2[n_s2-1]))
            n_s2-=1
    return reversed(result)
    
    
#s1 = "Line1\nLine2\nLine3\nLine4\n"
#s2 = "Line5\nLine4\nLine3\n"
#table = line_edits(s1, s2)
##print(table)
#for row in table:
    #print(row)

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
#print(table)
for row in table:
    print(row)
