from logger import input_data, print_data, delete_data, update_data

def interface():
    print("Добрый день! Вы попали на специальный бот-справочник Geekbrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление данных \n 4 - изменение данных")
    command = int(input("Введите число: "))

    while command !=1 and command !=2 and command !=3 and command !=4:
        print("Некорректное значение")
        command = int(input("Введите число: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        update_data()
interface()