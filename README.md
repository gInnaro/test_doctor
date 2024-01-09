# test_doctor
Доктор принимает с 9 утра до 9 вечера.
Часть времени у него занята: приемы, обед, уборка кабинета.
<code>
busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]
</code>
Требуется сформировать список свободных окон по 30 минут.

Результат 
09:00 - 09:30
09:30 - 10:00
10:00 - 10:30
10:50 - 11:20
11:20 - 11:50
11:50 - 12:20
12:20 - 12:50
12:50 - 13:20
13:20 - 13:50
13:50 - 14:20
15:50 - 16:20
17:20 - 17:50
17:50 - 18:20
18:50 - 19:20
19:20 - 19:50
20:20 - 20:50
