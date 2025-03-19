name = input('Enter file:') #name variable
handle = open(name, 'r') #opens the file on read mode
counts = dict() #created an empty dictionary

#Nested for loop
for line in handle:
    words = line.split() #split a line of text into separate words
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#find the most common word
bigcount = None
bigword = None

#for loop
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word #returns the most common word
        bigcount = count #returns the number of times the word repeats
 
print(bigword, bigcount)