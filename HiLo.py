import random

numberCards = [0,1,2,3,4,5,6,7,8,9]
symbolCards = ['+','-','/']
cardTiers = ['Gold', 'Silver', 'Bronze', 'Dirt']
specialCards = ['Root', 'Multiplication']

class Card:
    def __init__(self, type, value = None, tier = None, visibility = False):
        self.type = type 
        self.value = value     
        self.tier = tier
        self.visibility = visibility

    def __repr__(self):
        if self.type == "Number":
            return f" [{self.value} - {self.tier} - {self.visibility}]"
        return f" [{self.type}]"

class Deck:
    def __init__(self):
        self.cards = []
        self.makeDeck()
    
    def makeDeck(self):
        self.cards = []

        for i in range(11):
            for tier in cardTiers:
                newCard = Card(type = 'Number', value = i, tier = tier)
                self.cards.append(newCard)

        for i in range(4):
            self.cards.append(Card(type = 'Root'))
            self.cards.append(Card(type = 'Multiplication'))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
        
    def returnCard(self, card):
        self.cards.append(card)
        self.shuffle()

class Player:
    def __init__(self, playerName = 'N/A', chipCount = 100, isBot = True):
        self.playerName = playerName
        self.chipCount = chipCount
        self.isBot = isBot

        self.hand = []
        self.symbolCards = symbolCards

    def getCard(self, card, visibility = False):
        card.visibility = visibility
        self.hand.append(card)

    def newRound(self):
        self.hand = []
        self.symbolCards = symbolCards

    def __repr__(self):
        handDisplay = ""
            
        for card in self.hand:
            if card.visibility:
                handDisplay += str(card) + " "
            else:
                if self.isBot:
                    handDisplay += "[?] "
                else:
                    handDisplay += str(card) + "*"
            
        return f"{self.playerName}: {handDisplay}"

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.pot = 0
    
    def startRound(self):
        print("\n--- NEW ROUND STARTED ---")

        self.deck.makeDeck()
        self.deck.shuffle()

        for player in self.players:
            player.newRound()
            player.chipCount -= 1
        self.pot = len(self.players)

        self.hiddenCardRound()
        self.openCardRoundManager()

    def hiddenCardRound(self):
        print("\nDealing Hidden Cards...")

        for player in self.players:
            while True:
                card = self.deck.draw()
                
                if card.type == "Number":
                    player.getCard(card, visibility = False)
                    break
                else:
                    print(f"Dealer drew {card} for {player.playerName}'s hidden card. Discarding...")
                    self.deck.returnCard(card)

    def openCardRoundManager(self):

        print("\n--- Dealing Open Cards (2 per player) ---")  

        for i in range(2):
            print(f"\n> Dealing Open Card #{i+1}...")

            for player in self.players:
                self.openCardRound(player)          

    def openCardRound(self, player):
        card = self.deck.draw()
        player.getCard(card, visibility = True)

        if card.type in specialCards:
            print(f"-> {player.playerName} drew a {card.type}! Special rules trigger.")

            while True:
                additionalCard = self.deck.draw()
                if additionalCard.type == "Number":
                    print(f"   -> Extra card dealt: {additionalCard}")
                    player.getCard(additionalCard, visibility = True)
                    break
                else:
                    print(f"   -> Extra card was {additionalCard} (Symbol). Returning to deck and retrying...")
                    self.deck.returnCard(additionalCard)
            
            if card.type == "Multiplication":
                self.handleMultiplicationCard(player , card)

    def handleMultiplicationCard(self, player, multCard):  
        options = [op for op in player.symbolCards if op in ['+', '-']]
        options.append("Multiplication")
        
        choice = None

        if player.isBot:
            choice = random.choice(options)
        else:
            print(f"Your Hand: {player.hand}")
            print(f"Your Operators: {player.symbolCards}")
            print(f"You drew a MULT! You must discard '+', '-', or the 'MULT' card itself.")
            
            while choice not in options:
                userInput = input("Discard which? (+, -, MULT): ").strip().upper()
                if userInput in options:
                    choice = userInput
                else:
                    print(f"Invalid choice. Available options: {options}")

        print(f"   -> {player.playerName} chose to discard: {choice}")
        
        if choice == "Multiplication":
            if multCard in player.hand:
                player.hand.remove(multCard)
        else:
            player.symbolCards.remove(choice)

    """First Betting Round - Then Get 1 Last Card - Make Equations - Final Betting Round - Pick Hi-Lo - Win"""

    def dealOneCard(self):
            print("\n--- Dealing Final Card (1 per player) ---")
            for player in self.players:
                if player.hand:
                    self.openCardRound(player)
