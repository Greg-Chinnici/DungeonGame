types = [
    'death',
    'earth',
    'fire', 
    'ice',
    'lightning',
    'magic',
    'sand',
    'water',
    ]

themes = [
    'folklore',
    'greek',
    'historical',
    'medival',
    'pirate',
    'popCulture',
    'roman',
    'viking'
    ]

def sortLists():
    types.sort()
    themes.sort()

    for type in  types:
        print(f"\'{type}\',")

    for line in range(5):
        print('')
        
    for theme in  themes:
        print(f"\'{theme}\',")


coins = {"copper": 1,"silver": 5, "gold": 10}
GeneralLootTable = [coins] #isnt effected by type or theme

TimeBasedLootTable = {
    'day' : [],
    'night': ["Wendigo key"]
}

TypeLootTable = {
    'death': [],
    'earth': [],
    'fire': [],
    'ice': ['Yeti key'],
    'lightning': [],
    'magic': [],
    'sand': [],
    'water': ['Loviatar key', 'Neptune key']
}
ThemeLootTable = {
    'folklore': [],
    'greek': ['Ares key'],
    'historical': [],
    'medival': [],
    'pirate': [],
    'popCulture': [],
    'roman': [],
    'viking': []
}
