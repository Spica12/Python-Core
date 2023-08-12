import re

text = 'First sentence.\nSecond sentence!\nThird sentence?'


sentences = text.split('.')
print(sentences)

print('-----------------------------')
sentences = re.split('[\.\!\?]', text)
print(sentences)

print('-----------------------------')
sentences = text.split('\n')
print(sentences)

new_text = ' '.join(sentences)
print(new_text)
