"""
Задача 1 (advanced). Анализ температурных рядов.

Дан список температур temps.

1.1. Верните список температур без выбросов:
     только значения в диапазоне [-50, 50] включительно.
1.2. Верните список "нормализованных" значений:
     каждое значение минус среднее по исходному списку.
1.3. Верните список индексов, где температура отрицательная.
1.4. Верните dict: {индекс: температура} только для
     отрицательных температур.
1.5. Верните список температур, отсортированных по abs.
"""


def filter_outliers(temps):
    result = []
    for t in temps:
        if t >= -50 and t <= 50:
            result.append(t)
    return result
    pass


def normalized(temps):
    return [t - sum(temps) / len(temps) for t in temps]
    pass


def negative_indices(temps):
    result = []
    for i, t in enumerate(temps):
        if t < 0:
            result.append(i)
    return result
    pass


def negative_dict(temps):
    result = {}
    for i, t in enumerate(temps):
        if t < 0:
            result[i] = t
    return result
    pass


def sorted_by_abs(temps):
    return sorted(temps, key=lambda temp: abs(temp))
    pass


if __name__ == "__main__":
    temps = [3, -5, 120, -15, 7, -60, 4, 0]
    assert filter_outliers(temps) == [3, -5, -15, 7, 4, 0]
    avg = sum(temps) / len(temps)
    assert normalized(temps) == [t - avg for t in temps]
    assert negative_indices(temps) == [1, 3, 5]
    assert negative_dict(temps) == {1: -5, 3: -15, 5: -60}
    assert sorted_by_abs(temps) == [0, 3, 4, -5, 7, -15, -60, 120]
    print("task1 (advanced): все тесты пройдены.")
