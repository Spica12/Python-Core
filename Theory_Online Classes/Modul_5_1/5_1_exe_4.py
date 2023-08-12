phone_storage = ["380669640547", "0637306465 ", " 420961935171", "632643973", "050832520 ",
                 "00000000000", "480730283918", "597632643973", "0986223575", "37(029)7947963",
                 "+42(050)123-32-34", "38986223575","38(950)123 32 34", "38(050)123 32 3b"]

codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093", "029"}

def is_valid_phone(phone):

    if phone.isdigit():
        if len(phone) == 12:
            if phone[2] == '0':
                if phone[2:5] in codes_operators:
                    return True
                else:
                    return False
            else:
                return False
        
        if len(phone) == 10:
            if phone[:3] in codes_operators:
                    return True
            else:
                return False
        else:
            return False
    

def clean_up_phone(phone):

    return (phone.strip()
            .removeprefix('+')
            .replace('(', '')
            .replace(')', '')
            .replace('-', '')
            .replace(' ', ''))


def passed_control():

    for phone in phone_storage:
    phone = clean_up_phone(phone)
    is_valid = is_valid_phone(phone)
    if is_valid:
        print('Phone {:^4}| {:<16}| {:^4} valid'.format(' ', phone, ' '))
    else:
        print('Phone {:^4}| {:<16}| {:^4} invalid'.format(' ', phone, ' '))


def phone_by_country(list_of_phoned):
    numbers_dict = dict()
    for i in range(len(list_of_phoned)):
        phone = clean_up_phone(list_of_phoned)
        if phone.startswith('38'):
            numbers_dict.setdefault('UA', [].append(phone))
        if phone.startswith('42'):
            numbers_dict.setdefault('IT', [].append(phone))
        if phone.startswith('37'):
            numbers_dict.setdefault('UK', [].append(phone))
        if phone.startswith('48'):
            numbers_dict.setdefault('PL', [].append(phone))
    
    return numbers_dict

print(phone_by_country(phone_storage))
