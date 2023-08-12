'''---- LearnEngText ----
What I want from this program?
- Answer must be missed words 
- Add numbers to miss words
- Several levels fo studing

'''
import re

text = """
— Listen to this, George: «Dear Gemini, today definitely won’t be 
  your day. Things will repeatedly not go the way you want.»
— Linda, how many times have I told you not to read these stupid 
  horoscopes?
— Wait, it says: «Watch out for possible problems with your 
  superiors.» Today, of all days! This is a disaster!
— Why?
— I have this board meeting today, remember? I will certainly 
  bungle my presentation...
— Linda, these predictions are simply not true. Remember what my 
  horoscope said yesterday? «Libra, you may lose a great deal of 
  time in traffic jams.» I never even left the house!
— But had you left the house, you could have been stuck in traffic
  – what with that accident on Route 6.
— Linda, these horoscopes are completely made up. Look, I can 
  come up with one now. My friend Mike – he's a Taurus, I think. 
  «Dear Taurus, you certainly have to go to work today. That beer 
  will have to wait till Friday.»
— Now you're just being ridiculous. You know Mike always goes 
  out for a beer on Fridays.
— And so does every other man in this town!
— What's your point?
— Any of the things these horoscopes describe might happen to 
  anyone. Your colleague Sarah, she's what, a Sagittarius?
— A Scorpio.
— «Scorpios, be extra careful today when crossing the street. 
  You may get hit by a car!» How's that for Sarah's horoscope?
— Right. This could as easily be a prediction for Virgos or Pisces... oh, I see.
— Exactly. Now, which sign is your boss?
— Aquarius.
— Here's what I’ve got for him: «Dear Aquarius, you might get 
  an unexpected visit today. It will probably be someone 
  unpleasant. Could be a policeman, a debt collector, a paramedic. 
  You'll have to cancel your plans.» How's that?
— Hold on, here's my boss calling me now. Yes, Mr. Pence. 
  No board meeting today? Because you're...where? At a police 
  station? Yeah, talk to you later... George, please don't make 
  any more predictions for today, ok?"""





def print_text(list_of_words: list) -> None:
    
    new_text = ''
    len_row = 0

    for word in list_of_words:

        if word == '—' or len_row + len(word) > 70:
            new_text += ' \n'
            len_row = 0

        add_word = word + ' '
    
        len_row += len(add_word)
        new_text += add_word

    print(new_text)

def replace_words(text: str, words: list) -> str:

    count = 0
    
    def repl(m):

        nonlocal count

        count += 1
        return '(' + str(count) + ')' + '*' * len(m[0])

    words = '|'.join(words)

    text = re.sub(words, repl, text,flags=re.IGNORECASE)    

    return text 
    



if __name__ == '__main__':

    some_words = ['told', 'This']

    print(replace_words(text, some_words))

    user_input = input('Press any button for exit')
