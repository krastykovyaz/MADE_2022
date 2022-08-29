from itertools import permutations

def mapping(x):
    x = x.replace('\n', ' ')
    map_dict = {
        'A':'a',
        '1':'a',
        'a': 'a',
        'c': 'c',
        'b':'b',
        'B':'b',
        '2':'b',
        '3':'c',
        'C':'c'
    }
    new_x = []
    for i in list(x):
        if i in map_dict:
            new_x.append(map_dict[i])
        else:
            new_x.append(i)
    return ''.join(new_x)

def get_set(x):
    # for char in chars:
    chars = mapping(x)
    symbols = chars.split()
    n = int(symbols[0])
    cards = symbols[1:]
    combinations = []
    for f, s in permutations(cards, 2):
        if sorted((f,s)) not in combinations:
            combinations.append(sorted((f,s)))
    return combinations


if __name__=='__main__':
    string ='''
    5
    |3|
    /111/
    \\22\\
    |b|
    |A|
    '''
    print(get_set(string))