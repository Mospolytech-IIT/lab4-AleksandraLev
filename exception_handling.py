"""Module to demonstrate exceptions and exception handling."""
import datetime
from exceptions import (
    TaskNotFoundError,
    TaskCompletionError,
    MaximumPriorityError,
    MinimumPriorityError,
    InvalidDeadlineError,
    DeadlineInPastError,
    TaskAlreadyCompletedError,
    TaskExecutionError
)



#Пункт 1. Функция 1.
def add_task(task_list, task_name, priority):
    """Добавляет задачу в список задач"""
    if not task_name:
        raise ValueError("Название задачи не может быть пустым.")
    if priority < 1 or priority > 5:
        raise ValueError("Приоритет задачи должен быть в диапазоне от 1 до 5.")

    task_id = len(task_list) + 1
    task_list[task_id] = {
        'name': task_name,
        'priority': priority,
        'deadline': None,
        'subtasks': [],
        'completed': False
    }

#Пункт 1. Функция 2.
def validate_task(task_list, task_id):
    """Проверяет по индексу существует ли задача."""
    if task_id not in task_list:
        raise LookupError(f"Задача под идексом {task_id} не найдена.")

#Пункт 2.
def remove_task(task_list, task_id):
    """Удаляет задачу по индексу."""
    try:
        del task_list[task_id]
        print(f"Задача удалена под индексом {task_id}.")
    except KeyError:
        print("Ошибка: Такой задачи не существует!")

#Пункт 3.
def sort_tasks_by_priority(task_list):
    """Сортирует задачи"""
    try:
        sorted_tasks = sorted(task_list.items(),
                              key=lambda item: item[1].get('priority', 5))
        task_list = dict(sorted_tasks)
        print("Задачи успешно отсортированы по приоритетности.")
    except (ValueError, KeyError, TypeError) as e:
        print(f"Ошибка при сортировке задач: {e}")
    finally:
        print("Завершение сортироваки задач.")

#Пункт 4. Функция 1.
def edit_task(task_list, task_id, new_name):
    """Функция, которая изменяет название задачи."""
    try:
        task_list[task_id]['name'] = new_name
        print(f"Название задачи под индексом {task_id} изменено на '{new_name}'.")

    except KeyError as e:
        print(f"Ошибка: {e}")

    except ValueError as e:
        print(f"Ошибка: {e}")

    except TypeError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Операция по изменению названия задачи завершена.")

#Пункт 4. Функция 2.
def sorted_tasks_by_name(task_list):
    """Сортирует задачи по алфавиту."""
    try:
        sorted_tasks = sorted(task_list['tasks'].items(), key=lambda item: item[1]['name'])
        print(sorted_tasks)
    except KeyError as e:
        print(f"Ошибка: {e}")

    except ValueError as e:
        print(f"Ошибка: {e}")

    except TypeError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение сортироваки задач.")


#Пункт 4. Функция 3.
def set_task_deadline(task_list, task_id, deadline):
    """Назначает дедлайн по задаче."""
    try:
        # Проверяем, существует ли задача с данным ID
        if task_id not in task_list['tasks']:
            raise KeyError(f"Задача с ID {task_id} не найдена.")

        # Проверяем формат даты
        try:
            deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError as e:
            text = "Неверный формат даты. Используйте формат YYYY-MM-DD."
            raise InvalidDeadlineError(text) from e

        # Проверяем, что дедлайн не в прошлом
        current_date = datetime.datetime.now()
        if deadline_date < current_date:
            raise DeadlineInPastError("Дедлайн не может быть установлен в прошлом.")

        # Присваиваем дедлайн задаче
        task_list['tasks'][task_id]['deadline'] = deadline
        print(f"Дедлайн для задачи с ID {task_id} успешно установлен на {deadline}.")

    except KeyError as ke:
        print(f"Ошибка: {ke}")
    except InvalidDeadlineError as ide:
        print(f"Ошибка: {ide}")
    except DeadlineInPastError as dpe:
        print(f"Ошибка: {dpe}")

#Пункт 5.
def execute_task(task_list, task_id):
    """Отмечает задачу как выполненную."""
    try:
        if task_id not in task_list:
            raise TaskNotFoundError(f"Задача под индексом {task_id} не найдена.")
        if task_list[task_id].get('completed', False):
            raise TaskAlreadyCompletedError(f'Задача "{task_list[task_id]['name']}" уже выполнена.')
        task_list[task_id]['completed'] = True
        print(f"Задача '{task_list[task_id]['name']}' успешно выполнена.")
    except TaskNotFoundError as e:
        print(f"Ошибка: {e}")
    except TaskAlreadyCompletedError as e:
        print(f"Ошибка: {e}")


#Пункт 7.
def mark_task_complete(task_list, task_id):
    """Функция, которая отмечает задачу как выполненную и использует пользовательские исключения."""
    try:
        task = task_list.get(task_id)

        # Проверяем, не завершена ли уже задача
        if task['completed']:
            # Если задача уже завершена, выбрасываем исключение
            raise TaskCompletionError(f"Задача под индексом {task_id} уже выполнена.")
        if task['priority'] > 4:
            text = f"Очень низкая приоритеность у задачи под индексом {task_id}"
            raise MinimumPriorityError (text)
        if task['priority'] < 2:
            text = f"Очень высокая приоритеность у задачи под индексом {task_id}"
            raise MaximumPriorityError (text)

        # Помечаем задачу как выполненную
        task['completed'] = True
        print(f"Задача под индексом {task_id} помечена как выполненная.")

    except TaskCompletionError as e:
        # Обработка ошибки: выводим сообщение
        print(f"Ошибка: {e.message}")
        # Логика восстановления
        task['completed'] = False
        print(f"Задача с ID {task_id} восстановлена в исходное состояние.")
    except MaximumPriorityError as e:
        print(f"Ошибка: {e.message}")
    except MinimumPriorityError as e:
        print(f"Ошибка: {e.message}")
    finally:
        print(f"Функция завершена для задачи под индексом {task_id}. Проверка завершена.")


#Пункт 8. Функция 1.
def create_sample_tasks(task_list):
    """Функция создания примера задач 1"""
    try:
        task_list[1] = {
            'name': "Помыть кота",
            'priority': 3,
            'deadline': None,
            'subtasks': [],
            'completed': False
        }
        task_list[2] = {
            'name': "Пропылесосить гречку",
            'priority': 1,
            'deadline': None,
            'subtasks': [],
            'completed': False
        }
        task_list[3] = {
            'name': "Сделать уроки",
            'priority': 5,
            'deadline': None,
            'subtasks': [],
            'completed': False
        }
        print("Задачи созданы.")
    except TaskExecutionError as e:
        print(f"Ошибка при создании задач: {e}.")

#Пункт 8. Функция 2.
def simulate_assignment_error_1(task_list):
    """Функция создания примера задачи 2"""
    try:
        add_task(task_list, "Поймать голубя", 0)
    except TaskExecutionError as e:
        print(f"Ошибка назначения задачи: {e}")

#Пункт 8. Функция 3.
def simulate_assignment_error_2(task_list):
    """Функция создания примера задачи 2"""
    try:
        add_task(task_list, "", 1)
    except TaskExecutionError as e:
        print(f"Ошибка назначения задачи: {e}")

#Пункт 8. Функция 4.
def simulate_deadline_error(task_list):
    """Функция моделирования ошибки дедлайна"""
    try:
        set_task_deadline(task_list, 1, "2022-01-01")
    except (InvalidDeadlineError, DeadlineInPastError) as e:
        print(f"Ошибка установки дедлайна: {e}")
