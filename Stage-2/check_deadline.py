from datetime import datetime

# Сегодняшняя дата
today = datetime.today().date()
print("Сегодняшняя дата: ", today)
# Дата дедлайна
issue_date = datetime.strptime(input("Введите дедлайн(дд.мм.гггг): "), '%d.%m.%Y').date()
print("Дата дедлайна: ", issue_date)

#Вычисляем разницу дат
days_remaining = (issue_date - today).days

# Проверяем, вышел ли срок или сколько еще осталось дней
if days_remaining == 0:
    print("Срок истекает сегодня.")
elif days_remaining <= 0:
    print("Срок истек, дней с истечения срока:", abs(days_remaining))
else:
    print("Дней до истечения срока осталось:", days_remaining)