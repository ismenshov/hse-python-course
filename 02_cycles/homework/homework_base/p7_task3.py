"""
Задача 3 (base). Обработка логов.

Лог — список строк вида "LEVEL:message", например "INFO:start".

3.1. Верните список только сообщений (без "LEVEL:").
3.2. Верните список только уровней (INFO, WARN, ERROR).
3.3. Верните количество записей уровня "ERROR".
3.4. Верните список сообщений, длина которых больше 5.
3.5. Верните True, если есть хотя бы одна запись "ERROR:...".
"""


def messages(logs):
    return [x.split(":")[1] for x in logs]
    pass


def levels(logs):
    return [x.split(":")[0] for x in logs]
    pass


def error_count(logs):
    list = levels(logs)
    count = 0
    for n in list:
        if n == "ERROR":
            count += 1
    return count
    pass


def long_messages(logs):
    list = messages(logs)
    count = []
    for n in list:
        if len(n) >= 5:
            count.append(n)
    return count
    pass


def has_error(logs):
    return any("ERROR" for n in [x.split(":")[0] for x in logs])
    pass


if __name__ == "__main__":
    logs = ["INFO:start", "WARN:slow", "ERROR:fail", "INFO:done", "ERROR:crash"]
    assert messages(logs) == ["start", "slow", "fail", "done", "crash"]
    assert levels(logs) == ["INFO", "WARN", "ERROR", "INFO", "ERROR"]
    assert error_count(logs) == 2
    assert long_messages(logs) == ["start", "crash"]
    assert has_error(logs) is True
    print("task3 (base): все тесты пройдены.")
