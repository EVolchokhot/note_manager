username = input("Введите имя пользователя: ")
title_1 = input("Введите первый заголовок заметки: ")
title_2 = input("Введите второй заголовок заметки: ")
title_3 = input("Введите третий заголовок заметки: ")
content = input("Введите текст заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки: ")
issue_date = input("Введите дедлайн заметки: ")

title_list = [title_1, title_2, title_3]

print("Имя пользователя:", username)
print("Заголовки заметки:", title_list)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", str(created_date))
print("Дедлайн заметки:", str(issue_date))

