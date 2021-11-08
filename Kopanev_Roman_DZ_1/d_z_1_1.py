# Реализовать вывод
# информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: < s > сек;
# до часа: < m > мин < s > сек;до суток: < h > час < m > мин < s > сек; *в остальных случаях: < d > дн < h > час < m > мин < s > сек.

duration = int(input('Введите продолжительность времени в секундах: '))
days = duration // 86400
hours = duration // 3600
minutes = duration // 60
seconds = duration % 60
if duration <= 0:
    print('Число должно быть больше нуля')
elif duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    print(hours % 3600, 'час', minutes % 60, 'мин', seconds, 'сек')
else:
    print(days % 86400, 'дн', hours % 3600, 'час', minutes % 60, 'мин', seconds, 'сек')
