import random

freshDeck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣', 'A♣',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠', 'A♠',
             '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦', 'A♦']

class Card:
    def __init__(self, card):
        value, suit = card
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value}{self.suit}"

class Deck:
    def __init__(self):
        self.deck = []

    def shuffle(self, numDecks = 1):
        for i in range(numDecks):
            for c in freshDeck:
                card = Card(c)
                self.deck.append(card)
        random.shuffle(self.deck)

class Hand:
    def __init__(self, cards = None):
        self.hand = cards or []

    def __repr__(self):
        return str(self.hand)
    
    def addCardToHand(self, card):
        self.hand.append(card)

    def discard(self, card):
        self.hand.remove(card)

    def clearHand(self):
        self.hand = []

    def hasSingleHand(self):
        return not isinstance(self.hand[0], Hand)

class Player(Hand):
    def __init__(self, money = None, bet = None):
        self.money = money or 500
        self.bet = bet or 10
        Hand.__init__(self)

class Dealer(Hand, Deck):
    def __init__(self):
        Hand.__init__(self)
        Deck.__init__(self)

    def dealCardTo(self, player):
        player.addCardToHand(self.deck.pop())
    
    def split(self, player):
        if player.hasSingleHand():
            tempHand1 = Hand([player.hand[0]])
            tempHand2 = Hand([player.hand[1]])
            self.dealCardTo(tempHand1)
            self.dealCardTo(tempHand2)
            player.hand = [tempHand1, tempHand2]
        else:
            currentHand = 1
            tempHand1 = Hand([player.hand[currentHand].hand[0]])
            tempHand2 = Hand([player.hand[currentHand].hand[1]])
            self.dealCardTo(tempHand1)
            self.dealCardTo(tempHand2)
            player.hand.remove(player.hand[currentHand])
            player.hand.insert(currentHand, tempHand2)
            player.hand.insert(currentHand, tempHand1)
            
player = Player()
dealer = Dealer()
dealer.shuffle()

dealer.dealCardTo(player)
dealer.dealCardTo(dealer)
dealer.dealCardTo(player)
dealer.dealCardTo(dealer)

print(player)
# print(dealer)

dealer.split(player)
print(player)
# print(dealer)

dealer.split(player)
print(player)
# print(dealer)
