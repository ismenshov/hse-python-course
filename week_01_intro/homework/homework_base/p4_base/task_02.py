"""
ДЗ презентации 4, базовый уровень, задача 1.
Время: 15–20 минут.

Тема: ввод/вывод, str, int.

Условие:
    Запросите имя, возраст и город.
    Выведите: Иван, 25 лет, Москва.
"""

def main():
    name = input("Введите своё имя\n")
    age = int(input("Введите свой возраст\n"))
    if age == 1:
        age_noun = "год"
    elif age < 5:
        age_noun = "года"
    elif age < 21:
        age_noun = "лет"
    elif age % 10 == 1:
        age_noun = "год"
    elif age % 10 < 5:
        age_noun = "года"
    else:
        age_noun = "лет"
    city = input("Введите свой город\n")
    print(f"{name}, {age} {age_noun}, {city}.")


if __name__ == "__main__":
    main()
