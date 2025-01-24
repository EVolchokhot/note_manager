from datetime import datetime

today = datetime.today().date()
print(today)
# issue = input("Введите дедлайн(дд.мм.гггг): ")
issue_date = datetime.strptime(input("Введите дедлайн(дд.мм.гггг): "), '%d.%m.%Y').date()
print(issue_date)

days_remaining = (issue_date - today).days

# Проверяем, вышел ли срок или еще есть дни
if days_remaining == 0:
    print("Срок истекает сегодня.")
elif days_remaining <= 0:
    print("Срок истек, дней с истечения срока:", abs(days_remaining))
else:
    print("Дней до истечения срока осталось:", days_remaining)