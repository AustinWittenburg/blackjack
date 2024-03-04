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

class Player(Hand):
    def __init__(self, money = None, bet = None):
        self.money = money or 500
        self.bet = bet or 10
        Hand.__init__(self)

    # def split(self, hand, dealer):
    #     tempHand1 = Hand([hand.cards[0]])
    #     tempHand2 = Hand([hand.cards[1]])
    #     dealer.dealCardTo(tempHand1)
    #     dealer.dealCardTo(tempHand2)
    #     self.hands.remove(hand)
    #     self.hands.append(tempHand1)
    #     self.hands.append(tempHand2)

deck = Deck()
deck.shuffle()

player1 = Player()
player1.addCardToHand(deck.deck.pop())
print(player1)

player2 = Player()
player2.addCardToHand(deck.deck.pop())
print(player2)
