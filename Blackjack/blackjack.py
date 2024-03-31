import random

count = 0
numDecks = 4
suits = ['♠', '♦', '♥', '♣']
freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
    # Hard Totals     2     3     4     5     6     7     8     9     10    A
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

minimum = 5
maximum = 100
playerCash = 500
playerBet = minimum
playerHand = []
splitHands = []
dealerHand = []
dealerShows = []
gameState = None
evalMessage = ''
playerScore = 0
numChoices = 0
timesSplit = 0
surrender = True

# Calculates the computer's choice
def computerChoice(hand, dealerVal):
    global basicStrategy
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
        return playerChoice == '1'
    elif comChoice == 'surrender otherwise hit':
        if playerCanSurrender():
            return playerChoice == '2'
        else:
            return playerChoice == '1'
    elif comChoice == 'double otherwise hit':
        if playerCanDouble(hand):
            return playerChoice == '3'
        else:
            return playerChoice == '1'
    elif comChoice == 'double otherwise stand':
        if playerCanDouble(hand):
            return playerChoice == '3'
        else:
            return playerChoice == '2'
    elif comChoice == 'stand':
        return playerChoice == '2'
    elif comChoice == 'split':
        return playerChoice == '4'
    elif comChoice == 'surrender otherwise stand':
        if playerCanSurrender():
            return playerChoice == '5'
        else:
            return playerChoice == '2'
    return False

# Shuffles a new deck depending on how many decks are being played with
def shuffleDeck():
    result = []
    for i in range(numDecks):
        result += freshDeck
    random.shuffle(result)
    return result

# Updates the count according to the HiLo system
def HiLoCount(card):
    global count
    global HiLo
    if card[0] in HiLo[0]:
        count += 1
    elif card[0] in HiLo[2]:
        count -= 1

# Draws and returns the next card in the deck then updates the count
def drawFrom(deck, updateCount):
    card = deck.pop()
    if updateCount:
        HiLoCount(card)
    return card

# Deals the starting hand
def dealFrom(deck):
    global playerHand
    global dealerHand
    playerHand.append(drawFrom(deck, True) )
    dealerHand.append(drawFrom(deck, False) )
    playerHand.append(drawFrom(deck, True) )
    dealerHand.append(drawFrom(deck, True) )

# Adds one card to the players hand
def hit(hand, deck):
    hand.append(drawFrom(deck, True) )

# Doubles the players bet, gives them one more card, and prevents them from hitting again
def double(hand, deck):
    global gameState
    global playerBet
    global playerCash
    if playerCanDouble(hand):
        hit(hand, deck)
        playerCash -= playerBet
        playerBet = playerBet * 2
        gameState = 'double'
    else:
        print("You cannot double with your current hand")

# Splits the players hand into two
def split(deck, hand):
    global timesSplit
    global splitHands # [ ['9♥', 'T♥'], ['9♠', '8♠'] ]
    global gameState
    tempHand1 = []
    tempHand2 = []
    if playerCanSplit(hand):
        if hand in splitHands:
            handCopy = hand[:]
            splitHands.remove(hand)
        else:
            handCopy = hand[:]
        tempHand1.append(handCopy.pop() )
        tempHand2.append(handCopy.pop() )
        tempHand1.append(drawFrom(deck, True) )
        tempHand2.append(drawFrom(deck, True) )
        splitHands.append(tempHand1)
        splitHands.append(tempHand2)
        gameState = 'split'
        timesSplit += 1
    else:
        print("You cannot split with your current hand")

def surrender():
    global gameState 
    gameState = 'surrender'

# Ends the players turn
def stand():
    global gameState 
    gameState = 'stand'

def playerHasSoftHand(hand):
    numAces = 0
    for card in hand:
        if card[0] == 'A':
            numAces += 1
    return numAces == 1

def playerCanSplit(hand):
    global timesSplit
    return hand[0][0] == hand[1][0] and len(hand) == 2 and timesSplit < 3

def playerCanDouble(hand):
    return len(hand) == 2

def playerCanSurrender():
    global surrender
    return surrender

# Checks if the player has Blackjack
def playerHasBlackjack():
    global playerHand
    if cardValue(playerHand[0]) == 10 and cardValue(playerHand[1]) == 11:
        return True
    if cardValue(playerHand[1]) == 10 and cardValue(playerHand[0]) == 11:
        return True
    return False

