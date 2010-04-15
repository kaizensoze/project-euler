vals = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900
}

reVals = {
        1:'I',
        5:'V',
        10:'X',
        50:'L',
        100:'C',
        500:'D',
        1000:'M',
        4:'IV',
        9:'IX',
        40:'XL',
        90:'XC',
        400:'CD',
        900:'CM'
}

numLetterCount = {
        1:1,
        5:1,
        10:1,
        50:1,
        100:1,
        500:1,
        1000:1,
        4:2,
        9:2,
        40:2,
        90:2,
        400:2,
        900:2
}

exceptions = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']

f = open('../roman.txt', 'r')
numerals = [x.strip() for x in f.readlines()]
#numerals = ['MMCDLIX', 'MMDCCCLXXXIII']

def getValue(s):
    result = 0
    for exception in exceptions:
        result += s.count(exception) * vals[exception]
        s = s.replace(exception, '')
    for i in s:
        result += vals[i]
    return result

def reduced(x):
    count = 0
    s = ''
    b = list(vals.values())
    b.sort()
    b.reverse()
    for val in b:
        while x >= val and x > 0:
            x -= val
            count += numLetterCount[val]
            s += reVals[val]
    return count, s

lettersSaved = 0
for x in numerals:
    y = x
    oldCount = len(y)
    result = getValue(y)
    newCount, newY = reduced(result)
    lettersSavedLocal = (oldCount - newCount)
    lettersSaved += lettersSavedLocal
    print(result, end=' ')
    print(x, end=' ')
    print(newY, end=' ')
    print(lettersSavedLocal)

print(lettersSaved)
