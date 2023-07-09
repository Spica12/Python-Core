# Скласти програму визначення номера під'їзду та поверху квартири 
# за заданим номером квартири. У будинку 5 поверхів і 4 квартири на 
# поверсі.
# 
# Input - 54
# 
# Output_entrance - 3
# Output_floor - 4

number_of_flat = int(input('Enter number of flat: '))

OUTPUT_FLOOR = 5
OUTPUT_FLATS_ON_FLOOR = 4

flats_in_entrance = OUTPUT_FLATS_ON_FLOOR * OUTPUT_FLOOR


entrance = (number_of_flat - 1) // flats_in_entrance + 1
floor = ((number_of_flat - 1) // OUTPUT_FLATS_ON_FLOOR) % OUTPUT_FLOOR + 1
print(entrance, floor)