# Checks if the player has busted
def playerBust(hand):
    return handValue(hand) > 21

# Checks if the dealer has busted
def dealerBust():
    global dealerHand
    return handValue(dealerHand) > 21

# Returns the value of a given card
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

# Calculate the value of a hand
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

# Prints the current hand passed to it
def printHand(hand):
    message = "Hand: "
    for card in hand:
        message += card + " "
    message += "\tValue: " + str(handValue(hand) )
    return message

def playOutSplitHands(deck):
    global splitHands
    global gameState
    global playerHand
    global dealerHand
    global playerCash
    global playerBet
    global evalMessage
    global playerScore
    global numChoices
    global count
    playerChoice = ''
    hand = splitHands[-1]
    finishedHands = []
    while splitHands:
        while not (playerBust(hand) or (gameState == 'stand') or (gameState == 'double') or (gameState == 'surrender') or (handValue(hand) == 21) ):
            print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerShows) ) )
            print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
            comChoice = computerChoice(hand, cardValue(dealerHand[1]))
            playerChoice = input("Do you want to:\n\t1. Hit\n\t2. Stand\n\t3. Double\n\t4. Split\n\t5. Surrender\n")
            if evaluatePlayerChoice(playerChoice, comChoice, hand):
                evalMessage = "Correct"
                playerScore += 1
            else:
                evalMessage = "Wrong you're supposed to " + comChoice
            numChoices += 1
            if   playerChoice == '1':
                hit(hand, deck)
            elif playerChoice == '2':
                stand()
            elif playerChoice == '3':
                double(hand, deck)
            elif playerChoice == '4':
                split(deck, hand)
                playOutSplitHands(deck)
            elif playerChoice == '5':
                surrender()
            elif playerChoice.lower() == 'q' or playerChoice.lower() == 'quit' or playerChoice.lower() == 'exit':
                quit()
            else:
                print("Invalid input")
        finishedHands.append(hand)
        splitHands.pop()
        if splitHands:
            hand = splitHands[-1]
            gameState = None
    for h in finishedHands:
        printResult(deck, h)


def playOutHand(deck):
    global gameState
    global playerHand
    global dealerHand
    global playerCash
    global playerBet
    global evalMessage
    global playerScore
    global numChoices
    global count
    playerChoice = ''

    while not (playerBust(playerHand) or (gameState == 'stand') or (gameState == 'double') or (gameState == 'surrender') or (handValue(playerHand) == 21) ):
        print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerShows) ) )
        print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
        comChoice = computerChoice(playerHand, cardValue(dealerHand[1]))
        playerChoice = input("Do you want to:\n\t1. Hit\n\t2. Stand\n\t3. Double\n\t4. Split\n\t5. Surrender\n")
        if evaluatePlayerChoice(playerChoice, comChoice, playerHand):
            evalMessage = "Correct"
            playerScore += 1
        else:
            evalMessage = "Wrong you're supposed to " + comChoice
        numChoices += 1
        if   playerChoice == '1':
            hit(playerHand, deck)
        elif playerChoice == '2':
            stand()
        elif playerChoice == '3':
            double(playerHand, deck)
        elif playerChoice == '4':
            split(deck, playerHand)
            playOutSplitHands(deck)
            return
        elif playerChoice == '5':
            surrender()
        elif playerChoice.lower() == 'q' or playerChoice.lower() == 'quit' or playerChoice.lower() == 'exit':
            quit()
        else:
            print("Invalid input")
    printResult(deck, playerHand)
    

def printBust(hand):
    global playerCash
    global playerBet
    global evalMessage
    global count
    global dealerHand
    print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerHand) ) )
    print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
    print("\n####################################################\n##################### You Bust #####################\n####################################################\n")

def printSurrender(hand):
    global playerCash
    global playerBet
    global evalMessage
    global count
    global dealerHand
    winnings = playerBet/2
    print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
    print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
    print("\n####################################################\n#################### Surrender #####################\n####################################################\n")
    playerCash += winnings

def printBlackjack(hand):
    global gameState
    global playerCash
    global playerBet
    winnings = ( (3 / 2) * playerBet) + playerBet
    print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
    print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
    print("\n####################################################\n#################### Blackjack! ####################\n####################################################\n")
    playerCash += winnings

def printWin(hand):
    global gameState
    global playerCash
    global playerBet
    winnings = 2 * playerBet
    print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
    print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
    print("\n####################################################\n##################### You Win ######################\n####################################################\n")
    playerCash += winnings

