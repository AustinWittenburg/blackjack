import random
import math

freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']

f = math.inf

basicStrategy = [ 
    # Hard Totals     2     3     4     5     6     7     8     9     10    A
                  [ ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 4
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 5
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 6
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 7
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 8
                    ['H',  'DH', 'DH', 'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 9
                    ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H',  'H' ],    # 10
                    ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H' ],    # 11
                    ['H',  'H',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],    # 12
                    ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],    # 13
                    ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],    # 14
                    ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'UH', 'H' ],    # 15
                    ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'UH', 'UH', 'UH'],    # 16
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 17
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 18
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 19
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 20
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ] ],  # 21
    # Soft Totals     2     3     4     5     6     7     8     9     10    A
                  [ ['H',  'H',  'H',  'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 13
                    ['H',  'H',  'H',  'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 14
                    ['H',  'H',  'DH', 'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 15
                    ['H',  'H',  'DH', 'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 16
                    ['H',  'DH', 'DH', 'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 17
                    ['S',  'DS', 'DS', 'DS', 'DS', 'S',  'S',  'H',  'H',  'H' ],    # 18
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 19
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 20
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ] ],  # 21
    # Pairs           2     3     4     5     6     7     8     9     10    A
                  [ ['P',  'P',  'P',  'P',  'P',  'P',  'H',  'H',  'H',  'H' ],    # 2s
                    ['P',  'P',  'P',  'P',  'P',  'P',  'H',  'H',  'H',  'H' ],    # 3s
                    ['H',  'H',  'H',  'P',  'P',  'H',  'H',  'H',  'H',  'H' ],    # 4s
                    ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H',  'H' ],    # 5s
                    ['P',  'P',  'P',  'P',  'P',  'H',  'H',  'H',  'H',  'H' ],    # 6s
                    ['P',  'P',  'P',  'P',  'P',  'P',  'H',  'H',  'H',  'H' ],    # 7s
                    ['P',  'P',  'P',  'P',  'P',  'P',  'P',  'P',  'P',  'P' ],    # 8s
                    ['P',  'P',  'P',  'P',  'P',  'S',  'P',  'P',  'S',  'S' ],    # 9s
                    ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],    # 10s
                    ['P',  'P',  'P',  'P',  'P',  'P',  'P',  'P',  'P',  'P' ] ] ] # As

                                #-------------Variations-------------#
basicStrategyVariations = [
    # Hard Totals        2            3            4            5            6            7            8           9          10           A
                  [ [['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 4
                    [['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 5
                    [['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 6
                    [['H', f],    ['DH', 18],  ['DH', 13],  ['DH', 10],  ['DH', 10],  ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 7
                    [['DH', 13],  ['DH', 9],   ['DH', 6],   ['DH', 3],   ['DH', 3],   ['DH', 15],  ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 8
                    [['DH', 1],   ['DH', 0],   ['H', -3],   ['H', -5],   ['H', -6],   ['DH', 3],   ['DH', 8],  ['H', f],   ['H', f],   ['H', f] ],    # 9
                    [['H', -11],  ['H', -12],  ['H', -13],  ['H', -15],  ['H', -16],  ['H', -7],   ['H', -4],  ['H', -1],  ['DH', 3],  ['DH', 2] ],   # 10
                    [['H', -15],  ['H', -16],  ['H', -18],  ['H', -19],  ['H', -20],  ['H', -11],  ['H', -7],  ['H', -5],  ['H', -5],  ['H', -3] ],   # 11
                    [['S', 4],    ['S', 3],    ['S', 1],    ['H', -1],   ['H', -3],   ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['S', 21] ],   # 12
                    [['H', 0],    ['H', -1],   ['H', -3],   ['H', -5],   ['H', -7],   ['H', f],    ['H', f],   ['H', f],   ['S', 23],  ['S', 13] ],   # 13
                    [['H', -3],   ['H', -5],   ['H', -6],   ['H', -7],   ['H', -10],  ['S', 16],   ['S', 20],  ['S', 15],  ['S', 11],  ['S', 8] ],    # 14
                    [['H', -5],   ['H', -7],   ['H', -8],   ['H', -9],   ['H', -11],  ['S', 12],   ['S', 11],  ['S', 7],   ['S', 4],   ['S', 4] ],    # 15
                    [['H', -9],   ['H', -10],  ['H', -12],  ['H', -13],  ['H', -13],  ['S', 10],   ['S', 9],   ['S', 4],   ['S', 0],   ['S', 2]],     # 16
                    [['S', f],    ['S', f],    ['S', f],    ['H', -23],  ['H', -25],  ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['UH', -6] ],  # 17
                    [['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ],    # 18
                    [['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ],    # 19
                    [['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ],    # 20
                    [['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ] ],  # 21
    # Soft Totals         2           3          4          5           6           7          8           9         10           A
                  [ [['DH', 11], ['DH', 7], ['DH', 2],  ['H', 0],   ['H', -1],  ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 13
                    [['DH', 14], ['DH', 7], ['DH', 2],  ['H', -2],  ['H', -3],  ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 14
                    [['DH', 22], ['DH', 9], ['DH', 1],  ['H', -4],  ['H', -7],  ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 15
                    [['DH', 19], ['DH', 6], ['DH', -1], ['H', -6],  ['H', -13], ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 16
                    [['DH', 4],  ['H', -1], ['H', -6],  ['H', -12], ['H', -14], ['S', 14], ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 17
                    [['DH', 3],  ['DH', 1], ['S', -7],  ['S', -9],  ['S', -12], ['S', f],  ['H', -18], ['H', f],  ['UH', 19], ['S', 6] ],    # 18
                    [['DH', 9],  ['DH', 5], ['DH', 3],  ['DH', 1],  ['DH', 0],  ['S', f],  ['S', f],   ['S', f],  ['S', f],   ['S', f] ],    # 19
                    [['DH', 10], ['DH', 8], ['DH', 6],  ['DH', 4],  ['DH', 4],  ['S', f],  ['S', f],   ['S', f],  ['S', f],   ['S', f] ],    # 20
                    [['S', f],   ['S', f],  ['S', f],   ['S', f],   ['S', f],   ['S', f],  ['S', f],   ['S', f],  ['S', f],   ['S', f] ] ],  # 21
    # Pairs              2           3           4          5          6          7           8          9         10          A
                  [ [['H', 12],  ['H', -1],  ['H', -5], ['H', -4], ['H', -5], ['P', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 2s
                    [['H', 14],  ['H', 4],   ['H', -1], ['H', -4], ['H', -4], ['H', 8],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 3s
                    [['H', f],   ['H', f],   ['H', f],  ['DH', 9], ['DH', 9], ['H', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 4s
                    [['DH', f],  ['DH', f],  ['DH', f], ['DH', f], ['DH', f], ['DH', f],  ['DH', f], ['DH', f], ['H', f],  ['H', f] ],     # 5s
                    [['H', 3],   ['H', 1],   ['H', -2], ['P', f],  ['P', f],  ['H', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 6s
                    [['H', -14], ['H', -12], ['P', f],  ['P', f],  ['P', f],  ['P', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 7s
                    [['P', f],   ['P', f],   ['P', f],  ['P', f],  ['P', f],  ['P', f],   ['P', f],  ['H', 18], ['H', 6],  ['H', -1] ],    # 8s
                    [['S', -1],  ['S', -3],  ['S', -5], ['S', -6], ['S', -7], ['P', 5],   ['S', -7], ['S', -8], ['S', f],  ['P', 7] ],     # 9s
                    [['S', f],   ['S', f],   ['S', f],  ['P', 5],  ['P', 4],  ['S', f],   ['S', f],  ['S', f],  ['S', f],  ['S', f] ],     # 10s
                    [['P', f],   ['P', f],   ['P', f],  ['P', f],  ['P', f],  ['H', -10], ['H', -8], ['H', -8], ['H', -8], ['H', -7] ] ] ] # As

deck = []
timesSplit = 0
currentHand = 0
canSurrender = True
surrenderIndex = []
count = 0
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
evalMessage = ""
evalHand = []
playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
playerChoice = ""
possibleOptions = []
playerCash = 500
playerBet = 5
currentHandBet = playerBet
playerHands = [] # [ [card0, card1], [card0, card1] ] Multiple hands are optional
dealerHand  = [] #   [card0, card1]
dealerShows = [] #   [' '  , card1]
numDecks = 5
outcomeMessage = ""
goToNextHand = False
trainingMode = False

#-------------Setup--------------#
def shuffleDeck():
    global deck
    for _ in range(numDecks):
        deck += freshDeck
    random.shuffle(deck)

def dealHands():
    global dealerShows, playerCash
    newHand = []
    newHand.append(drawCard(False) )
    dealerHand.append(drawCard(True) ) # Don't update count on dealers down card
    newHand.append(drawCard(False) )
    dealerHand.append(drawCard(False) )
    playerCash -= playerBet
    playerHands.append(newHand)
    dealerShows = dealerHand[:]
    dealerShows[0] = '  '

def drawCard(DealerDownCard):
    card = deck.pop()
    if not DealerDownCard:
        HiLoCount(card)
    return card

def displayHands():
    print("Dealer:\t\tCount: {}\t${:.2f}".format(count, playerCash) )
    prettyPrintDealerHand(dealerShows)
    print("Player:\t\tBet: ${:.2f}\t{}".format(currentHandBet, evalMessage) )
    prettyPrintPlayerHand(playerHands)

def giveOpitons(hand):
    global possibleOptions
    possibleOptions = ["Hit", "Stand"]
    if playerCanDouble(hand):
        possibleOptions.append("Double")
    if playerCanSplit(hand):
        possibleOptions.append("Split")
    if playerCanSurrender():
        possibleOptions.append("Surrender")
    displayOptions()

def displayOptions():
    optionNum = 0
    for option in possibleOptions:
        optionNum += 1
        print("\t{}. {}".format(optionNum, option))
    for _ in range(5 - len(possibleOptions)):
        print()

#-----------Evaluation-----------#
def getPlayerChoice():
    global playerChoice, evalMessage
    userInput = input()
    if userInput == "q" or userInput == "quit" or userInput == "exit":
        exit()
    elif userInput == '':
        displayHands()
        giveOpitons(playerHands[currentHand])
        getPlayerChoice()
    else:
        playerChoice = possibleOptions[int(userInput) - 1]
        comChoice = computerChoice(evalHand, cardValue(dealerHand[1]) )
        if evaluatePlayerChoice(playerChoice, comChoice, evalHand):
            evalMessage = "Correct"
        else:
            evalMessage = "Wrong you're supposed to " + comChoice

def computerChoice(hand, dealerVal):
    if trainingMode:
        choice = computerChoiceVariations(hand, dealerVal)
    else:
        if playerHasSoftHand(hand):
            choice = basicStrategy[1][handValue(hand) - 13][dealerVal - 2]
        elif playerCanSplit(hand):
            choice = basicStrategy[2][cardValue(hand[0]) - 2][dealerVal - 2]
        else:
            choice = basicStrategy[0][handValue(hand) - 4][dealerVal - 2]
    if choice == 'H':
        return 'hit'
    elif choice == 'UH':
        return 'surrender otherwise hit'
    elif choice == 'DH':
        return 'double otherwise hit'
    elif choice == 'DS':
        return 'double otherwise stand'
    elif choice == 'S':
        return 'stand'
    elif choice == 'P':
        return 'split'
    elif choice == 'US':
        return 'surrender otherwise stand'
    else:
        raise Exception("Error in calculating computerChoice")
    
def computerChoiceVariations(hand, dealerVal):
    
    pass
    
def evaluatePlayerChoice(playerChoice, comChoice, hand):
    if comChoice == 'hit':
        return playerChoice == 'Hit'
    elif comChoice == 'surrender otherwise hit':
        if playerCanSurrender():
            return playerChoice == 'Surrender'
        else:
            return playerChoice == 'Hit'
    elif comChoice == 'double otherwise hit':
        if playerCanDouble(hand):
            return playerChoice == 'Double'
        else:
            return playerChoice == 'Hit'
    elif comChoice == 'double otherwise stand':
        if playerCanDouble(hand):
            return playerChoice == 'Double'
        else:
            return playerChoice == 'Stand'
    elif comChoice == 'stand':
        return playerChoice == 'Stand'
    elif comChoice == 'split':
        return playerChoice == 'Split'
    elif comChoice == 'surrender otherwise stand':
        if playerCanSurrender():
            return playerChoice == 'Surrender'
        else:
            return playerChoice == 'Stand'
    return False

def executePlayerChoice(hand):
    # execute = {
    #     "Hit"       : print(hand),
    #     "Stand"     : stand(),
    #     "Double"    : double(hand),
    #     "Split"     : split(hand),
    #     "Surrender" : surrender()
    # }
    # execute[playerChoice]
    if playerChoice == "Hit":
        hit(hand)
    if playerChoice == "Stand":
        stand()
    if playerChoice == "Double":
        double(hand)
    if playerChoice == "Split":
        split(hand)
    if playerChoice == "Surrender":
        surrender()

def HiLoCount(card):
    global count
    if card[0] in HiLo[0]:
        count += 1
    elif card[0] in HiLo[2]:
        count -= 1

#----------Hand Checks-----------#
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

def playerHasBlackjack(handIndex):
    if cardValue(playerHands[handIndex][0]) == 10 and cardValue(playerHands[handIndex][1]) == 11:
        return True
    if cardValue(playerHands[handIndex][1]) == 10 and cardValue(playerHands[handIndex][0]) == 11:
        return True
    return False

def dealerHasBlackjack():
    if cardValue(dealerHand[0]) == 10 and cardValue(dealerHand[1]) == 11:
        return True
    if cardValue(dealerHand[1]) == 10 and cardValue(dealerHand[0]) == 11:
        return True
    return False

def playerHasSoftHand(hand):
    numAces = 0
    softTotal = 0
    for card in hand:
        if card[0] == 'A':
            numAces += 1
        else:
            softTotal += cardValue(card)
    return numAces == 1 and softTotal < 11

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

#---------Print Functions---------#
def prettyPrintDealerHand(hand): # ['6♣', 'Q♦']
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

def prettyPrintPlayerHand(hands): # [ [card0, card1], [card0, card1], ... ]
    message = ["", "", "", "", "", "", ""]

    for i in range(currentHand):
        for card in hands[i]:
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
            message[j] += '|  '
    
    # if splitHandsPlayed != 0:
    if currentHand > 0:
        for i in range(7):
            message[i] += ' '
    
    for i in range(currentHand, len(hands)):
        for card in hands[i]:
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
        if i+1 != len(hands):
            for j in range(7):
                message[j] += '| '

    for line in message:
        print(line)    

def printOutcomes():
    dealerScore = handValue(dealerHand)
    for i in range(len(playerHands)):
        playerScore = handValue(playerHands[i])
        if playerHasBlackjack(i):
            if dealerHasBlackjack():
                printPush(playerHands[i])
            else:
                printBlackjack(playerHands[i])
        elif i in surrenderIndex:
            printSurrender(playerHands[i])
        elif playerBust(playerHands[i]):
            printBust(playerHands[i])
        elif playerScore == dealerScore:
            printPush(playerHands[i])
        elif playerScore > dealerScore or dealerBust():
            printWin(playerHands[i])
        elif playerScore < dealerScore:
            printLose(playerHands[i])

    print(outcomeMessage)
    print("\n\n\n")

def printBust(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Bust")

def printWin(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet * 2
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Win")

def printLose(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Lose")

def printPush(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Push")

def printBlackjack(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet * 2.5
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("BlackJack")

def printSurrender(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet/2
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Surrender")

# ---------Player Options----------#
def hit(hand):
    hand.append(drawCard(False) )
    if playerBust(hand):
        stand()

def stand():
    global goToNextHand
    goToNextHand = True

def double(hand):
    global currentHandBet, playerCash
    playerCash -= currentHandBet
    currentHandBet = currentHandBet * 2
    hand.append(drawCard(False) )
    stand()

def split(hand):
    global currentHandBet, playerCash, timesSplit
    timesSplit += 1
    playerCash -= currentHandBet
    copy = hand[:]
    tempHand1 = []
    tempHand2 = []
    tempHand1.append(copy.pop() )
    tempHand2.append(copy.pop() )
    tempHand1.append(drawCard(False) )
    tempHand2.append(drawCard(False) )
    playerHands.remove(hand)
    playerHands.append(tempHand1)
    playerHands.append(tempHand2)

def surrender():
    global playerCash, surrenderIndex
    surrenderIndex.append(currentHand)
    stand()

def changeBet(playerInput):
    global playerBet
    try:
        float(playerInput)
        inputIsFloat = True
    except ValueError:
        inputIsFloat = False
    if inputIsFloat:
        playerBet = round(float(playerInput), 2)

def playDealerHand():
    global dealerShows
    HiLoCount(dealerHand[0])
    dealerShows = dealerHand
    while handValue(dealerHand) < 17:
        dealerHand.append(drawCard(False))

def playHands():
    global currentHand, goToNextHand, evalHand
    while len(playerHands) > currentHand:
        evalHand = playerHands[currentHand]
        displayHands()
        if playerHasBlackjack(currentHand):
            currentHand += 1
        else:
            giveOpitons(playerHands[currentHand])
            getPlayerChoice()
            executePlayerChoice(playerHands[currentHand])
        if goToNextHand:
            currentHand += 1
            goToNextHand = False

def reset():
    global timesSplit, currentHand, evalMessage, playerOptions, playerChoice, outcomeMessage, surrenderIndex
    global possibleOptions, playerBet, playerHands, dealerHand, dealerShows, currentHandBet
    timesSplit = 0
    currentHand = 0
    currentHandBet = playerBet
    surrenderIndex = []
    evalMessage = ""
    playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
    playerChoice = ""
    outcomeMessage = ""
    possibleOptions = []
    playerHands = []
    dealerHand  = []
    dealerShows = []

def playGame():
    # start()
    shuffleDeck()
    while len(deck) > 10:
        dealHands()
        playHands()
        playDealerHand()
        displayHands()
        printOutcomes()
        changeBet(input("Continue?"))
        reset()

def start():
    global playerCash, playerBet, currentHandBet, trainingMode
    playerCash = int(input("Starting Cash:\n"))
    playerBet = int(input("Starting Bet:\n"))
    currentHandBet = playerBet
    trainingMode = input("Basic Strategy WITH Variations? Y/N\n")
    if trainingMode.lower() == 'y':
        trainingMode = True
    else:
        trainingMode = False

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

# length = 6
# outcomeMessage += ("{:*^" + str(length) + "}").format("Blackjack")
# print(outcomeMessage)
