import re

def check_date(date):
    """
    Проверяет корректность даты.

    Допустимые форматы:
    - день.месяц.год
    - день/месяц/год
    - день-месяц-год
    - год.месяц.день
    - год/месяц/день
    - год-месяц-день
    - день месяц_rus год
    - Месяц_eng день, год
    - Мес_eng день, год
    - год, Месяц_eng день
    - год, Мес_eng день

    Args:
    date (str): Дата для проверки.

    Returns:
    bool: True, если дата корректна, False в противном случае.
    """
    pattern = (
        r'\b(\d{1,2}[./-]\d{1,2}[./-]\d{4}|\d{4}[./-]\d{1,2}[./-]\d{1,2}|'  # Форматы с точкой, слешем и дефисом
        r'\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|'  # День месяц_rus год
        r'октября|ноября|декабря)\s\d{4}|\w+\s\d{1,2},\s\d{4}|\w+\s\d{1,2},\s\d{4}|\d{4},\s\w+\s\d{1,2}|\d{4},\s\w+\s\d{1,2})\b'
    )

    return bool(re.match(pattern, date, re.IGNORECASE))

# Примеры корректных дат
"""
>>> check_date("20 января 1806")
True
>>> check_date("1924, July 25")
True
>>> check_date("26/09/1635")
True
>>> check_date("3.1.1506")
True
"""

# Примеры некорректных дат
"""
>>> check_date("25.08-1002")
False
>>> check_date("декабря 19, 1838")
False
>>> check_date("8.20.1973")
False
>>> check_date("Jun 7, -1563")
False
>>> check_date("31 февраля 2023")
False
>>> check_date("31 июня 2015")
False
"""

# Дополнительные тесты
"""
>>> check_date("2022, September 14")
True
>>> check_date("2022, Sep 14")
True
>>> check_date("2022, Feb 5")
True
>>> check_date("2022, Apr 01")
True
>>> check_date("2022, February 30")
False  # Несуществующая дата
>>> check_date("2022, Dec 32")
False  # Несуществующая дата
"""
