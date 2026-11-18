"""
Задача 5 (advanced). Таблица оценок: аналитика по студентам.

Таблица — список списков: строки — студенты, столбцы — оценки.
Имена студентов — отдельный список names той же длины.

5.1. Верните плоский список всех оценок.
5.2. Верните список средних оценок по студентам.
5.3. Верните список имён студентов со средним >= 4.5.
5.4. Верните dict: {имя: средняя оценка}.
5.5. Верните список имён студентов, отсортированных
     по средней оценке по убыванию.
"""


def flat(grades):
    result = []
    for x in grades:
        for n in x:
            result.append(n)
    return result
    pass


def averages(grades):
    return [sum(x) / len(x) for x in grades]
    pass


def top_students(names, grades):
    result = []
    for student, grade in enumerate(grades):
        if sum(grade) / len(grade) >= 4.5:
            result.append(names[student])
    return result
    pass


def name_to_average(names, grades):
    result = {}
    for student, grade in enumerate(grades):
        result[names[student]] = sum(grade) / len(grade)
    return result
    pass


def sorted_names(names, grades):
    return [name for name, _ in sorted(
        zip(names, grades),
        key=lambda grade: sum(grade[1]) / len(grade[1]),
        reverse=True
    )]
    pass


if __name__ == "__main__":
    names = ["Ann", "Bob", "Cara"]
    grades = [[5, 5, 4], [3, 3, 4], [5, 5, 5]]
    assert flat(grades) == [5, 5, 4, 3, 3, 4, 5, 5, 5]
    assert averages(grades) == [14 / 3, 10 / 3, 5.0]
    assert top_students(names, grades) == ["Ann", "Cara"]
    assert name_to_average(names, grades) == {
        "Ann": 14 / 3,
        "Bob": 10 / 3,
        "Cara": 5.0,
    }
    assert sorted_names(names, grades) == ["Cara", "Ann", "Bob"]
    print("task5 (advanced): все тесты пройдены.")
