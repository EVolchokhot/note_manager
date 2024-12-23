import re
created_date = input("Введите дату создания заметки (в порядке день-месяц-год): ")
issue_date = input("Введите дату истечения заметки (в порядке день-месяц-год): ")

temp_created_date = re.split(r'[,.\n? -]+', created_date)
temp_issue_date = re.split(r'[,.\n? -]+', issue_date)

print(str(temp_created_date[0] + ' - ' + temp_created_date[1]))
print(str(temp_issue_date[0] + ' - ' + temp_issue_date[1]))
