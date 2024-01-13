book1 = {"name": "Atomic habits","year":2018, "author": "James clear"}
book2 = {"name": "Start with why","year": 2017,"author":"Simon Sinek"}
book2["year"] = 2018
for key,value in book1.items():
    print(f"{key}:{value}")
for key,value in book2.items():
    print(f"{key}:{value}")