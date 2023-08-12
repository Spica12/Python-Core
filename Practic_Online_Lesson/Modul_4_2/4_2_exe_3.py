# Гра в карти
# МастіЖ
# s - (Spades) Піки
# h - (Hearts) Черви
# d - (Diamonds) Бубни
# c - (Clovers) Хрести
# suits = ['s', 'h', 'd', 'c']
# values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

from random import randrange


def create_deck():

    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = list()

    for suit in suits:
        for value in values:
            deck.append(f'{value}{suit}')

    return deck


def deal(players, cards, deck):

    if players * cards > len(deck):
        return deck
    
    table = list()

    for _ in range(0, cards):
        for player in range(players):

            if player >= len(table):
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())

    return table


def shuffle_deck(deck):

    new_deck = deck.copy()

    for i in range(0, len(deck)):
        other_index = randrange(0, len(new_deck))
        new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
    
    return new_deck
    

def main(players, cards):

    init_deck = create_deck()
    print(f'Open new deck: {init_deck}\n')

    deck = shuffle_deck(init_deck)
    print(f'Shuffle deck: {deck}\n')

    print(f'Invite {players} players to table')
    print(f'Give {cards} cards to everyone player')

    table = deal(players, cards, deck)

    for i in range(players):
        print(f'Player {i+1} has cards: {table[i]}')

    print(f'Deck after shuffling: {deck}')


if __name__ == '__main__':
    main(4, 6)