favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': 'c',
    'edward': ['rust', 'go'],
    'phill': ['python', 'haskell'],
    'mark': []
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

