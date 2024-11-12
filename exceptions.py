"""Module providing a custom exception"""


#Пункт 6: Создание пользовательского исключения №1
class TaskCompletionError(Exception):
    """Ошибка завершения задачи"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#Пункт 6: Создание пользовательского исключения №2
class MaximumPriorityError(Exception): # При 'priority' < 2
    """Искусственная ошибка при слишком высоком приорите."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#Пункт 6: Создание пользовательского исключения №3
class MinimumPriorityError(Exception): # При 'priority' > 4
    """Искусственная ошибка при слишком низком приорите."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TaskNotFoundError(Exception):
    """Исключение, когда задача не найдена."""

class InvalidDeadlineError(Exception):
    """Исключение, если формат дедлайна недопустим или неверен."""

class DeadlineInPastError(Exception):
    """Исключение, если дедлайн установлен на дату в прошлом."""

class TaskAlreadyCompletedError(Exception):
    """Исключение, когда задача уже выполнена."""

class TaskExecutionError(Exception):
    """Исключение для ошибки выполнения задачи."""
