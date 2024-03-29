import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.value == '10':
            value_str = 'T'
        else:
            value_str = self.value
        return f"{value_str}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['♥', '♦', '♣', '♠']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                num_aces += 1
                value += 11
            else:
                value += int(card.value)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

class Player:
    def __init__(self):
        self.hand = Hand()
        self.split_hand = None
    
    def hit(self, card):
        self.hand.add_card(card)
    
    def get_hand_value(self):
        return self.hand.get_value()

    def split(self):
        self.split_hand = Hand()
        self.split_hand.add_card(self.hand.cards.pop())

class Dealer:
    def __init__(self):
        self.hand = Hand()
    
    def hit(self, card):
        self.hand.add_card(card)
    
    def get_hand_value(self):
        return self.hand.get_value()
    
    def should_hit(self):
        return self.get_hand_value() < 17

def print_card(card):
    value_str = card.value    
    suit_str = card.suit

    print("┌─────────┐ ")
    print(f"│{value_str:<2}       │")
    print("│         │")
    print(f"│    {suit_str}    │")
    print("│         │")
    print(f"│       {value_str:<2}│")
    print("└─────────┘ ")

def print_face_down():
    print("┌─────────┐")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("│░░░░░░░░░│")
    print("└─────────┘")

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
    
    def deal_initial(self):
        self.player.hit(self.deck.deal_card())
        self.dealer.hit(self.deck.deal_card())
        self.player.hit(self.deck.deal_card())
        self.dealer.hit(self.deck.deal_card())
    
    def player_turn(self):
        print("Dealer's hand:")
        print_card(self.dealer.hand.cards[0])
        print_face_down()
        print("Player's hand:")
        for card in self.player.hand.cards:
            print_card(card)
        print("Player's total value:", self.player.get_hand_value())
        
        while self.player.get_hand_value() < 21:
            actions = ['h', 's']
            if len(self.player.hand.cards) == 2 and self.player.hand.cards[0].value == self.player.hand.cards[1].value:
                actions.append('p')
                action = input("Do you want to hit, stand, or split? (h/s/p): ").strip().lower()
            elif '10' in [card.value for card in self.player.hand.cards]:
                actions.append('p')
                action = input("Do you want to hit, stand, or split? (h/s/p): ").strip().lower()
            else:
                action = input("Do you want to hit or stand? (h/s): ").strip().lower()
            if action in actions:
                if action == 'h':
                    self.player.hit(self.deck.deal_card())
                    print("Player's hand:")
                    for card in self.player.hand.cards:
                        print_card(card)
                    print("Player's total value:", self.player.get_hand_value())
                elif action == 's':
                    break
                elif action == 'p':
                    self.player.split()
                    self.player.hit(self.deck.deal_card())
                    self.player_turn()
                    break
            else:
                print("Invalid input, please try again.")
        
        print("Player's final hand:")
        for card in self.player.hand.cards:
            print_card(card)
        print("Player's final total value:", self.player.get_hand_value())
    
    def dealer_turn(self): 
        print("Dealer's total value:", self.dealer.get_hand_value())

        while self.dealer.should_hit():
            self.dealer.hit(self.deck.deal_card())
            print("Dealer's new hand:")
            for card in self.dealer.hand.cards:
                print_card(card)
            print("Dealer's new total value:", self.dealer.get_hand_value())

        print("Dealer's final hand:")
        for card in self.dealer.hand.cards:
            print_card(card)
        print("Dealer's final total value:", self.dealer.get_hand_value())
    
    def determine_winner(self):
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()
        if player_value > 21:
            print("Player busts! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
        elif player_value == dealer_value:
            print("It's a tie!")
        elif player_value > dealer_value:
            print("Player wins!")
        else:
            print("Dealer wins!")

    def play_game(self):
        print("Welcome to Blackjack!")
        self.deal_initial()
        self.player_turn()
        if self.player.get_hand_value() <= 21:
            self.dealer_turn()
            self.determine_winner()

game = Blackjack()
game.play_game()
