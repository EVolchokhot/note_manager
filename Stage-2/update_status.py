status = "0"

def whatisstatus():
    global status
    print("Выберите статус заметки: \n1. выполнено \n2. в процессе \n3. отложено")
    num = input("Введите выбранный статус: ")
    if num == "1" or num == "выполнено" or num == "1. выполнено":
        status = "выполнено"
    elif num == "2" or num == "в процессе" or num == "2. в процессе":
        status = "в процессе"
    elif num == "3" or num == "отложено" or num == "3. отложено":
        status = "отложено"
    else:
        print("Введите номер действия!")
        whatisstatus()


whatisstatus()
print(f'Статус заметки успешно обновлён на: "{status}"')