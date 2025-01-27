title_list = []
def titles():
    while True:
        title = input("Добавьте заголовок заметки (Чтобы закончить добавление нажмите Enter): ")
        if  title != "":
            title_list.append(title)
        else: break

titles()
print(f'Заголовки вашей заметки: {title_list}')