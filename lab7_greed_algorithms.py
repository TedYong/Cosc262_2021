###this is about to get interesting###

###Question 2###

#def change_greedy(amount, coinage):
    #"""greed algorithm written on the notes, derived from coin changing problem"""
    #coin = sorted(coinage)
    #counts = [[0, i] for i in coin]
    #result = []
    #imax = len(counts) - 1
    #while amount > 0:
        #while coin[imax] > amount:
            #if imax >= 0:
                #imax = imax - 1
            #else:
                #break
        #counts[imax][0] += 1 
        #amount = amount - coin[imax]
        
    #if imax >= 0:
        #for i in range(len(counts)):
            #if counts[i][0] != 0:
                #result.append(counts[i])
                
        #result.reverse() 
        #for j in range(len(result)):
            #result[j] = result[j][0], result[j][1]
    #else:
        #result = None
    #return result

#print(change_greedy(82, [1, 10, 25, 5]))
#print(change_greedy(80, [1, 10, 25]))
#print(change_greedy(82, [10, 25, 5]))
#print(change_greedy(68, [1, 11, 17]))

###Question 3###
#19, 16, 81, 92, 205, 6, 159, 77, 5

###Question 4###

#def print_shows(show_list):
    #"""the algorithm from notes"""
    #new_list = []
    #final_list = []
    #real_list = []
    #for j in range(len(show_list)):
        #num = int(show_list[j][1]) + int(show_list[j][2])
        #final_list.append(num)
        #new_list.append((show_list[j][0], show_list[j][1], num))
    #final_list.sort()
    #for k in final_list:
        #for i in new_list:
            #if k == i[2]:
                #real_list.append(i)
    #result = []
    #current = 0
    #for i in range(len(real_list)):
        #if real_list[i][1] >= current:
            #result.append(real_list[i])
            #current = real_list[i][2]
    #for a, b, c in result:
        #print("{0} {1} {2}".format(a, b, c))
    
   
#ted = print_shows([
    #('a', 0, 6),
    #('b', 1, 3),
    #('c', 3, 2),
    #('d', 3, 5),
    #('e', 4, 3),
    #('f', 5, 4),
    #('g', 6, 4), 
    #('h', 8, 3)])
#ted

###Question 6###

#def fractional_knapsack(capacity, items):
    #"""time to improvise"""
    #real_weight = []
    #new_list = []
    #real_list = []
    #for a, b, c in items:
        #weight = b/c
        #real_weight.append(weight)
        #new_list.append((a, weight, c))
    #real_weight.sort()
    #real_weight.reverse()
    #for i in real_weight:
        #for j in new_list:
            #if i == j[1]:
                #real_list.append(j)
    #result = 0
    #current = 0
    #for j in range(len(real_list)):
        #if capacity >= current + real_list[j][2]:
            #result += real_list[j][1] * real_list[j][2]
            #current += real_list[j][2]
        #else:
            #num = capacity - current
            #result += num * real_list[j][1]
            #current += num
            #break
    #return result
#items = [
    #("Chocolate cookies", 20, 5),
    #("Potato chips", 15, 3),
    #("Pizza", 14, 2),
    #("Popcorn", 12, 4)]
#print(fractional_knapsack(9, items))

###Question 12###
################################################################################
###prerequisite setting###
#""" Installs and updates modules for the current user.
    #Updates pip if needed.
    #Overwrites any rubbish currently installed for each module.
#"""
#import sys
#import subprocess

#MODULES_TO_INSTALL = ['graphviz', 'numpy', 'matplotlib']
#PATH = sys.executable

#def update_pip():
    #""" Tries to ensure pip is installed and updated for the current user """
    #print('Upgrading pip to latest version... \n')
    #subprocess.run([PATH] + '-m pip install --user --upgrade pip'.split(), check=True)
    
    
