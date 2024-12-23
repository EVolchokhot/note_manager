import re
created_date = input("Введите дату создания заметки (в виде хх.хх.хххх): ")
issue_date = input("Введите дату истечения заметки (в виде хх.хх.хххх): ")

temp_created_date = re.split(r'[,.\n? -]+', created_date)
temp_issue_date = re.split(r'[,.\n? -]+', issue_date)

print(str(temp_created_date[0] + ' - ' + temp_created_date[1]))
print(str(temp_issue_date[0] + ' - ' + temp_issue_date[1]))
