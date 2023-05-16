import random

count = 0
num_decks = 2
deck = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac',
        '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah',
        '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As',
        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad']
HiLo = [['2', '3', '4', '5', '6'], ['7', '8', '9'], ['T', 'J', 'Q', 'K', 'A']]
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
    playerHand.append(drawFrom(deck))
    dealerHand.append(drawFrom(deck))
    playerHand.append(drawFrom(deck))
    dealerHand.append(drawFrom(deck))

# Adds one card to the players hand
def hit(deck):
    global playerHand
    playerHand.append(drawFrom(deck))

# Ends the players turn
def stand():
    global gameState 
    gameState = None # Update later

# Splits the players hand into two
def split(deck):
    global playerHand
    global splitHand
    if (playerHand[0][0] == playerHand[1][0]) & (len(playerHand) == 2):
        splitHand.append(playerHand.pop())
        playerHand.append(drawFrom(deck))
        splitHand.append(drawFrom(deck))
    else:
        print("You cannot split with your current hand")




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

# simulateHit()