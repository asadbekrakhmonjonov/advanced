def smallest_average(person1: dict, person2: dict, person3: dict):
    average_1 = (person1["result1"] + person1["result2"] +person1["result3"])/3
    average_2 = (person2["result1"] + person2["result2"] + person2["result3"])/3
    average_3 = (person3["result1"] + person3["result2"] + person3["result3"])/3
    if average_2 > average_1 < average_3:
        for key, values in person1.items():
            print(f"{key}:{values}")
    elif average_1 > average_2 <average_3:
        for key, values in person2.items():
            print(f"{key}:{values}")
    elif average_2 > average_3 < average_1:
        for key, values in person3.items():
            print(f"{key}:{values}")
if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))