def printPush(hand):
    global gameState
    global playerCash
    global playerBet
    winnings = playerBet
    print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
    print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
    print("\n####################################################\n################### It's a Push ####################\n####################################################\n")
    playerCash += winnings

def printLose(hand):
    global gameState
    global playerCash
    global playerBet
    print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerHand) ) )
    print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(hand) ) )
    print("\n####################################################\n##################### You Lose #####################\n####################################################\n")

def printResult(deck, hand):
    global gameState
    global playerCash
    global playerBet
    playerCash -= playerBet
    if playerBust(hand):
        printBust(hand)
    elif gameState == 'surrender':
        printSurrender(hand)
    else:
        playDealer(deck)
        if playerHasBlackjack() and (handValue(dealerHand) != 21):
            printBlackjack(hand)
        elif dealerBust() or (handValue(dealerHand) < handValue(hand) ):
            printWin(hand)
        elif handValue(dealerHand) == handValue(hand):
            printPush(hand)
        else:
            printLose(hand)

# Plays one hand of Blackjack
def playHand(deck):
    global playerHand
    global dealerHand
    global dealerShows
    global playerScore
    global numChoices
    
    dealFrom(deck)
    # dealerHand = ['9♠', '4♥']
    # playerHand = ['A♠', 'A♠']
    dealerShows = dealerHand[:]
    dealerShows[0] = '  '
    
    playOutHand(deck)
    
    HiLoCount(dealerHand[0])
    

def playDealer(deck):
    global dealerHand
    while handValue(dealerHand) < 17:
        hit(dealerHand, deck)

def reset():
    global timesSplit
    global playerHand
    global splitHands
    global dealerHand
    global gameState
    global playerBet
    global minimum
    global evalMessage
    timesSplit = 0
    playerHand = []
    splitHands = []
    dealerHand = []
    gameState = None
    playerBet = minimum
    evalMessage = ''

def playGame():
    global playerScore
    global numChoices
    global playerCash
    deck = shuffleDeck()
    while len(deck) > 10:
        playHand(deck)
        input("Contine?")
        reset()
    print(("You got {}/{} correct and ended with ${:.2f}").format(playerScore, numChoices, playerCash) )

def prettyPrintHand(hand): # ['6♣', 'Q♦',]
    message = ""
    for card in hand:
        message += ('┌─────────┐ ')
    message += ('\n')
    for card in hand:
        if card[0] == 'T':
            message += ('│{}       │ '.format(10))
        else:
            message += ('│{}        │ '.format(card[0]))
    message += ('\n')
    for card in hand:
        message += ('│         │ ')
    message += ('\n')
    for card in hand:
        message += ('│    {}    │ '.format(card[1]))
    message += ('\n')
    for card in hand:
        message += ('│         │ ')
    message += ('\n')
    for card in hand:
        if card[0] == 'T':
            message += ('│       {}│ '.format(10))
        else:
            message += ('│        {}│ '.format(card[0]))
    message += ('\n')
    for card in hand:
        message += ('└─────────┘ ')
    return message

playGame()

#----------------DEBUG------------------#
def simulateFullDeck():
    global count
    deck = shuffleDeck()
    while len(deck) > 0:
        card = drawFrom(deck, True)
        print(str(len(deck)) + " Card drawn: " + card + "\t Count is now:" + str(count))

def simulateSplit():
    global playerHand
    global splitHand
    deck = shuffleDeck()
    playerHand = ['9c', '8s']
    split(deck, playerHand)
    print(playerHand, splitHand)

def simulateHit():
    global playerHand
    deck = shuffleDeck()
    playerHand = ['9c', '8s']
    hit(deck)
    print(playerHand)

def simulateHandValue():
    hand1 = ['As', '3c', '5d'] # 19
    hand2 = ['As', 'Ad', 'Ah'] # 13
    hand3 = ['Kh', 'Jc', '7c'] # 27
    hand4 = ['Ad', 'Th']       # 21
    print(handValue(hand1), handValue(hand2), handValue(hand3), handValue(hand4))

def simulateHand():
    deck = shuffleDeck()
    playHand(deck)

# print(evaluatePlayerChoice('h', 'surrender'))

# simulateHand()

# print(prettyPrintHand(['6♣', 'A♦', 'T♥', 'K♠', '  ']))

