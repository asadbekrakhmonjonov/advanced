import random


class WordGame:
    def __init__(self, rounds: int):
        self.rounds = rounds
        self.wins1 = 0
        self.wins2 = 0

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game: ")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
            winner = self.round_winner(answer1, answer2)
            if winner == 1:
                self.wins1 += 1
                print("player1 wins")
            elif winner == 2:
                self.wins2 += 1
                print("player2 wins")
            else:
                pass
        print("game over")
        print(f"player1: {self.wins1}")
        print(f"player2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return random.randint(1, 2)


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        self.vowels = ["a", "e", "i", "o", "u"]

    def round_winner(self, player1_word: str, player2_word: str):
        count1 = sum(1 for char in player1_word if char.lower() in self.vowels)
        count2 = sum(1 for char in player2_word if char.lower() in self.vowels)

        if count1 > count2:
            return 1
        elif count2 > count1:
            return 2
        else:
            return random.randint(1, 2)


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if player1_word == player2_word:
            return 0
        elif (player1_word == "rock" and player2_word == "scissors") or \
                (player1_word == "paper" and player2_word == "rock") or \
                (player1_word == "scissors" and player2_word == "paper"):
            return 1
        else:
            return 2


p = MostVowels(2)
p.play()
