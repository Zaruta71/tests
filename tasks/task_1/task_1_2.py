def course_durations(durations_dict_, courses_list_):
    print(durations_dict_)
    print(courses_list_)
    for duration, id in durations_dict_.items():
        # Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность»
        # print(duration, id)
        for i in id:
            yield f'{courses_list_[i]["title"]} - {duration} месяцев'


# Наводим порядок: упорядочиваем курсы по продолжительности

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
    course_dict = {"title": course, "mentors": mentor, "duration": duration}
    courses_list.append(course_dict)

# С этого момента начинается выполнение задания 2
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# Отсортируйте курсы по длительности (ключ duration), но при этом сохраните порядковый номер каждого курса из courses_list
# Самое простое — создать новый словарь durations_dict с ключом — duration и значением — исходным номером курса в courses_list
# Но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря — это список индексов, а не одно значение
durations_dict = {}

# Допишите код цикла так, чтобы в нём вы получали id курса. Подсказка: помните о функции enumerate
for id, value in enumerate(courses_list):
    key = value['duration']  # Получите значение из ключа duration
    # Допишите код ниже, который добавляет в словарь durations_dict по ключу key значения — id
    if durations_dict.get(key):
        temp_list = durations_dict.get(key).append(id)
    else:
        durations_dict[key] = [id]

# Отсортируем словарь по ключам. Этот код уже готов, ничего менять не нужно
# Здесь мы получаем пары ключ-значение в виде кортежа, и функция sorted выполняет сортировку по первым значениям кортежа — ключам
durations_dict = dict(sorted(durations_dict.items()))

# Выведите курсы, отсортированные по длительности
# Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения


res = course_durations(durations_dict_=durations_dict, courses_list_=courses_list)

for item in res:
    print(item)