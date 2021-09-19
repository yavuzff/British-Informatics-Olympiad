#Yavuz Part 3 c
def add(string):    
    index = len(string)
    return string+letters[index]

def swap(string):
    n1 = string[0]
    n2 = string[1]

    return n2+n1+string[2:]

def rotate(string):
    n1 = string[0]
    return string[1:] + n1

def returnSet(word):
    words = set()
    if len(word) !=8:
        words.add(add(word))
        
    try:
        words.add(swap(word))
    except: pass
    
    words.add(rotate(word))
    
    return words

def shortest(target,single=True):
    nodes = ['A']
    distances = {}
    path = {}
    
    size = len(target)
    paths = []
    distances['A'] = 1
    count = 0
    while len(nodes) != 0:
        #print(distances)
        #print(nodes)
        current = min(nodes, key=distances.get)
        nodes.remove(current)

        adjacents = returnSet(current)
        for adjacent in adjacents:
            
            if len(adjacent) <= size:
                if adjacent not in distances:
                    nodes.append(adjacent)
                    distances[adjacent] = float('inf')
                    path[adjacent] = set()
            
                new = distances[current] + 1
                if new == distances[adjacent]:

                    path[adjacent].add(current)
                    
                elif new<distances[adjacent]:

                    distances[adjacent] = new
                    path[adjacent] = {current}
                    
    return path

def paths(node):
    if node == 'BA':
        return 2
    if node == 'A':
        return 1

    subnodes = nodes[node]
    total = 0
    for subnode in subnodes:
        total += paths(subnode)

    return total

#AB and BA have 2 to each other 
letters = 'ABCDEFGH'

#a = shortest('HGFEDCBA')
#print(a)
#print(findpath(a[0],'HGFEDCBA'))
while 1:
    #word = 'BAC'
    #word = 'HGFEDCBA'
    word = input()
    nodes = shortest(word,True)
    print(paths(word))
