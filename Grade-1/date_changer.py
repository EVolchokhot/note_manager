import re

created_date = input("Введите дату создания (дд мм гггг): ")
issue_date = input("Введите дату дедлайна (дд мм гггг): ")

temp_created_date = re.split(r'[,.\n? -]+', created_date)
temp_issue_date = re.split(r'[,.\n? -]+', issue_date)

print("Дата создания заметки:", str(temp_created_date[0] + ' - ' + temp_created_date[1]))
print("Дата истечения заметки:", str(temp_issue_date[0] + ' - ' + temp_issue_date[1]))
