'''
Created on Apr 4, 2009

@author: anon
'''

numbers = {
            1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine',
            10 : 'ten',
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'nineteen',
            20 : 'twenty',
            30 : 'thirty',
            40 : 'forty',
            50 : 'fifty',
            60 : 'sixty',
            70 : 'seventy',
            80 : 'eighty',
            90 : 'ninety'            
          }

words = {
          'one' : 3,
          'two' : 3,
          'three' : 5,
          'four' : 4,
          'five' : 4,
          'six' : 3,
          'seven' : 5,
          'eight' : 5,
          'nine' : 4,
          'ten' : 3,
          'eleven' : 6,
          'twelve' : 6,
          'thirteen' : 8,
          'fourteen' : 8,
          'fifteen' : 7,
          'sixteen' : 7,
          'seventeen' : 9,
          'eighteen' : 8,
          'nineteen' : 8,
          'twenty' : 6,
          'thirty' : 6,
          'forty' : 5,
          'fifty' : 5,
          'sixty' : 5,
          'seventy' : 7,
          'eighty' : 6,
          'ninety' : 6,
          'hundred' : 7,
          'and' : 3,
          'thousand' : 8          
        }
count = 0

def analyze(x):
    if len(str(x)) == 1:
        return words[numbers[x]] 
    elif len(str(x)) == 2:
        tensDigit = int(str(x)[0])
        onesDigit = int(str(x)[1])
        
        if tensDigit == 1 or onesDigit == 0:
            return words[numbers[x]]
        else:            
            return words[numbers[tensDigit*10]] + words[numbers[onesDigit]]
    elif len(str(x)) == 3:
        hundredsDigit = int(str(x)[0])
        tensDigit = int(str(x)[1])
        onesDigit = int(str(x)[2])
        
        rest = int(str(x)[1:])
                                        
        if tensDigit == 0 and onesDigit == 0:
            return words[numbers[hundredsDigit]] + words['hundred']
        elif rest < 20 or onesDigit == 0:
            return words[numbers[hundredsDigit]] + words['hundred'] \
                    + words['and'] + words[numbers[rest]]
        else:
            return words[numbers[hundredsDigit]] + words['hundred'] \
                    + words['and'] + words[numbers[tensDigit*10]]   \
                    + words[numbers[onesDigit]]
    
    elif len(str(x)) == 4:
        return words['one'] + words['thousand']
    else:
        return 0

for i in xrange(1,1000+1):
    count = count + analyze(i)

print(count)