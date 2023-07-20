import random

freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']
deck = []
timesSplit = 0
currentHand = 0
canSurrender = True
surrenderIndex = []
count = 0
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
evalMessage = ""
playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
playerChoice = ""
possibleOptions = []
playerCash = 500
playerBet = 5
playerHands = [] # [ [card0, card1], [card0, card1] ] Multiple hands are optional
dealerHand  = [] #   [card0, card1]
dealerShows = [] #   [' '  , card1]
numDecks = 5
outcomeMessage = ""
goToNextHand = False

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

def displayHands():
    print("Dealer:\t\t\tCount: {}\t${:.2f}".format(count, playerCash) )
    prettyPrintDealerHand(dealerShows)
    print("Player:\t\t\tBet: ${:.2f}\t\t{}".format(playerBet, evalMessage) )
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

def getPlayerChoice():
    global playerChoice
    userInput = input()
    if userInput == "q" or userInput == "quit" or userInput == "exit":
        exit()
    elif userInput == '':
        displayHands()
        giveOpitons(playerHands[currentHand])
        getPlayerChoice()
    else:
        playerChoice = possibleOptions[int(userInput) - 1]

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

def playerHasMoreHands():
    return currentHand + 1 < len(playerHands)

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

def printOutcomes(): # Change to calculate outcomes based on each individual hand
    dealerScore = handValue(dealerHand)
    for i in range(len(playerHands)):
        playerScore = handValue(playerHands[i])
        if playerHasBlackjack(i):
            if dealerHasBlackjack():
                printPush(playerHands[i])
            else:
                printBlackjack(playerHands[i])
        if i in surrenderIndex:
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
    playerCash += playerBet * 2
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Win")

def printLose(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Lose")

def printPush(hand):
    global outcomeMessage, playerCash
    playerCash += playerBet
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Push")

def printBlackjack(hand):
    global outcomeMessage, playerCash
    playerCash += playerBet * 2.5
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("BlackJack")

def printSurrender(hand):
    global outcomeMessage, playerCash
    playerCash += playerBet/2
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}").format("Surrender")

# ---------Player Options----------
def hit(hand):
    hand.append(drawCard(False) )
    if playerBust(hand):
        stand()

def stand():
    global goToNextHand
    goToNextHand = True

def double(hand):
    global playerBet, playerCash
    playerCash -= playerBet
    playerBet = playerBet * 2
    hand.append(drawCard(False) )
    stand()

def split(hand):
    global playerBet, playerCash
    playerCash -= playerBet
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

def playDealerHand():
    global dealerShows
    HiLoCount(dealerHand[0])
    dealerShows = dealerHand
    while handValue(dealerHand) < 17:
        dealerHand.append(drawCard(False))

def playHands():
    global currentHand, goToNextHand
    while len(playerHands) > currentHand:
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
    global possibleOptions, playerBet, playerHands, dealerHand, dealerShows
    timesSplit = 0
    currentHand = 0
    surrenderIndex = []
    evalMessage = ""
    playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
    playerChoice = ""
    outcomeMessage = ""
    possibleOptions = []
    playerBet = 5
    playerHands = []
    dealerHand  = []
    dealerShows = []

def playGame():
    shuffleDeck()
    while len(deck) > 10:
        dealHands()
        playHands()
        playDealerHand()
        displayHands()
        printOutcomes()
        input("Continue?")
        reset()


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
