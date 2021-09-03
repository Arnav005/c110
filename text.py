f=open("test.txt")
print(f.read())
fileLines=f.readlines()
for i in fileLines:
    print(i)

text='my nameee@ is arnavvv'
print(text.split('@'))

def greetings(name):
     print("Happy Birthday"+name)
greetings("Arnav")

def countWordFromFile():
    file=input("my naameeeeee is aj")
    no_of_words=0
    file=open(file,'r')
    for line in file():
        words = line.split()
        no_of_words=no_of_words+len(words)
    print("no_of_words")
    print(no_of_words)

countWordFromFile()
