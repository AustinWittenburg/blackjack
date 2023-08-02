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
                  [ [ ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 4
                    [ ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 5
                    [ ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 6
                    [ ['H', f],    ['DH', 18],  ['DH', 13],  ['DH', 10],  ['DH', 10],  ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 7
                    [ ['DH', 13],  ['DH', 9],   ['DH', 6],   ['DH', 3],   ['DH', 3],   ['DH', 15],  ['H', f],   ['H', f],   ['H', f],   ['H', f] ],    # 8
                    [ ['DH', 1],   ['DH', 0],   ['H', -3],   ['H', -5],   ['H', -6],   ['DH', 3],   ['DH', 8],  ['H', f],   ['H', f],   ['H', f] ],    # 9
                    [ ['H', -11],  ['H', -12],  ['H', -13],  ['H', -15],  ['H', -16],  ['H', -7],   ['H', -4],  ['H', -1],  ['DH', 3],  ['DH', 2] ],   # 10
                    [ ['H', -15],  ['H', -16],  ['H', -18],  ['H', -19],  ['H', -20],  ['H', -11],  ['H', -7],  ['H', -5],  ['H', -5],  ['H', -3] ],   # 11
                    [ ['S', 4],    ['S', 3],    ['S', 1],    ['H', -1],   ['H', -3],   ['H', f],    ['H', f],   ['H', f],   ['H', f],   ['S', 21] ],   # 12
                    [ ['H', 0],    ['H', -1],   ['H', -3],   ['H', -5],   ['H', -7],   ['H', f],    ['H', f],   ['H', f],   ['S', 23],  ['S', 13] ],   # 13
                    [ ['H', -3],   ['H', -5],   ['H', -6],   ['H', -7],   ['H', -10],  ['S', 16],   ['S', 20],  ['S', 15],  ['S', 11],  ['S', 8] ],    # 14
                    [ ['H', -5],   ['H', -7],   ['H', -8],   ['H', -9],   ['H', -11],  ['S', 12],   ['S', 11],  ['S', 7],   ['S', 4],   ['S', 4] ],    # 15
                    [ ['H', -9],   ['H', -10],  ['H', -12],  ['H', -13],  ['H', -13],  ['S', 10],   ['S', 9],   ['S', 4],   ['S', 0],   ['S', 2]],     # 16
                    [ ['S', f],    ['S', f],    ['S', f],    ['H', -23],  ['H', -25],  ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['UH', -6] ],  # 17
                    [ ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ],    # 18
                    [ ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ],    # 19
                    [ ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ],    # 20
                    [ ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],    ['S', f],   ['S', f],   ['S', f],   ['S', f] ] ],  # 21
    # Soft Totals          2           3          4          5           6           7          8           9         10           A
                  [ [ ['DH', 11], ['DH', 7], ['DH', 2],  ['H', 0],   ['H', -1],  ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 13
                    [ ['DH', 14], ['DH', 7], ['DH', 2],  ['H', -2],  ['H', -3],  ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 14
                    [ ['DH', 22], ['DH', 9], ['DH', 1],  ['H', -4],  ['H', -7],  ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 15
                    [ ['DH', 19], ['DH', 6], ['DH', -1], ['H', -6],  ['H', -13], ['H', f],  ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 16
                    [ ['DH', 4],  ['H', -1], ['H', -6],  ['H', -12], ['H', -14], ['S', 14], ['H', f],   ['H', f],  ['H', f],   ['H', f] ],    # 17
                    [ ['DH', 3],  ['DH', 1], ['S', -7],  ['S', -9],  ['S', -12], ['S', f],  ['H', -18], ['H', f],  ['UH', 19], ['S', 6] ],    # 18
                    [ ['DH', 9],  ['DH', 5], ['DH', 3],  ['DH', 1],  ['DH', 0],  ['S', f],  ['S', f],   ['S', f],  ['S', f],   ['S', f] ],    # 19
                    [ ['DH', 10], ['DH', 8], ['DH', 6],  ['DH', 4],  ['DH', 4],  ['S', f],  ['S', f],   ['S', f],  ['S', f],   ['S', f] ],    # 20
                    [ ['S', f],   ['S', f],  ['S', f],   ['S', f],   ['S', f],   ['S', f],  ['S', f],   ['S', f],  ['S', f],   ['S', f] ] ],  # 21
    # Pairs               2           3           4          5          6          7           8          9         10          A
                  [ [ ['H', 12],  ['H', -1],  ['H', -5], ['H', -4], ['H', -5], ['P', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 2s
                    [ ['H', 14],  ['H', 4],   ['H', -1], ['H', -4], ['H', -4], ['H', 8],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 3s
                    [ ['H', f],   ['H', f],   ['H', f],  ['DH', 9], ['DH', 9], ['H', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 4s
                    [ ['DH', f],  ['DH', f],  ['DH', f], ['DH', f], ['DH', f], ['DH', f],  ['DH', f], ['DH', f], ['H', f],  ['H', f] ],     # 5s
                    [ ['H', 3],   ['H', 1],   ['H', -2], ['P', f],  ['P', f],  ['H', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 6s
                    [ ['H', -14], ['H', -12], ['P', f],  ['P', f],  ['P', f],  ['P', f],   ['H', f],  ['H', f],  ['H', f],  ['H', f] ],     # 7s
                    [ ['P', f],   ['P', f],   ['P', f],  ['P', f],  ['P', f],  ['P', f],   ['P', f],  ['H', 18], ['H', 6],  ['H', -1] ],    # 8s
                    [ ['S', -1],  ['S', -3],  ['S', -5], ['S', -6], ['S', -7], ['P', 5],   ['S', -7], ['S', -8], ['S', f],  ['P', 7] ],     # 9s
                    [ ['S', f],   ['S', f],   ['S', f],  ['P', 5],  ['P', 4],  ['S', f],   ['S', f],  ['S', f],  ['S', f],  ['S', f] ],     # 10s
                    [ ['P', f],   ['P', f],   ['P', f],  ['P', f],  ['P', f],  ['H', -10], ['H', -8], ['H', -8], ['H', -8], ['H', -7] ] ] ] # As

valueVariations = [ [ [5, 0], [5, 5], [6, 8], [6, 9], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [9, 0], [9, 1], [11, 8], [12, 7], [12, 8] ],
                    [],
                    [ [8, 3], [8, 4] ] ]

deck = []
timesSplit = 0
currentHand = 0
surrenderIndex = []
count = 0
trueCount = 0
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
evalMessage = ""
evalHand = []
playerOptions = ["Hit", "Stand", "Double", "Split", "Surrender"]
playerChoice = ""
possibleOptions = []
startingCash = 500
playerCash = 500
playerBet = 5
minBet = 5
maxBet = 50
currentHandBet = playerBet
playerHands = [] # [ [card0, card1], [card0, card1] ] Multiple hands are optional
dealerHand  = [] #   [card0, card1]
dealerShows = [] #   [' '  , card1]
outcomeMessage = ""
GREEN = '\033[92m'
RED = '\033[91m'
BOLD ='\033[1m'
ENDC = '\033[0m'
totalPlays = 0
correctPlays = 0
handsWon = 0
handsLost = 0
totalHands = 0
goToNextHand = False
trainingMode = False
valuedOnly = False

#-----------Game Rules-----------#
numDecks = 8
canSurrender = True

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
    global playerChoice, evalMessage, correctPlays, totalPlays
    userInput = input()
    if userInput == "q" or userInput == "quit" or userInput == "exit":
        exit()
    elif userInput == '' or int(userInput) > len(possibleOptions) or int(userInput) <= 0:
        displayHands()
        giveOpitons(playerHands[currentHand])
        getPlayerChoice()
    else:
        playerChoice = possibleOptions[int(userInput) - 1]
        comChoice = computerChoice(evalHand, cardValue(dealerHand[1]) )
        totalPlays += 1
        if evaluatePlayerChoice(playerChoice, comChoice, evalHand):
            evalMessage = GREEN + "Correct" + ENDC
            correctPlays += 1
        else:
            evalMessage = BOLD + "Wrong" + ENDC + " you're supposed to " + comChoice

def computerChoice(hand, dealerVal):
    if trainingMode:
        choice = computerChoiceVariations(hand, dealerVal)
    else:
        choice = computerChoiceBasic(hand, dealerVal)

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
    if playerCanSplit(hand):
        playerIndex = cardValue(hand[0]) - 2
        tableNum = 2

    elif playerHasSoftHand(hand):
        playerIndex = handValue(hand) - 13
        tableNum = 1

    else:
        playerIndex = handValue(hand) - 4
        tableNum = 0

    dealerIndex = dealerVal - 2
    isValue = [playerIndex, dealerIndex] in valueVariations[tableNum]
    if (valuedOnly and isValue) or (not valuedOnly):
        choice = determineVariation(playerIndex, dealerIndex, tableNum)
    else:    
        # Get the choice from the basic table
        choice = basicStrategy[tableNum][playerIndex][dealerIndex]
    
    
    return choice

def computerChoiceBasic(hand, dealerVal):
    if playerCanSplit(hand):
        choice = basicStrategy[2][cardValue(hand[0]) - 2][dealerVal - 2]
    elif playerHasSoftHand(hand):
        choice = basicStrategy[1][handValue(hand) - 13][dealerVal - 2]
    else:
        choice = basicStrategy[0][handValue(hand) - 4][dealerVal - 2]
    return choice

def determineVariation(playerIndex, dealerIndex, tableNum):
    global trueCount
    tableCount = basicStrategyVariations[tableNum][playerIndex][dealerIndex][1]
    estimatedNumDecks = round( (len(deck) / 52) * 2) / 2
    if estimatedNumDecks < 0.5:
        estimatedNumDecks = 0.5
    trueCount = int(count // estimatedNumDecks)
    if (tableCount >= 0 and trueCount >= tableCount) or (tableCount < 0 and trueCount <= tableCount):
        # Get the choice from the variations table
        choice = basicStrategyVariations[tableNum][playerIndex][dealerIndex][0]
    else:
        # Get the choice from the basic table
        choice = basicStrategy[tableNum][playerIndex][dealerIndex]
    return choice

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

#----------Computer Sim----------#
def giveSimulatedOpitons(hand):
    global possibleOptions
    possibleOptions = ["Hit", "Stand"]
    if playerCanDouble(hand):
        possibleOptions.append("Double")
    if playerCanSplit(hand):
        possibleOptions.append("Split")
    if playerCanSurrender():
        possibleOptions.append("Surrender")

def simulateComputer():
    # comChoice = computerChoiceBasic(evalHand, cardValue(dealerHand[1]) )
    comChoice = computerChoiceVariations(evalHand, cardValue(dealerHand[1]) )
    if comChoice == 'hit':
        return 'Hit'
    elif comChoice == 'surrender otherwise hit':
        if 'Surrender' in possibleOptions:
            return 'Surrender'
        else:
            return 'Hit'
    elif comChoice == 'double otherwise hit':
        if 'Double' in possibleOptions:
            return 'Double'
        else:
            return 'Hit'
    elif comChoice == 'double otherwise stand':
        if 'Double' in possibleOptions:
            return 'Double'
        else:
            return 'Stand'
    elif comChoice == 'stand':
        return 'Stand'
    elif comChoice == 'split':
        return 'Split'
    elif comChoice == 'surrender otherwise stand':
        if 'Surrender' in possibleOptions:
            return 'Surrender'
        else:
            return 'Stand'
    return 'Stand'

def executeComputerChoice():
    global playerChoice 
    playerChoice = simulateComputer()
    executePlayerChoice(playerHands[currentHand])

def playSimulatedHands():
    global currentHand, goToNextHand, evalHand
    while len(playerHands) > currentHand:
        evalHand = playerHands[currentHand]
        # displayHands()
        if playerHasBlackjack(currentHand):
            currentHand += 1
        else:
            giveSimulatedOpitons(playerHands[currentHand])
            executeComputerChoice()
        if goToNextHand:
            currentHand += 1
            goToNextHand = False

def runSimulation():
    global totalHands
    shuffleDeck()
    while len(deck) > 15:
        totalHands += 1
        dealHands()
        playSimulatedHands()
        playDealerHand()
        printSimulatedOutcomes()
        changeSimulatedBet()
        reset()

def changeSimulatedBet():
    global playerBet, trueCount
    estimatedNumDecks = round( (len(deck) / 52) * 2) / 2
    if estimatedNumDecks < 0.5:
        estimatedNumDecks = 0.5
    trueCount = int(count // estimatedNumDecks)
    if trueCount >= 1:
        if trueCount * minBet <= maxBet:
            playerBet = math.floor(trueCount) * minBet
        else: 
            playerBet = maxBet
    else:
        playerBet = minBet
    
def playFullSimulation(startingAmount, min, max, numShoes):
    global playerCash, playerBet, currentHandBet, startingCash, minBet, maxBet
    minBet = min
    maxBet = max
    playerCash = startingAmount
    playerBet = minBet
    currentHandBet = playerBet
    startingCash = playerCash
    while numShoes > 0:
        runSimulation()
        numShoes -= 1

def printSimulatedOutcomes():
    dealerScore = handValue(dealerHand)
    for i in range(len(playerHands)):
        playerScore = handValue(playerHands[i])
        if playerHasBlackjack(i):
            if dealerHasBlackjack():
                simulatePush()
            else:
                simulateBlackjack()
        elif i in surrenderIndex:
            simulateSurrender()
        elif playerBust(playerHands[i]):
            simulateBust()
        elif playerScore == dealerScore:
            simulatePush()
        elif playerScore > dealerScore or dealerBust():
            simulateWin()
        elif playerScore < dealerScore:
            simulateLose()

def simulateBust():
    global playerCash, handsLost
    handsLost += 1
    print(BOLD + RED + "Bust" + ENDC + "\t\tCash: {}\tBet: {}\tRunning Count: {}\tTrue Count: {}\tPercent Hands Won: {:%}".format(playerCash, playerBet, count, trueCount, handsWon/totalHands) )

def simulateWin():
    global playerCash, handsWon
    handsWon += 1
    playerCash += currentHandBet * 2
    print(BOLD + GREEN + "Win" + ENDC + "\t\tCash: {}\tBet: {}\tRunning Count: {}\tTrue Count: {}\tPercent Hands Won: {:%}".format(playerCash, playerBet, count, trueCount, handsWon/totalHands) )

def simulateLose():
    global playerCash, handsLost
    handsLost += 1
    print(BOLD + RED + "Lose" + ENDC + "\t\tCash: {}\tBet: {}\tRunning Count: {}\tTrue Count: {}\tPercent Hands Won: {:%}".format(playerCash, playerBet, count, trueCount, handsWon/totalHands) )

def simulatePush():
    global playerCash
    playerCash += currentHandBet
    print(BOLD + "Push" + ENDC + "\t\tCash: {}\tBet: {}\tRunning Count: {}\tTrue Count: {}\tPercent Hands Won: {:%}".format(playerCash, playerBet, count, trueCount, handsWon/totalHands) )

def simulateBlackjack():
    global playerCash, handsWon
    handsWon += 1
    playerCash += currentHandBet * 2.5
    print(BOLD + GREEN + "BlackJack" + ENDC + "\tCash: {}\tBet: {}\tRunning Count: {}\tTrue Count: {}\tPercent Hands Won: {:%}".format(playerCash, playerBet, count, trueCount, handsWon/totalHands) )

def simulateSurrender():
    global playerCash, handsLost
    handsLost += 1
    playerCash += currentHandBet/2
    print(BOLD + "Surrender" + ENDC + "\t\tCash: {}\tBet: {}\tRunning Count: {}\tTrue Count: {}\tPercent Hands Won: {:%}".format(playerCash, playerBet, count, trueCount, handsWon/totalHands) )

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
        if i == 0 and (sum + 11) <= 21: 
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
    return numAces > 0 and (numAces - 1) + softTotal < 11

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
    length = len(hand) * 4 + 2
    outcomeMessage += ("{:*^" + str(length + 13) + "} ").format(BOLD + RED + "Bust" + ENDC)

def printWin(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet * 2
    length = len(hand) * 4 + 2
    outcomeMessage += ("{:*^" + str(length + 13) + "} ").format(BOLD + GREEN + "Win" + ENDC)

def printLose(hand):
    global outcomeMessage
    length = len(hand) * 4 + 2
    outcomeMessage += ("{:*^" + str(length + 13) + "} ").format(BOLD + RED + "Lose" + ENDC)

def printPush(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet
    length = len(hand) * 4 + 2
    outcomeMessage += ("{:*^" + str(length + 8) + "} ").format(BOLD + "Push" + ENDC)

def printBlackjack(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet * 2.5
    length = len(hand) * 4 + 2
    outcomeMessage += ("{:*^" + str(length + 13) + "} ").format(BOLD + GREEN + "BlackJack" + ENDC)

def printSurrender(hand):
    global outcomeMessage, playerCash
    playerCash += currentHandBet/2
    length = len(hand) * 4 + 2
    outcomeMessage += ("{:*^" + str(length + 8) + "} ").format(BOLD + "Surrender" + ENDC)

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

def results():
    net = formatNet(playerCash - startingCash)
    print("{:#^48}".format(""))
    print("{:*^48}".format("SHUFFLING"))
    print("{:#^48}\n\n".format(""))
    print("Shoe Results:\n\tCash: ${:.2f}\n\tNet: {}\n\tPerformance: {}/{} Correct\n\n\n\n\n\n\n\n\n\n\n\n".format(playerCash, net, correctPlays, totalPlays))

def formatNet(net):
    if net >= 0:
        return GREEN + "+$" + ("{:.2f}").format(abs(net)) + ENDC
    elif net < 0:
        return RED + "-$" + ("{:.2f}").format(abs(net)) + ENDC

def playGame():
    # global deck
    start()
    shuffleDeck()
    # deck = ['6♣', '7♣', 'A♣', 'T♣', '3♣', 'Q♣', '7♣']
    while len(deck) > 15:
        dealHands()
        playHands()
        playDealerHand()
        displayHands()
        printOutcomes()
        changeBet(input("Continue?"))
        reset()
    results()

def start():
    global playerCash, playerBet, currentHandBet, trainingMode, startingCash
    playerCash = int(input("Starting Cash:\n"))
    playerBet = int(input("Starting Bet:\n"))
    currentHandBet = playerBet
    startingCash = playerCash
    trainingMode = input("Basic Strategy WITH Variations? Y/N\n")
    if trainingMode.lower() == 'y':
        trainingMode = True
        valuedOnly = input("Most Valuable Variations Only? Y/N\n")
        if valuedOnly.lower() == 'y':
            valuedOnly = True
        else:
            valuedOnly = False
    else:
        trainingMode = False

# playGame()

playFullSimulation(5000, 5, 50, 50)

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

def testSpecificHand():
    global deck
    deck = ['6♣', '7♣', '8♣', '9♣', 'A♣', 'A♣', 'A♣']
    dealHands()
    playHands()
    playDealerHand()
    displayHands()
    printOutcomes()

# print(GREEN + "+$" + ("{:.2f}").format(abs(0)) + ENDC)
# print(RED + "-$" + ("{:.2f}").format(abs(-62.50)) + ENDC)

# print(("{:*^" + str(12 + 9) + "}").format(RED + "Lose" + ENDC))

# evalMessage = GREEN + "Correct" + ENDC

# print("Player:\t\tBet: ${:.2f}\t{}".format(currentHandBet, evalMessage) )

# testDealerPrinting()

# testMultiPrinting()

# testPrinting()

# testSpecificHand()

# print(('│{:<3} end').format("3♣"))
# print(('│{:<3} end').format("10♣"))

# length = 6
# outcomeMessage += ("{:*^" + str(length) + "}").format("Blackjack")
# print(outcomeMessage)

# min = 5
# max = 50
# list = [i for i in range(min, max+1) if i % 5 == 0]
# print(list)

# count = 17
# estimatedNumDecks = round( (400 / 52) * 2) / 2
# trueCount = count // estimatedNumDecks

# print(trueCount)