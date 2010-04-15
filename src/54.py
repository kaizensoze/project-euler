
from functools import reduce

ROYAL_FLUSH = 100
STRAIGHT_FLUSH = 90
FOUR_OF_KIND = 80
FULL_HOUSE = 70
FLUSH = 60
STRAIGHT = 50
THREE_OF_KIND = 40
TWO_PAIRS = 30
ONE_PAIR = 20

cardVals = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

PLAYER_WINS = 0

def isFlush(suits):
    suitCount = 0
    suits = {}
    for suit in suits:
        if suit in suits:
            suits[suit] += 1
            if suits[suit] == 5:
                return True
        else:
            suits[suit] = 1
    return False

def isStraight(vals):
    for i in range(len(vals)-1):
        if vals[i+1] != vals[i]+1:
            return False
    return True

def extractVals(hand):
    vals = []
    for card in hand:
        val = cardVals[card[0]]
        vals.append(val)

def scoreHand(hand):
    four = 0
    three = 0
    two = 0
    one = 0

    vals = []
    suits = []
    valCount = {}
    for card in hand:
        val = cardVals[card[0]]
        vals.append(val)
        suit = card[1]
        suits.append(suit)
        if val in valCount:
            valCount[val] += 1
        else:
            valCount[val] = 1
    vals = sorted(vals)
    twoCount = 0
    twoNum = 0
    for k in valCount.keys():
        if valCount[k] == 4:
            four = k
        if valCount[k] == 3:
            three = k
        if valCount[k] == 2 and k != twoNum:
            twoNum = k
            twoCount += 1
            if twoCount >= 2:
                two = k
        if valCount[k] == 2:
            one = k

    if three > 0 and one > 0:
        return [FULL_HOUSE, three, one]

    if isFlush(suits):
        if isStraight(vals):
            if vals[4] == cardVals['A']:
                return [ROYAL_FLUSH]
            else:
                return [STRAIGHT_FLUSH]
        else:
            return [FLUSH]
    else:
        if isStraight(vals):
            return [STRAIGHT]
        elif four > 0:
            return [FOUR_OF_KIND, four]
        elif three > 0:
            return [THREE_OF_KIND, three]
        elif two > 0:
            return [TWO_PAIRS, two]
        elif one > 0:
            return [ONE_PAIR, one]
        else:
            return [vals[4]]

def determineResult(one, two):
    global PLAYER_WINS
    oneScore = scoreHand(one)
    twoScore = scoreHand(two)

    #if oneScore[0] >= 60 or twoScore[0] >= 60:
    #    print(oneScore, end=' ')
    #    print(twoScore, end=' ')
    #    print(one, end=' ')
    #    print(two, end=' ')

    if oneScore[0] == twoScore[0]:
        if oneScore[0] == FULL_HOUSE:
            result = oneScore[1:2] > twoScore[1:2]
        else:
            result = oneScore[1] > twoScore[1]
    else:
        result = oneScore[0] > twoScore[0]

    if result:
        PLAYER_WINS += 1

# FUGLY CODE
f = open('../poker.txt', 'r')
for x in f.readlines():
    cards = [y for y in x.strip().split(' ')]
    player1 = []
    player1.append(cards[0]) 
    player1.append(cards[1]) 
    player1.append(cards[2]) 
    player1.append(cards[3]) 
    player1.append(cards[4]) 
    player2 = []
    player2.append(cards[5]) 
    player2.append(cards[6]) 
    player2.append(cards[7]) 
    player2.append(cards[8]) 
    player2.append(cards[9]) 
    determineResult(player1, player2)
print(PLAYER_WINS)
