#Part 3 b
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
    
    size = len(target)
        
    distances['A'] = 1
    
    while len(nodes) != 0:
        current = min(nodes, key=distances.get)
        nodes.remove(current)

        if single and current == target:
            return distances[target]

        adjacents = returnSet(current)
        for adjacent in adjacents:
            
            if len(adjacent) <= size:
                if adjacent not in distances:
                    nodes.append(adjacent)
                    distances[adjacent] = float('inf')
            
                new = distances[current] + 1
                if new < distances[adjacent]:
                    distances[adjacent] = new
                    
    return distances
    
letters = 'ABCDEFGH'

distances = shortest('ABCDE',False)

for i in distances:
    if distances[i] == 6 and len(i) == 5:
        print(i)
