salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total = 0  # подушка безопасности

for _ in range(months):
    total += spend - salary
    spend += spend * increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total))
