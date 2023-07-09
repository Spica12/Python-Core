# Як відомо, зазвичай розробників заведено поділяти на три категорії:
# Джун (Junior) & mdash; молодший спеціаліст, 
# Мідл ( Middle) — основний розробник у компанії
# Сеньйор (Senior) — старший розробник. 

# Орієнтовно можна вважати, що до 1 року роботи включно — це Джуніор, 
# понад 5 років — це Сеньйор розробник, 
# а від одного року до 5 включно — мідл.

# Є змінна work_experience, що визначає стаж роботи програміста. 
# Залежно від стажу роботи, присвоїти змінній developer_type 
# значення "Junior", "Middle" або "Senior". Використовуйте, 
# якщо необхідно, булеві оператори or та and під час перевірок.

work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"

print(developer_type)