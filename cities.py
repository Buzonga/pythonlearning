cities = {
    'araras': {
        'country': 'brazil',
        'population': 130866,
        'fact': 'The name was given due to the number of the bird Arara in the region'
    },
    'campinas': {
        'country': 'brazil',
        'population': 1138309,
        'fact': 'Campinas is one of the most important technological centers of the country'
    },
    'amsterdam': {
        'country': 'netherlands',
        'population': 833989,
        'fact': 'The city is below sea level'
    }
}

for city, data in cities.items():
    print(f"City Name: {city.title()}")
    country = data['country']
    population = data['population']
    fact = data['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
      