from random import shuffle

class DeckOfCards:
    def __init__(self):
        self.__reset_deck()

    def __reset_deck(self):
        self.__deck = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for number in range(1, 14):
                card = (suit, number)
                self.__deck.append(card)
        shuffle(self.__deck)

    def deal(self, number_of_cards: int):
        hand = []
        for i in range(number_of_cards):
            hand.append(self.__deck.pop())
        return hand

if __name__ == "__main__":
    deck = DeckOfCards()
    hand1 = deck.deal(5)
    print(hand1)
    hand2 = deck.deal(5)
    print(hand2)
