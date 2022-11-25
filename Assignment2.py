###Question 1###
#def lcs(s1, s2):
    #"""this is outragous"""
    #n_s1 = len(s1)
    #n_s2 = len(s2)
    #cache = [[0 for i in range(n_s2 + 1)] for j in range(n_s1 + 1)]
    #for row in range(1, n_s1+1):
        #for col in range(1, n_s2+1):
            #if s1[row-1] == s2[col-1]:
                #cache[row][col] = cache[row-1][col-1] + 1
            #else:
                #last_num = cache[row-1][col]
                #next_num = cache[row][col-1]
                #if last_num >= next_num:
                    #cache[row][col] += last_num
                #else:
                    #cache[row][col] += next_num
    #i = n_s1
    #j = n_s2
    #output = []
    #while i > 0 and j > 0:
        #if s1[i-1] == s2[j-1]:
            #output.append(s1[i-1])
            #i-=1
            #j-=1
        #else:
            #solution1 = cache[i-1][j]
            #solution2 = cache[i][j-1]
            #if solution1 > solution2:
                #i = i - 1
            #else:
                #j = j - 1
        
    #result = reversed(output)
    #return ''.join(result)
#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(lcs(s1, s2))


###Question 3###

#def line_edits(s1, s2):
    #"""diff checker stemed from this"""
    #n_s1, n_s2 = len(str.splitlines(s1)), len(str.splitlines(s2))
    #result = []
    #cach = [[0] * (n_s2+1) for i in range(n_s1+1)]
    #for i in range(n_s1+1):
        #for j in range(n_s2+1):
            #if i == 0 or j == 0:
                #cach[i][j] = max(i, j)
            #elif str.splitlines(s1)[i-1] == str.splitlines(s2)[j-1]:
                #cach[i][j] = cach[i-1][j-1]
            #else:
                #cach[i][j] = min(cach[i][j-1],cach[i-1][j],cach[i-1][j-1]) + 1
    #s1, s2 = str.splitlines(s1), str.splitlines(s2)
    #while n_s1 > 0 or n_s2 > 0:
        #if (n_s1 > 0 and n_s2 > 0) and s1[n_s1-1] == s2[n_s2-1]:
            #result.append(('C', s1[n_s1-1], s2[n_s2-1]))
            #n_s1-=1
            #n_s2-=1
        #elif ((n_s1 > 0 and n_s2 > 0) and
              #(min(cach[n_s1-1][n_s2],cach[n_s1][n_s2-1],cach[n_s1-1][n_s2-1])==
               #cach[n_s1-1][n_s2-1])):
            #result.append(('S', s1[n_s1-1], s2[n_s2-1]))
            #n_s1-=1
            #n_s2-=1               
        #elif (n_s1 > 0 and 
              #(min(cach[n_s1-1][n_s2],cach[n_s1][n_s2-1],cach[n_s1-1][n_s2-1])==
               #cach[n_s1-1][n_s2])):
            #result.append(('D', s1[n_s1-1], ''))
            #n_s1-=1
        #elif (n_s2 > 0 and 
              #(min(cach[n_s1-1][n_s2],cach[n_s1][n_s2-1],cach[n_s1-1][n_s2-1])==
               #cach[n_s1][n_s2-1])):
            #result.append(('I', '', s2[n_s2-1]))
            #n_s2-=1
    #return reversed(result)

    
def line_edits(s1, s2):
    """calls the the backtrack to return the list of differences"""
    s1 = s1.splitlines() 
    s2 = s2.splitlines()
    if len(s1) == 0 and len(s2) == 0:
        return [('C', "", "")]
    odd_table = []
    if len(s1) == 0:
        for i in s2:
            odd_table.append(('I', "", i))
        return odd_table
    if len(s2) == 0:
        delete_table = []
        for i in s1:
            odd_table.append(("D", i, ""))
        return odd_table
    return backtrack(s1, s2)

def fill(s1, s2):
    """fill table top down"""
    table = [[None for col in range(len(s2) +1)] for row in range(len(s1)+1)]



    for i in range(len(table)):
        for j in range(len(table[0])):
            if i == 0 and j == 0:
                table[i][j] = 0
            if i == 0:
                table[i][j] = j 
            if j == 0:
                table[i][j] = i 
    
    row = 1
    col = 1
    while row < len(table):
        col = 1
        while col < len(table[0]):
            if s1[row-1] == s2[col-1]:
                table[row][col] = table[row-1][col-1]
                col +=1
            else:
                mini= 1 + min(table[row-1][col-1],table[row][col-1], table[row-1][col])
                table[row][col] = mini
                col +=1
        row += 1
    
    return table


def backtrack(s1, s2):
    """backtrack bottom up"""
    
    table = fill(s1, s2)
    row = len(table)-1
    col = len(table[0])-1
    output = []
    while row >= 0 and col >= 0:
        
        if s1[row-1] == s2[col-1]:
            output.append(('C', s1[row-1], s2[col-1]))
            row -= 1
            col -= 1
            if col == 0 or row == 0:
                break
        else: 
            
            if table[row][col] == table[row-1][col-1] + 1:
                output.append(("S", s1[row-1], s2[col-1]))
                row -= 1
                col -= 1
            elif table[row][col] == table[row-1][col] + 1 or col== 0:
                output.append(("D", s1[row-1], ""))
                row -= 1 
                if col == 0:
                    break
                       
            elif table[row][col] == table[row][col-1] + 1 or row ==0:
                output.append(("I", "", s2[col-1]))
                col -= 1
                if row == 0:
                    break
                
    return output[::-1]

            
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
#print(table)
for row in table:
    print(row)
('C', 'Line1', 'Line1')
('D', 'Line2', '')
('C', 'Line3', 'Line3')
('C', 'Line4', 'Line4')
('I', '', 'Line5')

print("----------------------------")
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
('S', 'Line1', 'Line5')
('S', 'Line2', 'Line4')
('C', 'Line3', 'Line3')
('D', 'Line4', '')

print("----------------------------")
s1 = "Line1\n"
s2 = ""
table = line_edits(s1, s2)
#print(table)
for row in table:
    print(row)
('D', 'Line1', '')

print("----------------------------")
s1 = ""
s2 = "Line1\n"
table = line_edits(s1, s2)
#print(table)
for row in table:
    print(row)
('I', '', 'Line1')
print("----------------------------")     
s1 = "Line1\nLine3\nLine5\n"
s2 = "Twaddle\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
('D', 'Line1', '')
('S', 'Line3', 'Twaddle')
('C', 'Line5', 'Line5')

