from random import choice

hangman_pics = [
    """
      +---+
          |
          |
          |
         ===""",
    """
      +---+
      O   |
          |
          |
         ===""",
    """
      +---+
      O   |
      |   |
          |
         ===""",
    """
      +---+
      O   |
     /|   |
          |
         ===""",
    """
      +---+
      O   |
     /|\  |
          |
         ===""",
    """
      +---+
      O   |
     /|\  |
     /    |
         ===""",
    """
      +---+
      O   |
     /|\  |
     / \  |
         ==="""
]


words = ['python', 'poker', 'programing', 'sunflower', 'Ukraine']
word = choice(words).upper()
quessed = list()


def print_word():
    display_word = ''

    for char in word:
        display_word += str(char if char in quessed else '_')

    print(display_word)

    return display_word

def main():

    attempts = 6
    

    while attempts > 0:
        print(f'{quessed=}')
        print(hangman_pics[6 - attempts])

        display_word = print_word()

        if '_' not in display_word:
            print(f'You are win! The quessed word was {word}')
            break
        
        quess = input('Guess a letter: ').upper()

        if quess in quessed:
            print('You already quessed this letter')
        elif quess in word:
            print('Correct letter!')
            quessed.append(quess)
        else:
            print('Wrong quess!')
            quessed.append(quess)
            attempts -= 1

    if attempts == 0:
        print(hangman_pics[-1])
        print('You lose!')
    
if __name__ == '__main__':
    main()
    
