import re
import keyword

def listSource(fileName):
      
    for lineIndex, textLine in enumerate(fileName, start=1):    
        print(lineIndex, textLine)

def refList(fileName):
    
    keywordList = keyword.kwlist

    referenceListDict = {}
    
    for lineIndex, textLine in enumerate(fileName, start=1): 
        print("Textfile:", textLine)
        textLine = re.sub(r'#.*$', "", textLine)
        
        for keyWords in keywordList:
            textLine = re.sub(r'\b%s\b' % keyWords, "", textLine)
        
        wordList = re.findall(r'[a-zA-ZåäöÅÄÖ]+', textLine)

        for w in wordList:
            if w in referenceListDict:
                words = referenceListDict.get(w)
                words.append(lineIndex)
            else:
                referenceListDict[w] = [lineIndex]
                        
    print("\nReference list:")
    sortDict = sorted(referenceListDict.items())
    for item in sortDict:
        print("     ", item[0], "\t", item[1], end="\n" )
    
    

fileName = "Assignments/Assignment3/pythonFile.py"

with open (fileName, "r") as file:
    textFile = file.read().splitlines()

listSource(textFile)
refList(textFile)