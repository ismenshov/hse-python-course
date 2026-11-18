"""
Задача 1 (base). Журнал температур.

Устройство пишет температуру каждый час. Дан список чисел temps.

1.1. Верните список только тех температур, которые выше 0.
1.2. Верните сумму всех температур.
1.3. Верните среднее арифметическое (как float).
1.4. Верните количество температур ниже -10.
1.5. Верните список температур, округлённых до целого
     (используйте int(x) для простоты).
"""


def above_zero(temps):
    result = []
    for t in temps:
        if t > 0:
            result.append(t)
    return result
    pass


def total(temps):
    return sum(temps)
    pass


def average(temps):
    return sum(temps) / len(temps)
    pass


def below_minus_ten(temps):
    result = 0
    for t in temps:
        if t < -10:
            result += 1
    return result
    pass


def rounded(temps):
    return [round(t) for t in temps]
    pass


if __name__ == "__main__":
    temps = [3, -5, 0, 12, -15, 7, -20, 4]
    assert above_zero(temps) == [3, 12, 7, 4]
    assert total(temps) == -14
    assert average(temps) == -14 / 8
    assert below_minus_ten(temps) == 2
    assert rounded(temps) == [3, -5, 0, 12, -15, 7, -20, 4]
    print("task1 (base): все тесты пройдены.")
