import re

username = "Евгений"
title = "Заметка 1"
content = "Первая заметка созданная в этом проекте"
status = "active"
created_date = "21-12-2024"
issue_date = "21-12-2034"

temp_created_date = re.split(r'[,.\n? -]+', created_date)
temp_issue_date = re.split(r'[,.\n? -]+', issue_date)

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", str(temp_created_date[0] + ' - ' + temp_created_date[1]))
print("Дата истечения заметки:", str(temp_issue_date[0] + ' - ' + temp_issue_date[1]))
