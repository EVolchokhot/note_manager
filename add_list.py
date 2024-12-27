username = input("Введите имя пользователя: ")
title = input("Введите название заметки: ")
title_1 = input("Введите первый заголовок заметки: ")
title_2 = input("Введите второй заголовок заметки: ")
title_3 = input("Введите третий заголовок заметки: ")
content = input("Введите текст заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки (в виде хх.хх.хххх): ")
issue_date = input("Введите дату истечения заметки (в виде хх.хх.хххх): ")

import re

temp_created_date = re.split(r'[,.\n? -]+', created_date)
temp_issue_date = re.split(r'[,.\n? -]+', issue_date)

print("Имя пользователя:", username)
print("Название заметки:", title)
print("Первый заголовок заметки: ", title_1)
print("Второй заголовок заметки: ", title_2)
print("Третий заголовок заметки: ", title_3)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", str(temp_created_date[0] + ' - ' + temp_created_date[1]))
print("Дата истечения заметки:", str(temp_issue_date[0] + ' - ' + temp_issue_date[1]))

