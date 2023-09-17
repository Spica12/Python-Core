from re import sub


UKR_LETTERS = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
UKR_TRANSLATION = ("a", "b", "v", "g", 'g',"d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                    "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")
TRANS = {}

for key, ukr_letter in zip(UKR_LETTERS, UKR_TRANSLATION):

    TRANS[ord(key)] = ukr_letter
    TRANS[ord(key.upper())] = ukr_letter.upper()


def normalize(name):

    new_name = sub(r'\W', '_', name)
    new_name = new_name.translate(TRANS)

    return new_name
