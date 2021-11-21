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

# Class for cards, a card as a name, a type(offensive or defensive), health_effect, status_effect and the text which the decription of the card.
class Card:

    def __init__(self, name, type, health_effect, status_effect, text):
        self.name = name
        self.type = type
        self.health_effect = health_effect
        self.status_effect = status_effect
        self.text = text


    def describeCard(self):
        print(f' --- The card {self.name} is a {self.type}. --- \n --- {self.text} ---')

# Class for a deck, a deck is composed of offensive_cards, defensive_cards and has a max card.
# It also contains the deck which is a list and isShuffled.
# There are the functions createDeck, shuffleDeck and printDeck
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
        for _ in range(n_defensive_cards):
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
        
    def showDeck(self):
        pass

# Class CardUser is the class for player and enemies. A card user has a hand, a deck, health_points and a status.
# There are the functions showStatus which shows the health and the status and useCard that has 
class CardUser:

    def __init__(self):
        self.hand = []
        self.deck = []
        self.health_points = 20
        self.status_effect = None
    
    def showStatus(self):
        pass

    def useCard(self, card, target):
        pass

    def applyCardEffect(self, card, target):
        pass
    
    def removeCardFromHand(self, card):
        pass


# Class Player inherits from CardUser, however here with have a set health_points value
class Player(CardUser):
    
    def __init__(self, health_points = 20):
        super().__init__()
        self.health_points = health_points
    
    def giveDeck(self, deck):
        self.deck = deck

    pass


# Class Enemy inherist from CardUser
class Enemy(CardUser):
    pass


class Admin:
    pass


# Class Game will take care of the interactions of the user.
class Game:

    def __init__(self):

        self.player = None
        self.enemies = []
        self.current_floor = 0
        
        self.quit = False
        self.isDeckCreated = False
        self.isDeckShuffle = False
        self.isGameStarted = False
        self.isPlayerCreated = False
        self.isTypeUser = False
        self.commands = dict()

        self.offensive_cards_dic = {
            0: Card("FireBall", "offensive", -5, "burn", "Inflict 5 damages to the targeted entity"),
            1: Card("Ice Spike", "offensive", -3, "freeze", "Inflict 3 damage to targeted entity"),
            2: Card("Burn", "offensive", 0, "burn", "Inflict burning effect to the target") 
        }

        self.defensive_cards_dic = {
            0: Card("Heal", "defensive", +5, None, "Heal 5 health points to target"),
            1: Card("Block", "defensive", 6, "prevent", "Prevent next turn damage"),
            2: Card("Blessing", "defensive", 0, "bless", "Next healing will be doubled")
        }


    # Add a command manager with commands dic. To have a single function that manages 
    # Main process of the CLI.
    def main(self):
        
        
        print("--- Welcome in the SPOP of Gabriel S.J. Spadoni ---")
        print("--- Type help to display the available commands and their description ---")
        print("--- Enter your user type ---")

        while not self.isTypeUser:
            command = input("--- Type your command --- ")

            if command == 'player':
                player = Player()
                self.isPlayerCreated = True
                self.isTypeUser = True
            elif command == 'admin':
                print("---  admin not supported --- ")
            else:
                print('--- Enter your user type: player or admin ---')

        while not self.quit:
            
            command = input("--- Type your command --- ")

            command = command.split(' ')


            if command[0] == 'quit':
                self.quit = True
            elif command[0] == 'help':
                print("--- Commands are: ---")
                print("--- createDeck: creates a deck of random cards taken from the card pool ---")
                print("--- showDeck: shows the cards in the deck --- ")
                print("--- shuffleDeck: shuffles the deck --- ")
                print("--- quit: quit the software --- ")
            elif command[0] == 'createDeck':
                deck = Deck(self.offensive_cards_dic, self.defensive_cards_dic)
                deck.createDeck()
                print("--- Deck Created! --- ")
                self.isDeckCreated = True
            elif command[0] == 'showDeck':
                if self.isDeckCreated:
                    print("--- Deck contains --- ")
                    deck.printDeck()
                else:
                    print('--- Deck not created! --- ')
            elif command[0] == 'shuffleDeck':
                if self.isDeckCreated:
                    deck.shuffleDeck()
                    self.isDeckShuffled = True
                    print('--- Deck succesfuly shuffled! --- ')
                else:
                    print('--- Deck not created! --- ')
            elif command[0] == 'startGame':
                if self.isDeckCreated and self.isDeckShuffled and self.isPlayerCreated:
                    player.giveDeck(deck)
                    print('--- The game has started! --- ')
                    self.isGameStarted = True
                else:
                    print("--- Game can't be started ---")
            elif command[0] == 'describeCard':
                try: 
                    asked_card_name = command[1]
                    set_of_cards = set(deck.deck)
                    
                except:
                    print("--- no card given ---")
            else:
                print("--- Unknown Command. Try again! --- ")
            

    
    
    def startFight(self, player, enemy):
        pass

    def processTurn(self): #possibility will modidy the RAD, as it introduces further concept of turn.
        pass
    

game = Game()

game.main()