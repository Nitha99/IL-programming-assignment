import csv
#task1
with open("word_corpus.txt",encoding="utf8") as fin,open("temporary.txt","w") as fout:
    for line in fin:
        fout.write(line.replace('\t',','))
with open('temporary.txt') as csvDataFile:
    i=1
    occurrence=[]
    word=[]
    data = [row for row in csv.reader(csvDataFile)];
    for i in range(1,10001):
        occurrence.append(int(data[i][0]))
        word.append(data[i][1])
#print(occurrence)
#print(word)
f=open("character_mapping.txt","r",encoding="utf8")
lines=f.readlines()
character=[]
represented_by=[]
for x in lines:
    character.append(x.split('\t')[0])
    represented_by.append(x.split('\t')[1])
f.close()
represented_by=[s.replace('\n','')for s in represented_by]
#print(character)
#print(represented_by)
i=0
j=1
c=0
final=[]
for i in range(1,51):
    for j in range(0,9999):
        if(represented_by[i] in word[j]):
            word[j]=word[j].replace(represented_by[i],character[i])
           # c=c+1
#print(word)
#print(c)
zip(occurrence,word)
with open("word_frequency.txt","w",encoding="utf8") as f:
    writer=csv.writer(f,delimiter='\t')
    writer.writerows(zip(occurrence,word))
    
#task2
i=0
j=0
str=input('enter the string to be checked')
for i,j in zip(word,occurrence):
    if i.startswith(str):
        print((i,j))
        