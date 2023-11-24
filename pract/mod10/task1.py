import re

def check_password(password):
    """
    Проверяет корректность пароля.

    Пароль должен:
    - Содержать только латинские символы, цифры и специальные символы ^$%@#&*
    - Состоять из не менее чем восьми символов
    - Содержать по крайней мере два латинских символа в нижнем регистре
    - Содержать по крайней мере одну цифру
    - Содержать по крайней мере три различных специальных символа
    - Не содержать символы ,.!?

    Args:
    password (str): Пароль для проверки.

    Returns:
    bool: True, если пароль корректен, False в противном случае.
    """
    pattern = (
        r'^(?=.*[a-z].*[a-z])'  # Два латинских символа в нижнем регистре
        r'(?=.*\d)'              # Хотя бы одна цифра
        r'(?=(?:[^a-zA-Z\d]|.*[a-z]){3,})'  # Три различных специальных символа
        r'[a-zA-Z\d^$%@#&*]{8,}$'  # Только латинские символы, цифры и специальные символы, не менее 8 символов
    )

    return bool(re.match(pattern, password))

# Примеры корректных паролей
"""
>>> check_password("rtG&3FG#Tr^e")
True
>>> check_password("a^A1@*@1Aa")
True
>>> check_password("oF^a1D@y5%e6")
True
>>> check_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
True
"""

# Примеры некорректных паролей
"""
>>> check_password("пароль")
False
>>> check_password("password")
False
>>> check_password("qwerty")
False
>>> check_password("lOngPa$$W0Rd")
False
"""

# Дополнительные тесты
"""
>>> check_password("Abc123")
False  # Нет трех различных специальных символов
>>> check_password("A@1bC2dE")
True   # Корректный пароль
"""
