# Read from the file words.txt and output the word frequency list to stdout.
from collections import defaultdict
file_object=open('words.text','r')

lines=file_object.readlines()

words_count=defaultdict(int)
word=""

for line in lines:

    for char in line:
        
        if (char==" ") or (char=='\n'):
            if char==" ":
            	words_count[" "]+=1
            else:
            	words_count["NL"]+=1

            if word!="":
            	words_count[word]+=1
        
            word=""
        else:
        	word+=char

print(words_count)

res=sorted(words_count.items(),key=lambda x : x[1],reverse=True)

for words in res:
    print(words[0]  ,  words[1])