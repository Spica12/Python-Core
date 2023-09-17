import random

data_transliterated = {
    "2004": {
        "AA": "Kyiv",
        "AB": "Vinnytska oblast",
        "AC": "Volynska oblast",
        "AE": "Dnipropetrovska oblast",
        "AH": "Donetsk oblast",
        "AI": "Kyivska oblast",
        "AM": "Zhytomyrska oblast",
        "AO": "Zakarpatska oblast",
        "AP": "Zaporizka oblast",
        "AT": "Ivano-Frankivska oblast",
        "AX": "Kharkivska oblast",
        "BA": "Kirovohradska oblast",
        "BB": "Luhansk oblast",
        "BC": "Lvivska oblast",
        "BE": "Mykolayivska oblast",
        "BH": "Odeska oblast",
        "BI": "Poltavska oblast",
        "BK": "Rivnenska oblast",
        "BM": "Sumska oblast",
        "BO": "Ternopilska oblast",
        "BT": "Khersonska oblast",
        "BX": "Khmelnytska oblast",
        "CA": "Cherkaska oblast",
        "CB": "Chernihivska oblast",
        "CE": "Chernivetska oblast"
    },
    "2013": {
        "KA": "Kyiv",
        "KB": "Vinnytska oblast",
        "KC": "Volynska oblast",
        "KE": "Dnipropetrovska oblast",
        "KH": "Donetsk oblast",
        "KI": "Kyivska oblast",
        "KM": "Zhytomyrska oblast",
        "KO": "Zakarpatska oblast",
        "KP": "Zaporizka oblast",
        "KT": "Ivano-Frankivska oblast",
        "KX": "Kharkivska oblast",
        "HA": "Kirovohradska oblast",
        "HB": "Luhansk oblast",
        "HC": "Lvivska oblast",
        "HE": "Mykolayivska oblast",
        "HH": "Odeska oblast",
        "HI": "Poltavska oblast",
        "HK": "Rivnenska oblast",
        "HM": "Sumska oblast",
        "HO": "Ternopilska oblast",
        "HT": "Khersonska oblast",
        "HX": "Khmelnytska oblast",
        "IA": "Cherkaska oblast",
        "IB": "Chernihivska oblast",
        "IE": "Chernivetska oblast"
    }
}

set_of_letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]

def car_number_generator():

    random_year = random.choice(list(data_transliterated.keys()))
    region_code = random.choice(list(data_transliterated[random_year].keys()))
    region_value = data_transliterated[random_year][region_code]

    numbers = str(random.randint(1000, 9999))

    initials = ''.join(random.choices(set_of_letters, k=2))
    
    car_number = ''.join([region_code, numbers, initials])

    return f'Generated car number: {car_number} from {region_value} {random_year} year'


print(car_number_generator())



