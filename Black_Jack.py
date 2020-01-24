#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


# In[12]:


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + "of" + self.suit


# In[17]:


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has : " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# In[18]:


test_deck = Deck()
test_deck.shuffle()
print(test_deck)


# In[22]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passed in
        #from Deck.deal() --> Single Card(suit)
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        
        
        #if total value >21 then if we still have an ace
        #lower the value an ace by 10
        
        while self.value>21 and self.aces:
            self.value -= 10
            self.aces -= 1
            


# In[23]:


#testing
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
#hand the player a card from the deck
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
test_player.value


# In[24]:


class Chips:
    
    def __init__(self, total = 100):
        self.total = total   # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# In[25]:


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How many chips you want to bet? "))
        except:
            print("Sorry you have not entered the number of chips")
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have this many chips to bet: you have {} chips ".format(chips.total))
            else:
                break


# In[26]:


def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# In[28]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        x = input("Hit or Stand ? enter h and s ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)
            
        elif x[0].lower() == 's':
            print("Players stands dealer's turn")
            playing = False
            
        else:
            print("Sorry unable to understand enter h or s only! ")
            continue
            
        break


# In[35]:


def show_some(player,dealer):
    
    print("Dealers Hand")
    print("one card hidden")
    print(dealer.cards[1])
    print("\n")
    print("Players Hand")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    
    print("Dealer Hand")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Players Hand")
    for card in player.cards:
        print(card)


# In[36]:


def player_busts(player, dealer, chips):
    print("Player Busted")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Busted")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("Dealer Wins")
    chips.lose_bet()
    
def push(player, dealer):
    print("Dealer and Player tie! PUSH!")


# In[37]:


while True:
    # Print an opening statement
    
    print("Welcome To The World Of Black Jack")

    
    # Create & shuffle the deck, deal two cards to each player
    
    deck = Deck()
    deck.shuffle()
    
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    if player_hand.value < 21:
        
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
            
        # Show all cards
        
        show_all(player_hand, dealer_hand)
    
        # Run different winning scenarios
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(play_hand, player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            
        else:
            push(player_hand, dealer_hand)
    
    # Inform Player of their chips total 
    
    print("The total chips of the player is {}".format(player_chips.total))
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


# In[ ]:




