import os
from typing import Callable


def clear_environ(rule: Callable):
    """
    Очищает переменные окружения, переменные для очистки определяет переданная
    функция rule.
    """
    # Ключи из os.environ копируются в новый tuple, чтобы не менять объект
    # os.environ во время итерации.
    for name in filter(rule, tuple(os.environ)):
        os.environ.pop(name)