#def install_module_for_user(module):
    #""" 
    #Installs module if needed.
    #Updates module if already installed.
    #Forces install/update over top of any rubbish that's already there
    #"""
    #print(f'Installing {module} for the current user... \n')
    #subprocess.run([PATH] + f'-m pip install --user {module} --upgrade --ignore-installed'.split(), check=True)
    

#def main():
    #""" Feel free to add other modules to the list of things to install """
    #print('Python executable at: {}\n'.format(PATH))
    #update_pip()
    #for module in MODULES_TO_INSTALL:    
        #install_module_for_user(module)


#if __name__ == "__main__":
    #main()
################################################################################

"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, count, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char
    
    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph
        

class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root
        
    def find_node(self, current_node, text_dict, result=""):
        """this function mainly serve as a helper function to encode function to 
        find routes of text exhaustively
        """
        if current_node.is_leaf():
            if current_node.char in text_dict:
                text_dict[current_node.char] = result
        else:
            self.find_node(current_node.left, text_dict, result + "0")
            self.find_node(current_node.right, text_dict, result + "1")
        return text_dict
        
    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.      
        """
        result = ""
        text_dict = dict()
        for i in text:
            text_dict[i] = 0
        binary_dict = self.find_node(self.root,text_dict)
        for k in text:
            for j in binary_dict:
                if j == k:
                    result += binary_dict[j]
        return result
        
        
        
    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        result = ""
        current = self.root
        b_list = list(binary)
        for j in b_list:
            if j == '0':
                current = current.left
            elif j == '1':
                current = current.right
            if current.is_leaf():
                result += current.char
                current = self.root                   
        return result
        
                

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)
    def find_min(self, alist):
        """find the minimum count in table"""
        list1 = []
        result = 0
        for i in alist:
            list1.append(i.count)
        list1.sort()
        if list1.count(list1[0]) == 1:
            for j in range(len(alist)):
                if alist[j].count == list1[0]:
                    result = j
        else:
            for i in range(len(alist)):
                if alist[i].count == list1[0]:
                    a = alist[i]
                    num1 = i
                    break
            for j in range(len(alist)):
                if alist[j].count == list1[0]:
                    b = alist[j]
                    num2 = j   
            if a.min_char < b.min_char:
                result = num1
            else:
                result = num2
        return result

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        result = ""
        trees = []
        for i in freqs:
            trees.insert(-1, Leaf(freqs[i], i))
        while len(trees) > 1:
            mini = self.find_min(trees)
            left = trees.pop(mini)
            mini = self.find_min(trees)
            right = trees.pop(mini)
            trees.insert(0, Node(left.count+right.count, left, right))
        #result = ' '.join([str(i) for i in trees]) 
        #for i in trees:
            #self.root = i
        
        #return self.root
        self.root = trees[0]
        return trees[0]
        

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


def main():
    #""" Demonstrate defining a Huffman tree from its string representation and
        #printing and plotting it (if plotting is enabled on your machine).
    #"""
    freqs = {'a': 9,
             'b': 8,
             'c': 15,
             'd': 3,
             'e': 5,
             'f': 2}
    tree = HuffmanTree()
    tree.build_from_freqs(freqs)
    print(tree)
    
    
    
   
    #tree = HuffmanTree()
    #tree_string = """Node(42,
      #Node(17,
        #Leaf(8, 'b'),
        #Leaf(9, 'a')),
      #Node(25,
        #Node(10,
          #Node(5,
            #Leaf(2, 'f'),
            #Leaf(3, 'd')),
          #Leaf(5, 'e')),
        #Leaf(15, 'c')))
    #"""
    #tree.build_from_freqs(tree_string)
    #print(tree)
    #tree.plot()
    
    ## Or you can build the tree directly
    #tree2 = HuffmanTree(Node(
      #Node(
        #Leaf(8, 'b'),
        #Leaf(9, 'a')),
      #Node(
        #Node(
          #Node(
            #Leaf(2, 'f'),
            #Leaf(3, 'd')),
          #Leaf(5, 'e')),
        #Leaf(15, 'c'))))
    #print(tree2)
    #print(tree2.encode('adcb'))
main()
