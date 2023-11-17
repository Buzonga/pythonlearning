favorite_places = {
    'david': ['quarto', 'sala', 'fac'],
    'surica': ['praia', 'parques', 'quarto'],
    'gabriel': ['quarto', 'loja de jogos', 'eventos de jogos / rpg'],
    'rick': ['quarto', 'casa', 'mercado']
}

for person in favorite_places:
    print(f"Name: {person.title()}")
    print("Favorite Places:")
    for place in favorite_places[person]:
        print(f"\t{place.title()}")