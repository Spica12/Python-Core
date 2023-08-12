"""
Розглянемо завдання на перевірку спаму в електронному листі або 
фільтрацію заборонених слів у повідомленні.

Нехай функція is_spam_words приймає рядок (параметр text), 
перевіряє його на вміст заборонених слів зі списку 
(параметр spam_words), і повертає результат перевірки: True, 
якщо є хоч одне слово присутнє зі списку, та False, якщо в 
тексті стоп-слів не виявлено.

Слова у параметрі text можуть бути у довільному регістрі, а 
значить функція is_spam_words, при пошуку заборонених слів, 
регістру незалежна і весь текст має зводитися до нижнього 
регістру. Для спрощення, будемо вважати, що в рядку є тільки 
одне заборонене слово.

Передбачити третій параметр функції space_around, який за 
замовчуванням дорівнює False. Він відповідатиме за те, що 
функція шукатиме окреме слово чи ні. Слово вважати, що стоїть 
окремо, якщо ліворуч від слова знаходиться символ пробілу або 
воно розташоване на початку тексту, а праворуч від слова 
знаходиться пробіл або символ крапки.

Наприклад, у тексті ми шукаємо слово "лох". То в слові "Молох" 
виклик та результат буде наступним:

    print(is_spam_words("Молох", ["лох"]))  # True
    print(is_spam_words("Молох", ["лох"], True))  # False

Тобто у другому випадку слово не окреме і є частиною іншого.

У цьому прикладі функція поверне True в обох випадках.

    print(is_spam_words("Ты лох.", ["лох"]))  # True
    print(is_spam_words("Ты лох.", ["лох"], True))  # True

------------------------------------------------------------
def is_spam_words(text, spam_words, space_around=False):
"""

def is_spam_words(text, spam_words, space_around=False):

    words_sentense = text.replace('.', '').split()
    
    for word in words_sentense:

        for spam in spam_words:

            if space_around and word == spam:
                return True
            elif not space_around and word.find(spam):
                return True
    
    return False


text = 'Молох це. тобі не щось'
is_spam = is_spam_words(text, ['лох'])
print(f'{text}; {is_spam = }')
is_spam = is_spam_words(text, ['лох'], True)
print(f'{text}; {is_spam = }')

text = 'Ти лох'
is_spam = is_spam_words(text, ['лох'])
print(f'{text}; {is_spam = }')
is_spam = is_spam_words(text, ['лох'], True)
print(f'{text}; {is_spam = }')
