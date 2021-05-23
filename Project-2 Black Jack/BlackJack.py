# global variables
import random
suits = ('Hearts' , 'Spades' , 'Clubs' , 'Diamonds')
ranks = ('Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' , 'Jack' , 'Queen' , 'King' , 'Ace')
values = {
    'Two' : 2 , 'Three' : 3 , 'Four' : 4 ,
    'Five' : 5 , 'Six' : 6 , 'Seven' : 7 ,
    'Eight' : 8 , 'Nine' : 9 , 'Ten' : 10,
    'Jack' : 10 , 'Queen' : 10 , 'King' : 10,
    'Ace' : 11
}

# required classes
class Card : 
    def __init__(self , suit , rank) :
        self.suit = suit
        self.rank = rank
        
    def __str__(self) :
        return f'[{self.rank} of {self.suit}]'

class Deck :
    def __init__(self) :
        self.cards = []
        
        for suit in suits :
            for rank in ranks :
                self.cards.append(Card(suit,rank))
    
    def shuffle(self) :
        random.shuffle(self.cards)
        
    def deal(self) :
        return self.cards.pop(0)

class Hand :
    def __init__(self) :
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self , card) :
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace' :
            self.aces += 1
        
    def adjust_for_ace(self) :
        # we will adjust ace value according to our requirement 
        # aces can have value either 1 or 11
        while self.value > 21 and self.aces :
            self.value -= 10
            self.aces -= 1

class Chips :
    def __init__(self , total = 100) :
        self.total = total 
        self.bet = 0
        
    def win_bet(self) :
        self.total += self.bet
    
    def lose_bet(self) :
        self.total -= self.bet

# game functions
def take_bet(chips) :
    
    while True :
        try :
            chips.bet = int(input('How many chips you will bet ? : '))
        except :
            print('Sorry... Bet should be a Number..')
        else :
            break

def hit(deck , hand) :
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck , hand) :
    global playing
    
    while True :
        x = input('Hit or Stand ? (H/S) : ')
        if x.lower() == 'h' :
            hit(deck , hand)
        elif x.lower() == 's' :
            print('Player Stands Dealers Turn')
            playing = False
        else :
            print('Sorry only H or S required..')
            continue
        break

def show_some(player , dealer) :
    
    print("\nDealer's Hand : ")
    print('First Card Hidden!')
    print(dealer.cards[1])
    
    print("\nPlayer's Hard : ")
    for card in player.cards :
        print(card)

def show_all(player , dealer) :
    print("\nDealer's Hand : ")
    for card in dealer.cards :
        print(card)
        
    print(f"Value of Dealer's Hand : {dealer.value}")
    
    print("\nPlayer's Hard : ")
    for card in player.cards :
        print(card)
    print(f"Value of Player's Hand : {player.value}")

def player_busts(player , dealer,chips) :
    print('BUST PLAYER!')
    chips.lose_bet()

def player_wins(player , dealer,chips) :
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player , dealer,chips) :
    print('PLAYER WINS! DEALER BUSTED')
    chips.win_bet()

def dealer_wins(player , dealer,chips) :
    print('BUST PLAYER! DEALER WINS')
    chips.lose_bet()

def push(player , dealer) :
    print('DEALER AND PLAYER TIE! Push...')

# game logic

playing = True
while True :

    print('Welcome To BlackJack')
    deck = Deck()
    deck.shuffle()
    
    #player hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    #dealer hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # initialising chips
    chips = Chips()
    
    take_bet(chips)
    
    show_some(player_hand , dealer_hand)
    
    while playing :
        hit_or_stand(deck , player_hand)
        
        show_some(player_hand , dealer_hand)
        
        if player_hand.value > 21 :
            player_busts(player_hand , dealer_hand , chips)
            
            break
    
    if player_hand.value <= 21 :
        
        while dealer_hand.value < 17 :
            hit(deck , dealer_hand)
            
        show_all(player_hand , dealer_hand)
        
        if dealer_hand.value > 21 :
            dealer_busts(player_hand , dealer_hand , chips)
        elif dealer_hand.value > player_hand.value :
            dealer_wins(player_hand , dealer_hand , chips)
        elif dealer_hand.value < player_hand.value :
            player_wins(player_hand , dealer_hand , chips)
        else :
            push(player_hand , dealer_hand)
            
        print(f'\nPlayer total chips : {chips.total}')
        
        
        new_game = input('Do you want a play another game ? (y/n) : ')
        if new_game[0].lower() == 'y' :
            playing = True
            continue
        else :
            print('Thank you for playing')
            playing = False
            break
    
    