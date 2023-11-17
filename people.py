surica = {
    'first_name': 'guilherme',
    'last_name': 'surica',
    'age': 19,
    'city': 'mogi guacu'
}

lollo = {
    'first_name': 'joao pedro',
    'last_name': 'lollo',
    'age': 20,
    'city': 'araras'
}

enache = {
    'first_name': 'henrique',
    'last_name': 'enache',
    'age': 19,
    'city': 'araras'
}

people = [surica, lollo, enache]

print("What I know about each one?")
for person in people:   
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")