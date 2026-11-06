"""
Задача 3 (advanced). Обработка логов с уровнями.

Лог — список строк "LEVEL:message".

3.1. Верните dict: {уровень: количество записей}.
3.2. Верните список сообщений уровня "ERROR".
3.3. Верните список уровней, отсортированных по
     убыванию частоты (key=lambda).
3.4. Верните True, если есть и "ERROR", и "WARN".
3.5. Верните список сообщений длиной > 4 в верхнем регистре.
"""


def level_counts(logs):
    result = {}
    for log in logs:
        if log.split(":")[0] in result:
            result[log.split(":")[0]] += 1
        else:
            result[log.split(":")[0]] = 1
    return result
    pass


def error_messages(logs):
    result = []
    for log in logs:
        if log.split(":")[0] == "ERROR":
            result.append(log.split(":")[1])
    return result
    pass


def levels_by_frequency(logs):
    result = level_counts(logs)
    return sorted(result, key=lambda level: -result[level])
    pass


def has_error_and_warn(logs):
    result = level_counts(logs)
    return result["ERROR"] and result["WARN"] and True
    pass


def long_messages_upper(logs):
    result = []
    for log in logs:
        if len(log.split(":")[1]) > 4:
            result.append(log.split(":")[1].upper())
    return result
    pass


if __name__ == "__main__":
    logs = ["INFO:start", "WARN:slow", "ERROR:fail", "INFO:done", "ERROR:crash"]
    assert level_counts(logs) == {"INFO": 2, "WARN": 1, "ERROR": 2}
    assert error_messages(logs) == ["fail", "crash"]
    assert levels_by_frequency(logs) == ["INFO", "ERROR", "WARN"]
    assert has_error_and_warn(logs) is True
    assert long_messages_upper(logs) == ["START", "CRASH"]
    print("task3 (advanced): все тесты пройдены.")
