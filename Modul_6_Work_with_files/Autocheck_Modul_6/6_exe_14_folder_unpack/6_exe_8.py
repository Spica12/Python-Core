"""
Задано відомість абітурієнтів, які склали вступні іспити до університету. Структура даних щодо абітурієнтів подана у вигляді наступного списку:

[
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, на яку він поступив — ключ specialty, та отримані ним бали з окремих дисциплін — ключі math (математика), lang ( українська мова) та eng (англійська мова)

Розробіть функцію save_applicant_data(source, output), яка буде вказаний список із параметра source зберігати у файл із параметра output

Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу повинні бути записані через кому без прогалин прізвище абітурієнта, код спеціальності, на яку він поступив, та отримані ним бали за окремими дисциплінами.

Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Karpenko Dmitro,201,155,175,185
Вимоги:

відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
запис нового вмісту файлу output має бути або за допомогою методу writelines, або використовувати метод write
---------------------------------------------
def save_applicant_data(source, output):
"""

def save_applicant_data(source, output):
    
    with open(output, 'w') as file:
        for student in source:
            line = list()
            print(student)
            for field in student:
                line.append(str(student.get(field)))
            
            line = ','.join(line)
            file.write(f"{line}\n")
            



source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

path_output = 'D:/GoIT/Python Core\Modul_6_Work with files/Autocheck_Modul_6/6_exe_8_output.txt'

save_applicant_data(source, path_output)