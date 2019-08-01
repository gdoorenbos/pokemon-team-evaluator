
# if a multiplier is not given, it is assumed to be 1
type_strengths = {
    'normal': {
        'rock': 0.5,
        'ghost': 0,
        'steel': 0.5
    },
    'fire':
    'water':
    'electric':
    'grass':
    'ice':
    'fighting':
    'poison':
    'ground':
    'flying':
    'psychic':
    'bug':
    'rock':
    'ghost':
    'dragon':
    'dark':
    'steel':
    'fairy':
}

team = [
    ['water']
]

def print_team(team):
    for pokemon in team:
        print('types: {}'.format(pokemon))

def main():
    print_team(team)

main()
