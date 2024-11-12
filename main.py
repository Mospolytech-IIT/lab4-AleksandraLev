"""Модуль, демонстрирующий работу программы (функции и исключения)"""


from exceptions import (
    TaskCompletionError,
    MaximumPriorityError,
    TaskNotFoundError,
    InvalidDeadlineError,
    DeadlineInPastError,
    TaskAlreadyCompletedError,
    TaskExecutionError
)
from exception_handling import (
    add_task,
    validate_task,
    remove_task,
    sort_tasks_by_priority,
    edit_task,
    sorted_tasks_by_name,
    set_task_deadline,
    execute_task,
    mark_task_complete,
    create_sample_tasks,
    simulate_assignment_error_1,
    simulate_assignment_error_2,
    simulate_deadline_error
)

def main():
    """Функция, которая последовательно вызывает все вышесозданные функции."""
    # Инициализируем пустой список задач
    task_list = {}

    # Создаём пример задач
    try:
        create_sample_tasks(task_list)
    except TaskExecutionError as e:
        print(f"Ошибка при создании примерных задач: {e}")

    # Пробуем добавить новую задачу
    try:
        add_task(task_list, "Пойти на пробежку", 3)
    except ValueError as e:
        print(f"Ошибка при добавлении задачи: {e}")

    # Проверяем валидацию задачи
    try:
        validate_task(task_list, 1)
    except LookupError as e:
        print(f"Ошибка проверки задачи: {e}")

    # Пробуем удалить задачу
    try:
        remove_task(task_list, 1)
    except KeyError as e:
        print(f"Ошибка удаления задачи: {e}")

    # Пробуем сортировать задачи по приоритету
    sort_tasks_by_priority(task_list)

    # Пробуем изменить название задачи
    try:
        edit_task(task_list, 2, "Приготовить обед")
    except KeyError as e:
        print(f"Ошибка редактирования задачи: {e}")

    # Сортируем задачи по алфавиту
    sorted_tasks_by_name(task_list)

    # Пробуем установить дедлайн для задачи
    try:
        set_task_deadline(task_list, 2, "2024-12-31")
    except (InvalidDeadlineError, DeadlineInPastError, KeyError) as e:
        print(f"Ошибка установки дедлайна: {e}")

    # Пробуем выполнить задачу
    try:
        execute_task(task_list, 2)
    except (TaskNotFoundError, TaskAlreadyCompletedError) as e:
        print(f"Ошибка выполнения задачи: {e}")

    # Отмечаем задачу как выполненную с обработкой пользовательского исключения
    try:
        mark_task_complete(task_list, 2)
    except (TaskCompletionError, MaximumPriorityError, MaximumPriorityError) as e:
        print(f"Ошибка при завершении задачи: {e}")

    # Пробуем вызвать ошибки добавления задач и дедлайна для демонстрации
    simulate_assignment_error_1(task_list)
    simulate_assignment_error_2(task_list)
    simulate_deadline_error(task_list)

    print("Все задачи были успешно вызваны и обработаны.")

if __name__ == "__main__":
    main()
