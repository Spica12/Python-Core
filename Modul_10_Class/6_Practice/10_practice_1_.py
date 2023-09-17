from random import randint
from collections import UserDict


class Card(UserDict):

    number_per_letter = 15
    limit_line = 5
    loto_fields = ['B', 'I', 'N', 'G', 'O']

    def __init__(self):

        super().__init__()
        self.min_num = 1
        self.max_num = self.number_per_letter
        self.create_card()

    def create_card(self):

        for letter in self.loto_fields:
            self.data[letter] = []

            while len(self.data[letter]) < self.limit_line:
                next_num = randint(self.min_num, self.max_num)

                if next_num not in self.data[letter]:
                    self.data[letter].append(next_num)

            self.min_num = self.max_num + 1
            self.max_num = self.max_num + self.number_per_letter


    def pretty_card_info(self):
        print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data))

        for i in range(self.limit_line):
            line = list()

            for letter in self.loto_fields:
                line.append(self.data[letter][i])
            
            print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*line))
            line.clear()


class Player:

    def _init__(self, name: str, card: Card):

        self.card = card
        self.name = name
        self.winner = False

    def check_winner(self):
        for line in self.card.values():
            if sum(line) == 0:
                self.winner = True

        for index in range(self.card.limit_line):
            temp_line = list()
            for key in self.card.keys():
                temp_line.append(self.card[key][index])
        
        if sum(temp_line) == 0:
            self.winner = True

    def mark_number(self, number):
        for line in self.card.values():
            if number in line:
                for i in range(len(line)):
                    if line[i] == number:
                        line[i] == 0


class LotoGame:

    def __init__(self, player_names):
        self.number_of_players = len(player_names)
        self.players_names = player_names
        self.game_progress = 0
        self.player: list(Player) = list()
        self.winner: list(Player) = list()
        self.drawn_numbers = list()

    def create_game(self):
        for name in self.players_names:
            card = Card()
            player = Player(name, card)
            self.players.append(player)

    def start_game(self):
        while True:
            self.step_game()
            self.check_winner()
            if len(self.winner) > 0:
                break

        return self.game_progresesses

    def step_game(self):
        while True:
            number = randint(0, Card.number_per_letter * len(Card.loto_fields))
            if number not in self.dram_numbers:
                self.drawn_numbers.append(number)
                break

        for player in self.players:
            player.mark_number(number)
            player.check_winner()

    def check_winners(self):
        for player in self.players:
            if player.winner:
                self.winners.append(player)


game = LotoGame(['Oleh', 'Stepan', 'Maria', 'Bohdan'])
game.create_game()

quantity, winners = game.start_game()
print(f'Step required {quantity}')

for winner in winners:
    print(f'Winner {winner.name}')
    winner.card.pretty_card_info()