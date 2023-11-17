nina = {
    'name': 'nina',
    'age': 7,
    'species': 'dog',
    'race': 'none',
    'owner': 'ana'
}

luigi = {
    'name': 'luigi',
    'age': 10,
    'species': 'dog',
    'race': 'daschrund',
    'owner': 'miriam'
}

gatao = {
    'name': 'gatao',
    'age': 13,
    'species': 'cat',
    'race': 'black',
    'owner': 'gabriel'
}

pets = [nina, luigi, gatao]

for pet in pets:
    print(f"Pet Name: {pet['name'].title()}")
    print(f"\tAge: {pet['age']} years old")
    print(f"\tSpecies: {pet['species'].title()}")
    print(f"\tRace: {pet['race'].title()}")
    print(f"\tOwner Name: {pet['owner'].title()}")