
trans_map = {ord('Я'): 'Ya', ord('н'): 'n', ord('а'): 'a', ord('о'): 'o'}


ukr_name = 'Яна'

lat_nam = ukr_name.translate(trans_map)
print(ukr_name, ' = ', lat_nam)

print('-------------------------------------------')

text = 'Hello wоrld!'

indx = text.find('World')
print(indx) # -1

print('-------------------------------------------')

text = 'Hello Wоrld'

indx = text.find('World')
new_indx = text.translate(trans_map).find('World')
print(indx) # -1
print(new_indx) # 6
