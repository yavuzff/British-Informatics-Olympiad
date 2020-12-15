#BIO 2018 part 2
#2B) LKBXIY done using puttin 1000000000 in input of program
#2C) It is impossible to have a dial that will result in the all 26 letters being in the answer
#the resulting answer will have a repeat of 13 letters twice
#this is because, as the inside dial is ordered alphabetically,
#encrypting the word is the same as going clockwise from A reading off the value for each letter
#as the outside dial gets turned after each reading as well,
#this means the dials will meet back in the same orientation after 13 letters
#producing the same previous 13 letters for a total of only 13 different letters


def generateLetters(n):
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alphabet = alphabet.split()
    
    letters = ['']*26
    pointer = 0
    for i in range (0,26):
        pointer += (n-1)
        pointer = pointer % (26-i)
        letters[i] = alphabet[pointer]
        alphabet.pop(pointer)

    return letters

def index(letter):
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alphabet = alphabet.split()

    return alphabet.index(letter)

parta = True

alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
alphabet = alphabet.split()

data = input().split()

n = int(data[0])
word = data[1]

a2 = generateLetters(n)
print(''.join(a2[0:6]))

if parta:
    start = 0
    new = ''

    for i in range (0,len(word)):
        char = word[i]
        newchar = a2[(start+index(char))%26]
        new += newchar
        start+=1

    print(new)

else: #part d
    counts = []
    indices = []
    for i in range (1,1000):
        for j in range (1,27):
            a2 = generateLetters(i)
            word = alphabet[0:j]
            count = 0
            word1 = word
            while True:
                new = ''
                for i in range (0,len(word)):
                    char = word1[i]
                    new += a2[index(char)]
                count += 1
                if new == word:
                    counts.append(count)
                    indices.append([i,word])
                    break
                else:
                    word1 = new

    best = max(counts)
    index = counts.index(best)

    print(best, indices[index])
