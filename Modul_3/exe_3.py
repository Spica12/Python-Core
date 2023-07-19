"""
Необхідно написати функцію, яка буде обчислювати суму за 
користування послугами таксі. Сума складається з базового тарифу 
40 грн, та 10 грн за кожен кілометр поїздки. Напишіть функцію, 
яка приймає один параметр — відстань поїздки в кілометрах. 
Функція має повертати підсумкову суму оплати за послуги таксі 
дійсним числом. Також функція повинна змінювати глобальну 
змінну — лічильник total_trip після кожного виклику та збільшувати
її на одиницю.
"""
# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def calculate_trip_price(distance_km):
# ---------------------------------------------
base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):

    global total_trip

    total_trip += 1

    return base_rate + distance_km * price_per_km

price = calculate_trip_price(100)

print(price, total_trip)