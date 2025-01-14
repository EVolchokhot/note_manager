title_list = []

while True:
    title = input("Добавьте заголовок заметки (Чтобы закончить добавление нажмите Enter): ")
    if  title != "":
        title_list.append(title)
    else: break

print(f'Заголовки вашей заметки: {title_list}')