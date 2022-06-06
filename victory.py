# Модуль 6
answer = 0
question = 'yes'

while question == "yes":
    SJ = int(input("Введите год рождения Стива Джобса? "))
    BG = int(input("Введите год рождения Билл Гейтса? "))
    DP = int(input("Введите год рождения Джезоф Пакард? "))
    GP = int(input("Введите год рождения Григорий Перельман? "))
    VP = int(input("Введите год рождения Владимир Путин? "))
    if SJ == 1955:
        answer += 1
    if BG == 1955:
        answer += 1
    if DP == 1912:
        answer += 1
    if GP == 1966:
        answer += 1
    if VP == 1952:
        answer += 1

    print(f"Правильных ответов: {answer}")
    print(f"Колличество ошибок: { 5 - answer}")
    print(f"Процент правильных ответов: {answer * 100 // 5}%")
    print(f"Процент неправильных ответов {100 - (answer * 100 // 5)}%")

    b = input("Хотите начать заново? ")
