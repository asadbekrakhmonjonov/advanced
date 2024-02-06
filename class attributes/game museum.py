class ComputerGame:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.list_games = []

    def add_game(self, game: ComputerGame):
        self.list_games.append(game)

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def __str__(self):
        result = ""
        for game in self.list_games:
            if game.year < 1990:
                result += f"{game.name}, {game.author} - {game.year}\n"
        return result if result else "No games found before 1990."

if __name__ == "__main__":
    museum = GameMuseum()
    museum.add_game(ComputerGame("Pacman", "Namco", 1980))
    museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
    museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
    print(museum)
