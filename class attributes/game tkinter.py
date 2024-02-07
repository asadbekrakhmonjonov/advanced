import tkinter as tk
from tkinter import messagebox
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
            answer2 = random.choice(["rock", "paper", "scissors"])
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

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.rounds_label = tk.Label(master, text="Enter number of rounds:")
        self.rounds_label.pack()
        self.rounds_entry = tk.Entry(master)
        self.rounds_entry.pack()
        self.play_button = tk.Button(master, text="Play Game", command=self.play_game)
        self.play_button.pack()

    def play_game(self):
        rounds = int(self.rounds_entry.get())
        game = RockPaperScissors(rounds)
        game.play()
        messagebox.showinfo("Game Over", f"Player1: {game.wins1}\nPlayer2: {game.wins2}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()
