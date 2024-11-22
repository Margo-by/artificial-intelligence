from itertools import product
from collections.abc import Iterable
from logger import setup_logger
import logging
setup_logger()

# Функция для поиска ключа по значению
def get_key_by_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None  # Если значение не найдено

# Проверка, что все элементы из правила присутствуют в s_res
def is_rule_satisfied(rule, s_res):
    # Преобразуем s_res в множество для упрощения поиска
    s_res_set = {tuple(item) for item in s_res}  # Преобразуем элементы s_res в кортежи и создаем множество

    # Проверяем, что каждый элемент из rule присутствует в s_res_set
    for item in rule:
        if item not in s_res_set:
            return False  # Если хотя бы одного элемента нет, правило не выполнено
    
    return True  # Если все элементы найдены, правило выполнено


# для лабы 3

def format_attribute(attr_index, value, attributes, attributes_values):
    """
    Форматирует атрибут для вывода пользователю. Это может быть полезно для отображения результатов.

    :param attr_index: Индекс атрибута в списке attributes.
    :param value: Значение атрибута (или None, если не задано).
    :param attributes: Список атрибутов.
    :param attributes_values: Список значений для каждого атрибута.
    :return: Отформатированная строка с названием атрибута и его значением.
    """
    if value is None:
        return f"{attributes[attr_index]}: Не задано"  # Если значение не задано
    return f"{attributes[attr_index]}: {attributes_values[attr_index][value]} ({value})"  # Если значение задано


def format_condition(cond, attributes, attributes_values):
    """
    Форматирует условие из правила для отображения пользователю.

    :param cond: Условие в формате [атрибут, значение], например [2, 0].
    :param attributes: Список атрибутов.
    :param attributes_values: Список значений для каждого атрибута.
    :return: Строка с описанием условия.
    """
    attr_index = cond[0]  # Индекс атрибута
    value_index = cond[1]  # Индекс значения для атрибута
    return f"{attributes[attr_index]}: {attributes_values[attr_index][value_index]} ({value_index})"  # Получаем название атрибута и значение по индексу


def combinate(arrays):
    """
    Создаёт множество всех комбинаций элементов из n массивов.
    возвращает список кортежей

    :param arrays: Списки (или массивы), из которых формируются комбинации.
    :return: Множество всех комбинаций.
    """
    combination = list(product(*arrays))
    flatten_combination=flatten(combination)
    return flatten_combination

# array=[[1,2,3]]
# arrays=[[1,2,3],[4,5,6]]
# print(combinate(arrays))

def flatten(data):
    logging.debug(f"current element: {data}")
    new_data=[]
    while len(data)==1:
        logging.debug("delete unnessesery breaks")
        data=flatten(data[0])

    for i,item in enumerate(data):
        if isinstance(item, Iterable):
            logging.debug(f"element{item} in number {i} is Iterable")
            new_item=flatten(item)
            logging.debug(f"new item: {new_item}")
            new_data.append(new_item)            
        else:
            logging.debug(f"element{item} in number {i} is not Iterable")
            new_data.append(item)  
    logging.debug(f"new data: {new_data}")        
    return new_data






