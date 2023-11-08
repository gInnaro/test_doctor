from datetime import datetime, timedelta
from operator import itemgetter

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

# Создаем список всех временных интервалов, начиная с 9:00 и заканчивая 21:00
start_time = datetime.strptime('09:00', '%H:%M')
end_time = datetime.strptime('21:00', '%H:%M')
busy_one_appointment = timedelta(minutes=30)
free_slots = []
time_slots = []
time = start_time

# Сортируем список по возрастанию
busy_sorted = sorted(busy, key=itemgetter('start'))

# Удаляем занятые временные интервалы из списка всех временных интервалов
for busy_slot in busy_sorted:
    busy_start = datetime.strptime(busy_slot['start'], '%H:%M')
    busy_stop = datetime.strptime(busy_slot['stop'], '%H:%M')
    while True:
        time_slots.append({'start': time.strftime('%H:%M'), 'stop': (time + timedelta(minutes=30)).strftime('%H:%M')})
        slot_start = datetime.strptime(time_slots[-1]['start'], '%H:%M')
        slot_stop = datetime.strptime(time_slots[-1]['stop'], '%H:%M')
        slot_free = True
        if (time < busy_stop and time >= busy_start) or (slot_stop > busy_start and slot_stop <= busy_stop):
            slot_free = False
            break
        if slot_free:
            free_slots.append({'start': time.strftime('%H:%M'), 'stop': (time + timedelta(minutes=30)).strftime('%H:%M')})
        time += busy_one_appointment
    time = busy_stop
    
# Обработка времени после последнего промежутка времени и до конца рабочего дня
while True:
    time += busy_one_appointment
    if time < end_time:
        free_slots.append({'start': (time - timedelta(minutes=30)).strftime('%H:%M'), 'stop': time.strftime('%H:%M')})
    else: break

# Выводим список свободных временных интервалов по 30 минут
for slot in free_slots:
    print(slot['start'] + ' - ' + slot['stop'])


