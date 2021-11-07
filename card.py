"""
8/11/2021 - Time:
Gabriel S.J. Spadoni
spadoni.gabriel-TASK31-DLV01-INC01-SPOP-PROG-v0.1
This product is the first version of the python program of the SPOP (Small Proprietary Original Project). 
The SPOP is a simple one player game with fantasy elements. In this game, the user plays with a random 
generated deck of 20 offensive and defensive cards. The player starts at the first floor of a dungeon and 
will try to climb it. Each floor is constituted of one fight against an enemy. The enemy will attack and 
defend itself against the player using cards. If the player is able to win each single fight, he wins a game.
The program contains the different classes (Card, Deck, CardUser, Player, Enemy) as well as the main function
that is responsible of the CLI used to interact with the software.
"""

import random as rd


class Card:

    def __init__(self, name, type, health_effect, status_effect, text):
        self.name = name
        self.type = type
        self.health_effect = health_effect
        self.status_effect = status_effect
        self.text = text


class Deck:
    
    def __init__(self, offensive_cards, defensive_cards, max_cards=20):
        self.offensive_cards = offensive_cards
        self.defensive_cards = defensive_cards
        self.deck = []
        self.max_cards = max_cards
        self.isShuffled = False

    def createDeck(self):

        self.isShuffled = False
        
        n_offensive_cards = rd.randint(8, 12)
        n_defensive_cards = self.max_cards - n_offensive_cards

        for _ in range(n_offensive_cards):
            card = self.offensive_cards[rd.randint(0, len(self.offensive_cards) - 1)]
            self.deck.append(card)
        for card in range(n_defensive_cards):
            card = self.defensive_cards[rd.randint(0, len(self.defensive_cards) - 1)]
            self.deck.append(card)

    def shuffleDeck(self):
        self.isShuffled = True
        rd.shuffle(self.deck)
    
    
    def printDeck(self):
        n = 1
        for card in self.deck:
            print(n, card.name)
            n += 1


class CardUser:

    def __init__(self, hand, deck, health_points, status):
        self.hand = hand
        self.deck = deck
        self.health_points = health_points
    
    def showStatus(self):
        pass

    def useCard(self, card, target):
        pass


class Player(CardUser):
    pass



class Enemy(CardUser):
    pass

class Game:

    def __init__(self):
        pass
    pass

offensive_cards_dic = {
    0: Card("FireBall", "offensive", -5, "burn", "Inflict 5 damages to the targeted entity"),
    1: Card("Ice Spike", "offensive", -3, "freeze", "Inflict 3 damage to targeted entity") 
}

defensive_cards_dic = {
    0: Card("Heal", "defensive", +5, None, "Heal 5 health points to target"),
    1: Card("Block", "defensive", 6, "prevent", "Prevent next turn damage")
}


""" fireball = Card("FireBall", "offensive", -5, "burn", "Inflict 5 damages to the targeted entity")
ice_spike =  Card("Ice Spike", "offensive", -3, "freeze", "Inflict 3 damage to targeted entity")
heal = Card("Heal", "defensive", +5, None, "Heal 5 health points to target")
block = Card("Block", "defensive", 6, "prevent", "Prevent next turn damage")



deck = Deck([fireball, ice_spike], [heal, block])
deck.createDeck()
deck.shuffleDeck()
deck.printDeck()
"""
def main():
    quit = False
    isDeckCreated = False
    isDeckShuffled = False
    isGameStarted = False
    
    print("--- Welcome in the SPOP of Gabriel S.J. Spadoni ---")
    print("--- Type help to display the available commands and their description ---")

    while not quit:
        
        command = input("--- Type your command --- ")

        if command == 'quit':
            quit = True
        elif command == 'help':
            print("--- Commands are: ---")
            print("--- createDeck: creates a deck of random cards taken from the card pool ---")
            print("--- showDeck: shows the cards in the deck --- ")
            print("--- shuffleDeck: shuffles the deck --- ")
            print("--- quit: quit the software --- ")
        elif command == 'createDeck':
            deck = Deck(offensive_cards_dic, defensive_cards_dic)
            deck.createDeck()
            print("--- Deck Created! --- ")
            isDeckCreated = True
        elif command == 'showDeck':
            if isDeckCreated:
                print("--- Deck contains --- ")
                deck.printDeck()
            else:
                print('--- Deck not created! --- ')
        elif command == 'shuffleDeck':
            if isDeckCreated:
                deck.shuffleDeck()
                isDeckShuffled = True
                print('--- Deck succesfuly shuffled! --- ')
            else:
                print('--- Deck not created! --- ')
        else:
            print("--- Unknown Command. Try again! --- ")
            

main()