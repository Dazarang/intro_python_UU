import re

def wordCount(fileName, n):
    with open (fileName, "r") as file:
        textFile = file.read()
    
    wordList = re.findall(r'[a-zA-ZåäöÅÄÖ]+', textFile)
    numbWords = len(wordList)
    uniqueWords = len(set(wordList)) # Unique for me is how many different unique words there are, not that they should occur 1 time
    
    freq = {}
    
    for w in wordList:
        if w in freq:
            freq[w] +=1
        else:
            freq[w] = 1
            
    def part2(e):
        return e[1]
    
    freqOrder = (sorted(freq.items(), key=lambda k: k[1], reverse=True))
    
    print()
    print(f'Number of words in text: {numbWords}')
    print(f'Number of unique words: {uniqueWords}')       
    print(f'Top {n} most common words: {freqOrder[0:n]}')


   
fileName = "Assignments\Assignment3\Black_box.txt"

n = int(input("Number of common words seen: "))
wordCount(fileName, n)
    