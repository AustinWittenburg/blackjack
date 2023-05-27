import random

freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']
deck = []
timesSplit = 0
splitHandsPlayed = 0
canSurrender = True
count = 0
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
evalMessage = ""
playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
possibleOptions = []
playerCash = 500
playerBet = 5
playerChoice = ""
playerHands = [] # [ [card0, card1], [card0, card1] ] Multiple hands are optional
dealerHand  = [] #   [card0, card1]
dealerShows = []

numDecks = 5

def shuffleDeck():
    global deck
    for _ in range(numDecks):
        deck += freshDeck
    random.shuffle(deck)

def dealHands():
    global dealerShows
    newHand = []
    
    newHand.append(drawCard(False) )
    dealerHand.append(drawCard(True) ) # Don't update count on dealers down card
    newHand.append(drawCard(False) )
    dealerHand.append(drawCard(False) )

    playerHands.append(newHand)
    dealerShows = dealerHand[:]
    dealerShows[0] = '  '

def displayHands():
    print("Dealer:\t\t\tCount: {}\t${:.2f}".format(count, playerCash) )
    prettyPrintDealerHand(dealerShows)
    print("Player:\t\t\tBet: ${:.2f}\t\t{}".format(playerBet, evalMessage) )
    prettyPrintPlayerHand(playerHands)

def giveOpitons():
    global possibleOptions
    possibleOptions = ["Hit", "Stand"]
    if playerCanDouble:
        possibleOptions.append("Double")
    if playerCanSplit:
        possibleOptions.append("Split")
    if playerCanSurrender:
        possibleOptions.append("Surrender")
    displayOptions()

def displayOptions():
    optionNum = 0
    for option in possibleOptions:
        optionNum += 1
        print("\t{}. {}".format(optionNum, option))

def getPlayerChoice():
    global playerChoice
    userInput = input()
    if userInput == "q" or userInput == "quit" or userInput == "exit":
        exit()
    playerChoice = possibleOptions[int(userInput)]

def executePlayerChoice():
    pass

def HiLoCount(card):
    global count
    if card[0] in HiLo[0]:
        count += 1
    elif card[0] in HiLo[2]:
        count -= 1

def drawCard(DealerDownCard):
    card = deck.pop()
    if not DealerDownCard:
        HiLoCount(card)
    return card

def handValue(hand):
    sum = 0
    numAces = 0
    for card in hand:
        if cardValue(card) == 11:
            numAces += 1    
        else:
            sum += cardValue(card)
    for i in range(numAces):
        if (i == (numAces - 1) ) and ( (sum + 11) <= 21): 
            sum += 11
        else: sum += 1
    return sum

def playerHasSoftHand(hand):
    numAces = 0
    for card in hand:
        if card[0] == 'A':
            numAces += 1
    return numAces == 1

def playerCanSplit(hand):
    return hand[0][0] == hand[1][0] and len(hand) == 2 and timesSplit < 3

def playerCanDouble(hand):
    return len(hand) == 2

def playerCanSurrender():
    return canSurrender

def playerBust(hand):
    return handValue(hand) > 21

def dealerBust():
    return handValue(dealerHand) > 21

def cardValue(card):
    val = card[0]
    if   val == 'T':
        return 10
    elif val == 'J':
        return 10
    elif val == 'Q':
        return 10
    elif val == 'K':
        return 10
    elif val == 'A':
        return 11
    else:
        return int(val)

def prettyPrintDealerHand(hand):
    message = ["", "", "", "", "", "", ""]

    for card in hand:
            message[0] +=     ('┌─────────┐ ')
            if card[0] == 'T':
                message[1] += ('│{:<2}       │ ').format(10)
            else:
                message[1] += ('│{:<2}       │ ').format(card[0])
            message[2] +=     ('│         │ ')
            message[3] +=     ('│    {}    │ '.format(card[1]))
            message[4] +=     ('│         │ ')
            if card[0] == 'T':
                message[5] += ('│       {:<2}│ ').format(10)
            else:
                message[5] += ('│       {:<2}│ ').format(card[0])
            message[6] +=     ('└─────────┘ ')

    for line in message:
        print(line)

def prettyPrintPlayerHand(hand): # ['6♣', 'Q♦'] or [ [card0, card1], [card0, card1] ]
    message = ["", "", "", "", "", "", ""]

    for i in range(splitHandsPlayed):
        for card in hand[i]:
            message[0] +=     ('┌───')
            if card[0] == 'T':
                message[1] += ('│{:<2} ').format(10)
            else:
                message[1] += ('│{:<2} ').format(card[0])
            message[2] +=     ('│   ')
            message[3] +=     ('│   ')
            message[4] +=     ('│   ')
            message[5] +=     ('│   ')
            message[6] +=     ('└───')
        for j in range(7):
            message[j] += '|'
    
    if splitHandsPlayed != 0:
        for i in range(7):
            message[i] += ' '
    
    for i in range(splitHandsPlayed, len(hand)):
        for card in hand[i]:
            message[0] +=     ('┌─────────┐ ')
            if card[0] == 'T':
                message[1] += ('│{:<2}       │ ').format(10)
            else:
                message[1] += ('│{:<2}       │ ').format(card[0])
            message[2] +=     ('│         │ ')
            message[3] +=     ('│    {}    │ '.format(card[1]))
            message[4] +=     ('│         │ ')
            if card[0] == 'T':
                message[5] += ('│       {:<2}│ ').format(10)
            else:
                message[5] += ('│       {:<2}│ ').format(card[0])
            message[6] +=     ('└─────────┘ ')
        if i+1 != len(hand):
            for j in range(7):
                message[j] += '| '

    for line in message:
        print(line)

def hit(hand):
    hand.append(drawCard(False) )

def playGame():
    shuffleDeck()
    dealHands()
    displayHands()
    giveOpitons()
    getPlayerChoice()
    executePlayerChoice()


playGame()


#----------------DEBUG------------------#
def testPrinting():
    message = ["", "", "", "", "", "", ""]
    message[0] +=  "┌── "
    message[1] += ("│{:<2}").format(10)
    message[2] += ("│   ")
    message[3] += ("│   ")
    message[4] += ("│   ")
    message[5] += ("│   ")
    message[6] += ("└── ")

    for line in message:
        print(line)

def testMultiPrinting():
    prettyPrintPlayerHand([['6♣', 'Q♦', '4♣'], ['4♣', 'T♦'], ['9♣', '5♦']])

def testDealerPrinting():
    prettyPrintDealerHand(['  ', 'Q♦'])



# testDealerPrinting()

# testMultiPrinting()

# testPrinting()

# print(('│{:<3} end').format("3♣"))
# print(('│{:<3} end').format("10♣"))
