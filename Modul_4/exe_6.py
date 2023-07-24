# У нас є список показників студентів групи – це список з 
# отриманими балами з тестування. Необхідно поділити список 
# на дві частини. Напишіть функцію split_list, яка приймає 
# список (цілі числа), знаходить середнє значення бала у 
# списку та ділить його на два списки. У перший потрапляють 
# значення менше середнього, включаючи середнє значення, тоді 
# як у другий — строго більше від середнього. Функція повертає 
# кортеж цих двох списків. Для порожнього списку повертаємо два 
# порожні списки.
# ----------------------------------
# def split_list(grade):
# ---------------------------------
def split_list(grade):

    first_list = []
    second_list = []

    average_sum = 0
    count = 0

    for i in grade:
        average_sum += i
        count += 1


    if count > 0:

        average_ball = average_sum / count

        for result in grade:

            if result <= average_ball:
                first_list.append(result)
            else:
                second_list.append(result)

        

    output_data = (first_list, second_list)

    return output_data


list_of_student = (1, 12, 3, 24, 5)

tuple_one = split_list(list_of_student)
print(tuple_one)

list_of_student = tuple()

tuple_two = split_list(list_of_student)
print(tuple_two)