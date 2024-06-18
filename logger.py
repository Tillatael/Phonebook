from data_create import name_data, surname_data, phone_data, adress_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = adress_data()
    var = int(input(f'В каком формате записать данные? \n'
    f'1 Вариант:  \n'
    f'{name}\n {surname}\n {phone}\n {address} \n\n'
    f'2 Вариант: \n'
    f'{name}; {surname};  {phone};  {address} \n'
    f'Выберите вариант: '))

    while var !=1 and var !=2:
        print("Некорректное значение")
        var = int(input("Введите число: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n {surname}\n {phone}\n {address} \n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}; {surname};  {phone};  {address} \n\n')



def print_data():
    print('Вывожу данные из файла 1: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из файла 2: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        print(*data_second)

def delete_data():
    name_to_delete = input("Введите имя для удаления записи: ")

    # Обработка первого формата файла
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
        skip = False
        for line in lines:
            if line.strip() == name_to_delete:
                skip = True
            elif skip and line.strip() == '':
                skip = False
                continue
            if not skip:
                file.write(line)

    # Обработка второго формата файла
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        for line in lines:
            if not line.startswith(name_to_delete + ';'):
                file.write(line)
    print(f"Запись с именем {name_to_delete} удалена.")


def update_data():
    name_to_update = input("Введите имя для изменения записи: ")
    updated = False

    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
        skip = False
        for line in lines:
            if line.strip() == name_to_update:
                updated = True
                new_name = name_data()
                new_surname = surname_data()
                new_phone = phone_data()
                new_address = adress_data()
                file.write(
                    f'{new_name}\n {new_surname}\n {new_phone}\n {new_address} \n\n')
                skip = True
            elif skip and line.strip() == '':
                skip = False
                continue
            if not skip:
                file.write(line)
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith(name_to_update + ';'):
                updated = True
                new_name = name_data()
                new_surname = surname_data()
                new_phone = phone_data()
                new_address = adress_data()
                file.write(
                    f'{new_name}; {new_surname}; {new_phone}; {new_address} \n')
            else:
                file.write(line)

    if updated:
        print(f"Запись с именем {name_to_update} обновлена.")
    else:
        print(f"Запись с именем {name_to_update} не найдена.")