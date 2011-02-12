'''
Created on Apr 17, 2009

@author: anon
'''

import time

f = open('../cipher1.txt', 'r')
letters = [x.strip() for x in f.readline().split(',')]
f.close()
#f = open('../plain1.txt', 'w')
#print(letters)
for letter1 in range(ord('g'), ord('g')+1):
    for letter2 in range(ord('o'), ord('o')+1):
        for letter3 in range(ord('d'), ord('d')+1):
            key = []
            key.append(chr(letter1))
            key.append(chr(letter2))
            key.append(chr(letter3))
#            keyLabel = "********* " + str(key) + " *********" + '\n'
#            f.write(keyLabel)
#            print("*********", key, "*********")
            plaintext = ''.join([chr(int(x) ^ ord(key[i%3])) for i,x in enumerate(letters)])
#            plaintext = plaintext + '\n'
            print(sum([ord(x) for x in plaintext]))
#            f.write(plaintext)
#            print(plaintext)
#        time.sleep(10)
#f.close()