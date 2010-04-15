import random

f = open('/home/anon/documents/programming_languages.txt')
files = [x.rstrip() for x in f]
i = random.randint(0,len(files)-1)
print(files[i])
