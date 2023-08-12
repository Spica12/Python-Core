numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


header = '|{:^15}|{:^15}|{:^15}|{:^15}|'.format('int', 'dex', 'oct', 'bin')
separator = '-' * len(header)
body = ''
for num in numbers:
    body += '|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n'.format(num)
table = '\n'.join([separator, header, separator, body, separator])

print(table)

print('----------------------------------------')


def table(*columns, hor_separator='-', vert_separator='|') -> str:
    print(columns)
    table = ''
    length_columns = list()
    borders = list()

    for index_column, column in enumerate(columns):
        length_columns.append(0)
        borders.append('')


        for index_row, row in enumerate(column):

            if (len(str(row))+2) > length_columns[index_column]:
                length_columns[index_column] = len(str(row)) + 2

        borders[index_column] = hor_separator * (length_columns[index_column] + 2)

    print(f'{table = }')
    print(f'{length_columns = }')
    print(f'{borders = }')

    # table = ''
    # length_columns = [0 for _ in range(len(columns))]
    # rows_columns = [0 for _ in range(len(columns))]
    # borders = [0 for _ in range(len(columns))]
    # header = [0 for _ in range(len(columns))]

    # for index_column, column in enumerate(columns):
    #     rows_columns[index_column] = len(column)
    #     for row in column:

    #         if (len(str(row))+2) > length_columns[index_column]:
    #             length_columns[index_column] = len(str(row)) + 2
        
    #     borders[index_column] = hor_separator * (length_columns[index_column] + 2)
    #     header[index_column] = column[0]
            
    # print(f'{length_columns = }')
    # print(f'{rows_columns = }')
    # print(f'{header = }')


    # for index_row in range(1, max(rows_columns)):
        
    #     temp_table = list()

    #     for column in range(len(columns)):

    #         try:
    #             temp_row.append(str(columns[column][index_row]))
    #         except IndexError:
    #             temp_row.append('')


    #     temp_table.append(temp_table)


    # print('////')


    # print(table)



column_one = [i for i in range(14)]
column_two = [i**2 for i in range(18)]
column_three = [i**3 for i in range(17)]

column_one.insert(0, 'First column')
column_two.insert(0, 'Second column')
column_three.insert(0, 'Third column')


print(column_one, column_two, column_three, sep='\n')
print('------------ START --------------')
print(table(column_one, column_two, column_three))
print('------------ FINISH --------------')

