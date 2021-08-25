introstring=input("Enter your introduction")
print(introstring)
charactercount=0
wordcount=0
for i in introstring:
    charactercount=charactercount+1
    if(i==' '):
        wordcount=wordcount+1  
print("Number of Words in the string:")
print(wordcount)
print("number of characters in the string:")
print(charactercount)
