import re
import csv

files = [
    "./Materials/info_1.txt",
    "./Materials/info_2.txt",
    "./Materials/info_3.txt"
]


def get_data(files):
    regexp = '[ ]+ ([-\\w ]*\\w)'
    regexp_os_prod = 'Изготовитель ОС:' + regexp
    regexp_os_name = 'Название ОС:' + regexp
    regexp_os_code = 'Код продукта:' + regexp
    regexp_os_type = 'Тип системы:' + regexp

    main_data_columns = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = []

    for file in files:
        os_prod = ""
        os_name = ""
        os_code = ""
        os_type = ""
        with open(file, 'r', newline="") as file_reader:
            line = file_reader.readline()
            while line:
                match_os_prod = re.search(regexp_os_prod, line)
                match_os_name = re.search(regexp_os_name, line)
                match_os_code = re.search(regexp_os_code, line)
                match_os_type = re.search(regexp_os_type, line)
                if match_os_prod:
                    os_prod = match_os_prod.group(1)
                elif match_os_name:
                    os_name = match_os_name.group(1)
                elif match_os_code:
                    os_code = match_os_code.group(1)
                elif match_os_type:
                    os_type = match_os_type.group(1)
                line = file_reader.readline()
        main_data.append([os_prod, os_name, os_code, os_type])

    return main_data_columns, main_data


def write_to_csv(file):
    column_names, data = get_data(files)
    with open(file, 'w', newline="") as file_writer:
        csv_writer = csv.writer(file_writer, delimiter=';')
        csv_writer.writerow(column_names)
        for d in data:
            csv_writer.writerow(d)


write_to_csv('sample.csv')
