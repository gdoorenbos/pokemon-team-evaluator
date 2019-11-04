# pokemon-team-evaluator
# type chart: https://img.rankedboost.com/wp-content/uploads/2018/10/Pokemon-Lets-Go-Type-Chart.jpg

types = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost',
         'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon',
         'dark', 'fairy']

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
