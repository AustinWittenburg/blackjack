import random

count = 0
numDecks = 4
suits = ['♠', '♦', '♥', '♣']
freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']
HiLo = [ ['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A'] ]
                #   2     3     4     5     6     7     8     9     10    A
basicStrategy = [ ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],  # 4
                  ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],  # 5
                  ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],  # 6
                  ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],  # 7
                  ['H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' ],  # 8
                  ['H',  'DH', 'DH', 'DH', 'DH', 'H',  'H',  'H',  'H',  'H' ],  # 9
                  ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H',  'H' ],  # 10
                  ['DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H' ],  # 11
                  ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],  # 12
                  ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],  # 13
                  ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'H',  'H' ],  # 14
                  ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'H',  'UH', 'H' ],  # 15
                  ['S',  'S',  'S',  'S',  'S',  'H',  'H',  'UH', 'UH', 'UH'],  # 16
                  ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],  # 17
                  ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],  # 18
                  ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],  # 19
                  ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ],  # 20
                  ['S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' ] ] # 21
minimum = 5
maximum = 100
playerCash = 500
playerBet = minimum
playerHand = []
splitHand = []
dealerHand = []
dealerShows = []
gameState = None
evalMessage = ''
playerScore = 0
numChoices = 0

# Calculates the computer's choice
def computerChoice(playerVal, dealerVal):
    global basicStrategy
    choice = basicStrategy[playerVal - 4][dealerVal - 2]
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

def evaluatePlayerChoice(playerChoice, comChoice):
    if playerChoice == 'h':
        return comChoice == 'hit'
    elif playerChoice == 's':
        return comChoice == 'stand'
    elif playerChoice == 'd':
        return comChoice == 'double otherwise hit' or comChoice == 'double otherwise stand'
    elif playerChoice == 'sp':
        return comChoice == 'split'
    elif playerChoice == 'su':
        return comChoice == 'surrender otherwise stand' or comChoice == 'surrender otherwise hit'
    else:
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
    hit(hand, deck)
    playerCash -= playerBet
    playerBet = playerBet * 2
    gameState = 'double'

# Splits the players hand into two
def split(deck):
    global playerHand
    global splitHand
    if (playerHand[0][0] == playerHand[1][0]) and (len(playerHand) == 2):
        splitHand.append(playerHand.pop() )
        playerHand.append(drawFrom(deck, True) )
        splitHand.append(drawFrom(deck, True) )
    else:
        print("You cannot split with your current hand")

def surrender():
    global gameState 
    gameState = 'surrender'

# Ends the players turn
def stand():
    global gameState 
    gameState = 'stand'

# Checks if the player has Blackjack
def playerHasBlackjack():
    global playerHand
    if cardValue(playerHand[0]) == 10 and cardValue(playerHand[1]) == 11:
        return True
    if cardValue(playerHand[1]) == 10 and cardValue(playerHand[0]) == 11:
        return True
    return False

# Checks if the player has busted
def playerBust():
    global playerHand
    return handValue(playerHand) > 21

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

# Plays one hand of Blackjack
def playHand(deck):
    global gameState
    global playerHand
    global dealerHand
    global playerCash
    global playerBet
    global evalMessage
    global playerScore
    global numChoices
    global count
    dealFrom(deck)
    dealerShows = dealerHand[:]
    dealerShows[0] = '  '    
    playerCash -= playerBet
    playerChoice = ''
    while not (playerBust() or (gameState == 'stand') or (gameState == 'double') or (gameState == 'surrender') or (handValue(playerHand) == 21) ):
        print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerShows) ) )
        print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
        comChoice = computerChoice(handValue(playerHand), cardValue(dealerHand[1]))
        playerChoice = input("Do you want to:\n\t(H)it\n\t(S)tand\n\t(D)ouble\n\t(Sp)lit\n\t(Su)rrender\n")
        if   playerChoice.lower() == 'h':
            hit(playerHand, deck)
        elif playerChoice.lower() == 's':
            stand()
        elif playerChoice.lower() == 'd':
            double(playerHand, deck)
        elif playerChoice.lower() == 'sp':
            split(deck)
        elif playerChoice.lower() == 'su':
            surrender()
        elif playerChoice.lower() == 'q' or playerChoice.lower() == 'quit' or playerChoice.lower() == 'exit':
            quit()
        else:
            print("Invalid input")
        if evaluatePlayerChoice(playerChoice, comChoice):
            evalMessage = "Correct"
            playerScore += 1
        else:
            evalMessage = "Wrong you're supposed to " + comChoice
        numChoices += 1

    HiLoCount(dealerHand[0])

    if playerBust():
        print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerHand) ) )
        print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
        print("\n####################################################\n##################### You Bust #####################\n####################################################\n")
    elif gameState == 'surrender':
        winnings = playerBet/2
        print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
        print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
        print("\n####################################################\n#################### Surrender #####################\n####################################################\n")
        playerCash += winnings
    else:
        playDealer(deck)
        if playerHasBlackjack() and (handValue(dealerHand) != 21):
            winnings = ( (3 / 2) * playerBet) + playerBet
            print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
            print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
            print("\n####################################################\n#################### Blackjack! ####################\n####################################################\n")
            playerCash += winnings
        elif dealerBust() or (handValue(dealerHand) < handValue(playerHand) ):
            winnings = 2 * playerBet
            print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
            print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
            print("\n####################################################\n##################### You Win ######################\n####################################################\n")
            playerCash += winnings
        elif handValue(dealerHand) == handValue(playerHand):
            winnings = playerBet
            print("Dealer:\t\t\tCount: {}\t${:.2f} + ${:.2f}\n{}".format(count, playerCash, winnings, prettyPrintHand(dealerHand) ) )
            print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
            print("\n####################################################\n################### It's a Push ####################\n####################################################\n")
            playerCash += winnings
        else:
            print("Dealer:\t\t\tCount: {}\t${:.2f}\n{}".format(count, playerCash, prettyPrintHand(dealerHand) ) )
            print("Player:\t\t\tBet: ${:.2f}\t\t{}\n{}".format(playerBet, evalMessage, prettyPrintHand(playerHand) ) )
            print("\n####################################################\n##################### You Lose #####################\n####################################################\n")

def playDealer(deck):
    global dealerHand
    while handValue(dealerHand) < 17:
        hit(dealerHand, deck)



def reset():
    global playerHand
    global splitHand
    global dealerHand
    global gameState
    global playerBet
    global minimum
    global evalMessage
    playerHand = []
    splitHand = []
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
    split(deck)
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

# print(computerChoice(11, 8))

# print(evaluatePlayerChoice('h', 'surrender'))

# simulateHand()

# print(prettyPrintHand(['6♣', 'A♦', 'T♥', 'K♠', '  ']))
