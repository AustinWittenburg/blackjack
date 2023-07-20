import random

freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']
basicStrategy = [ [ ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 4
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 5
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 6
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 7
                    ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],    # 8
                    ['H',  'DH', 'DH', 'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],    # 9
                    ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H',  'H' ],    # 10
                    ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H' ],    # 11
                    ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],    # 12
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

deck = []
timesSplit = 0
currentHand = 0
splitHandsPlayed = 0
canSurrender = True
count = 0
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
evalMessage = ""
playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
playerChoice = ""
possibleOptions = []
playerCash = 500
playerBet = 5
playerHands = [] # [ [card0, card1], [card0, card1] ] Multiple hands are optional
playerOutcomes = []
dealerHand  = [] #   [card0, card1]
dealerShows = []
numDecks = 5
outcomeMessage = ""
standHelper = True

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
    global evalMessage, playerChoice
    if playerChoice != "":
        comChoice = computerChoice(playerHands[currentHand], cardValue(dealerHand[1]) )
        if evaluatePlayerChoice(playerChoice, comChoice, playerHands[currentHand]):
            evalMessage = "Correct"

        else:
            evalMessage = "Wrong you're supposed to " + comChoice
    playerChoice = ""

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
    if len(playerOutcomes) < len(playerHands):
        userInput = input()
        if userInput == "q" or userInput == "quit" or userInput == "exit":
            exit()
        if userInput == "":
            userInput = "Stand"
        else:
            playerChoice = possibleOptions[int(userInput) - 1]

def computerChoice(hand, dealerVal):
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
    if playerChoice == "Hit":
        hit(hand)
    if playerChoice == "Stand" and standHelper:
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

def playerHasBlackjack():
    if currentHand >= len(playerHands):
        return False
    if cardValue(playerHands[currentHand][0]) == 10 and cardValue(playerHands[currentHand][1]) == 11:
        return True
    if cardValue(playerHands[currentHand][1]) == 10 and cardValue(playerHands[currentHand][0]) == 11:
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
    return cardValue(hand[0]) == cardValue(hand[1]) and len(hand) == 2 and timesSplit < 3

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

def prettyPrintPlayerHand(hand): # [ [card0, card1], [card0, card1], ... ]
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
            message[j] += '|  '
    
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

def printOutcomes():
    for i in range(len(playerOutcomes)):
        outcome = playerOutcomes[i]
        if outcome == "Blackjack":
            if dealerHasBlackjack():
                printPush(playerHands[i])
            else:
                printBlackjack(playerHands[i])
        if outcome == "Bust":
            printBust(playerHands[i])
        if outcome == "Surrender":
            printSurrender(playerHands[i])
        if outcome == None:
            dealerScore = handValue(dealerHand)
            playerScore = handValue(playerHands[i])
            if playerScore == dealerScore:
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
    outcomeMessage += ("{:*^" + str(length) + "}  ").format("Bust")

def printWin(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}  ").format("Win")

def printLose(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}  ").format("Lose")

def printPush(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}  ").format("Push")

def printBlackjack(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}  ").format("BlackJack")

def printSurrender(hand):
    global outcomeMessage
    length = len(hand) * 3 + 3
    outcomeMessage += ("{:*^" + str(length) + "}  ").format("Surrender")

# ---------Player Options----------
def hit(hand):
    hand.append(drawCard(False) )
    if playerBust(hand):
        if len(playerOutcomes) < len(playerHands):
            playerOutcomes.append("Bust")
        stand()
    else:
        playHand()

def stand():
    global currentHand, splitHandsPlayed, playerChoice, standHelper
    # playerChoice = ""
    if currentHand + 1 == len(playerHands) and len(playerOutcomes) < len(playerHands):
        if not playerBust(playerHands[currentHand]):
            playerOutcomes.append(None)
            standHelper = False
        return
    if len(playerOutcomes) < len(playerHands):
        playerOutcomes.append(None)
        currentHand += 1
        splitHandsPlayed += 1

    playHand()

def double(hand):
    global playerBet
    playerCash - playerBet
    playerBet = playerBet * 2
    hand.append(drawCard(False) )
    if playerBust(hand):
        playerOutcomes.append("Bust")
        stand()
    playerOutcomes.append(None)

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
    playerHands.append(tempHand2)
    playerHands.append(tempHand1)
    playerHands.remove(hand)
    playHand()

def surrender():
    global playerCash
    playerOutcomes.append(None)
    playerCash += playerBet/2
    stand()

def playDealerHand():
    global dealerShows
    HiLoCount(dealerHand[0])
    dealerShows = dealerHand
    while handValue(dealerHand) < 17:
        dealerHand.append(drawCard(False))

def playHand():
    global currentHand, standHelper
    displayHands()
    if playerHasBlackjack():
        currentHand += 1
        playerOutcomes.append("Blackjack")
        playHand()
        return
    elif currentHand < len(playerHands):
        giveOpitons(playerHands[currentHand])
        getPlayerChoice()
        executePlayerChoice(playerHands[currentHand])
        standHelper = True

def reset():
    global timesSplit, currentHand, splitHandsPlayed, evalMessage, playerOptions, playerChoice, outcomeMessage
    global possibleOptions, playerCash, playerBet, playerHands, dealerHand, dealerShows, playerOutcomes
    timesSplit = 0
    currentHand = 0
    splitHandsPlayed = 0
    evalMessage = ""
    playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
    playerChoice = ""
    outcomeMessage = ""
    possibleOptions = []
    playerCash = 500
    playerBet = 5
    playerHands = []
    playerOutcomes = []
    dealerHand  = []
    dealerShows = []

def playGame():
    shuffleDeck()
    while len(deck) > 10:
        dealHands()
        playHand()
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

def testingSplitBlackjack():
    global deck
    deck = ['A♦', '3♦', 'A♥', '8♦', 'Q♦', '7♦', '5♦', 'K♦', '2♦', '8♦', 'T♦']
    deck.reverse()
    while len(deck) > 10:
        dealHands()
        playHand()
        playDealerHand()
        displayHands()
        printOutcomes()
        input("Continue?")
        reset()

def testSpecificHand():
    global deck, playerHands, dealerHand, dealerShows
    deck = ['5♦', 'J♦', '5♦', 'K♦', '2♦', '8♦', 'T♦', '7♦', '5♦', 'K♦', '2♦', '8♦', 'T♦']
    deck.reverse()
    playerHands = [['T♦', '2♥']]
    dealerHand = ['J♦', '3♦']
    dealerShows = dealerHand[:]
    dealerShows[0] = '  '
    playHand()
    playDealerHand()
    displayHands()
    printOutcomes()
    input("Continue?")
    reset()

# testDealerPrinting()

# testMultiPrinting()

# testPrinting()

# testingSplitBlackjack()

# testSpecificHand()

# print(('│{:<3} end').format("3♣"))
# print(('│{:<3} end').format("10♣"))

# length = 6
# outcomeMessage += ("{:*^" + str(length) + "}").format("Blackjack")
# print(outcomeMessage)
