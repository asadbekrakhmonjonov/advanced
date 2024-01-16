class Series:
    def __init__(self, title: str, number_of_seasons: int, genre_list: list):
        self.title = title
        self.number_of_seasons = number_of_seasons
        self.genre_list = genre_list
        self.ratings = []
        self.average = 0

    def rate(self, rating: int):
        self.rating = rating
        self.ratings.append(rating)
        self.average = sum(self.ratings) / len(self.ratings)
        self.average = round(self.average, 1)

    def minimum_grade(self, rating: float):
        return self.average >= rating

    def includes_genre(self, genre: str):
        return genre in self.genre_list

    def __str__(self):
        genre_string = ", ".join(self.genre_list)
        return f"{self.title} ({self.number_of_seasons}) \n Genre: {genre_string}\n {len(self.ratings)} ratings, average {self.average} points"


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("Series with a minimum grade of 4.5:")
    for series in filter(lambda x: x.minimum_grade(4.5), series_list):
        print(series.title)

    print("Series with genre Comedy:")
    for series in filter(lambda x: x.includes_genre("Comedy"), series_list):
        print(series.title)
