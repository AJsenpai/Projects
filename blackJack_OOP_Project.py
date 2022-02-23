# OOP Project - Black Jack
import random


class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit  # read only property no need setter

    @property
    def value(self):
        return self._value

    def show(self):
        print(f"{self._value} of {self._suit}")


class Deck:
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self):
        self._cards = []  # no getters or setters, handled internally
        self.build()

    def build(self):
        for suit in Deck.suits:
            for value in range(1, 12):
                self._cards.append(Card(suit, value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        for i in range(len(self._cards) - 1, 0, -1):
            rand = random.randint(0, i)
            self._cards[i], self._cards[rand] = self._cards[rand], self._cards[i]

    def draw(self):
        if self._cards:
            return self._cards.pop()


class Player:
    def __init__(self, name, is_dealer=False):
        self._name = name
        self._hand = []
        self._is_dealer = is_dealer

    @property
    def name(self):
        return self._name

    @property
    def is_dealer(self):
        return self._is_dealer

    def draw(self, deck):
        self._hand.append(deck.draw())
        return self  # return a reference to the instance that is calling the method

    def show_hand(self, reveal_card=False):
        if not self.is_dealer:
            for card in self._hand:
                card.show()
        else:
            for i in range(len(self._hand) - 1):
                self._hand[i].show()

            if reveal_card:
                self._hand[-1].show()
            else:
                print("X")

    def discard(self):
        return self._hand.pop()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card.value
        return value


class CardGame:
    INSTRUCTIONS = """\n | Welcome to our version of the Blackjack Game |
        =================================================================================
        The goal is to get as close to 21 as possible, without going over 21. 
        Each card has a value and a suit. The values are added for the final result.

        The game starts by dealing two cards to the player (you) and to the dealer.            
        You are playing against the dealer. On each turn, you must choose if you
        would like to take another card or stand to stop the game and see if you won.

        The game ends if the total value of the player's hand goes over 21,
        and if the total value of the hand is below 21, the game continues
        until the player chooses to stand.

        When the game ends or when the player chooses to stand,
        the total value of each hand is calculated.  
        The value that is closest to 21 without going over it wins the game.
        If the total value is over 21, the player or dealer automatically lose the game.
        =================================================================================
        """

    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.start_game()

    def start_game(self):
        print(CardGame.INSTRUCTIONS)
        turn = 1

        self.deck.shuffle()

        # draw two cards
        self.player.draw(self.deck).draw(self.deck)  # method chaining
        self.dealer.draw(self.deck).draw(self.deck)

        while True:
            print(f" == Turn #{turn} ==")
            print("\nThe Dealer's hand is:")
            self.dealer.show_hand()

            print("\nyour hand is:")
            self.player.show_hand()

            if self.player.get_hand_value() > 21:
                print("\nThe total value of your hand is over 21")
                break
            elif self.player.get_hand_value() == 21:
                break

            choice = self.ask_choice()
            turn += 1

            if choice == 1:
                self.player.draw(self.deck)
            else:
                break

        player_hand = self.player.get_hand_value()
        print("\nValue - Your hand :", player_hand)

        dealer_hand = self.dealer.get_hand_value()
        print("\nValue - Dealer's Hand:", dealer_hand)

        print("\nThe dealer's hand was:")
        self.dealer.show_hand(True)

        if player_hand > 21:
            print(f"\nYour lose, {self.player.name} you can play again")
        elif dealer_hand > 21 or player_hand == 21 or player_hand > dealer_hand:
            print(f"\nYour win, {self.player.name}! Congratulations")
        elif player_hand < dealer_hand:
            print(f"\nyour lose, {self.player.name}.. player again")
        else:
            print("we have a tie")

    def ask_choice(self):
        print("\nWhat do you want to do?")
        print("1- Ask for another card")
        print("2- stand")
        choice = int(input("please enter your choice 1 or 2 below:\n"))

        if choice == 1 or choice == 2:
            return choice
        else:
            print("The value was not valid , i will assume you choose 2")
            return 2


deck = Deck()
you = Player("jack")
dealer = Player("Dealer", True)

game = CardGame(deck, you, dealer)

