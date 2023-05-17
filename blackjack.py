import random

count = 0
num_decks = 2
deck = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac',
        '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah',
        '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As',
        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad']
HiLo = [['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A']]
minimum = 5
maximum = 100
playerBet = minimum
playerHand = []
splitHand = []
dealerHand = []
gameState = None

# Shuffles a new deck depending on how many decks are being played with
def shuffleDeck():
    result = []
    for i in range(num_decks):
        result += deck
    random.shuffle(result)
    return result

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

# Updates the count according to the HiLo system
def HiLoCount(card):
    global count
    global HiLo
    if card[0] in HiLo[0]:
        count += 1
    elif card[0] in HiLo[2]:
        count -= 1

# Draws and returns the next card in the deck then updates the count
def drawFrom(deck):
    card = deck.pop()
    HiLoCount(card)
    return card

# Deals the starting hand
def dealFrom(deck):
    global playerHand
    global dealerHand
    playerHand.append(drawFrom(deck) )
    dealerHand.append(drawFrom(deck) )
    playerHand.append(drawFrom(deck) )
    dealerHand.append(drawFrom(deck) )
    print("Dealer Hand: [] " + dealerHand[1])

# Adds one card to the players hand
def hit(hand, deck):
    hand.append(drawFrom(deck) )

# Doubles the players bet, gives them one more card, and prevents them from hitting again
def double(hand, deck):
    global gameState
    hit(hand, deck)
    playerBet = playerBet * 2
    gameState = None # Update later

# Splits the players hand into two
def split(deck):
    global playerHand
    global splitHand
    if (playerHand[0][0] == playerHand[1][0]) and (len(playerHand) == 2):
        splitHand.append(playerHand.pop() )
        playerHand.append(drawFrom(deck) )
        splitHand.append(drawFrom(deck) )
    else:
        print("You cannot split with your current hand")

# Ends the players turn
def stand():
    global gameState 
    gameState = 'stand'

def playerHasBlackjack():
    global playerHand
    if cardValue(playerHand[0]) == 10 and cardValue(playerHand[1]) == 11:
        return True
    if cardValue(playerHand[1]) == 10 and cardValue(playerHand[0]) == 11:
        return True
    return False

def playerBust():
    global playerHand
    return handValue(playerHand) > 21

def dealerBust():
    global dealerHand
    return handValue(dealerHand) > 21

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

def printHand(hand):
    message = "Hand: "
    for card in hand:
        message += card + " "
    message += "\tValue: " + str(handValue(hand))
    return message

# Plays one hand of Blackjack
def playHand(deck):
    global gameState
    global playerHand
    global dealerHand
    dealFrom(deck)
        
    while (not playerBust()) and (gameState != 'stand') and (handValue(playerHand) != 21):
        print("Player " + printHand(playerHand) )
        playerChoice = input("Do you want to:\n\t(H)it\n\t(S)tand\n\t(D)ouble\n\t(Sp)lit\n")
        if   playerChoice.lower() == 'h':
            hit(playerHand, deck)
        elif playerChoice.lower() == 's':
            stand()
        elif playerChoice.lower() == 'd':
            double(playerHand, deck)
        elif playerChoice.lower() == 'sp':
            split(deck)
        else:
            print("Invalid input")
    if playerBust():
        print("You Bust")
    else:
        playDealer(deck)
        print("Player" + printHand(playerHand) )
        print("Dealer" + printHand(dealerHand) )
        if playerHasBlackjack() and (handValue(dealerHand) != 21):
            print("Blackjack!")
        elif dealerBust() or (handValue(dealerHand) < handValue(playerHand) ):
            print("You Win")
        elif handValue(dealerHand) == handValue(playerHand):
            print("It's a Push")
        else:
            print("You Lose")

def playDealer(deck):
    global dealerHand
    while handValue(dealerHand) < 17:
        hit(dealerHand, deck)
    



#----------------DEBUG------------------#
def simulateFullDeck():
    global count
    deck = shuffleDeck()
    while len(deck) > 0:
        card = drawFrom(deck)
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


simulateHand()
