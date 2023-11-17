favorite_numbers = {
    "lion eljhonson": [1, 7],
    'fulgrim': [3, 9],
    'perturabo': [4, 10],
    'jagathai khan': [5, 11], 
    'leman russ': [6, 12]
    }

for person in favorite_numbers:
    print(f"Name: {person.title()}")
    print("Favorite Numbers:")
    for number in favorite_numbers[person]:
        print(f"\t{number}")