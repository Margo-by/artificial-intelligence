import pprint
import logging

from logger import setup_logger
setup_logger()

def get_premise_name_from_number(number):
    """
    Получение названия посылки по её номеру.
    :param number: Номер посылки.
    :return: Название посылки.
    """
    return premises[int(number)]  # Используем индекс для получения названия из списка

def get_premise_number_from_name(name):
    """
    Получение номера посылки по её названию.
    :param name: Название посылки.
    :return: Номер посылки, если найдено, иначе None.
    """
    if name in premises:
        return premises.index(name)  # Индекс в списке возвращает номер
    else:
        return None  # Если не найдено, возвращаем None

def get_premises_value_number_from_premise_number_and_value_name(premise_number, premise_value_name):
    """
    Получение номера значения посылки по её номеру и имени значения.
    :param premise_number: Номер посылки.
    :param premise_value_name: Имя значения.
    :return: Номер значения, если найдено, иначе None.
    """
    values = premises[premise_number]  # Получаем все значения для данной посылки
    if premise_value_name in values:
        return values.index(premise_value_name)  # Находим индекс значения в списке
    else:
        return None  # Если не найдено, возвращаем None

def get_premises_from_rule_number(number):
    """
    Получение посылок для конкретного правила.
    :param number: Номер правила.
    :return: Посылки, связанные с данным правилом.
    """
    return tuple(map(tuple, rule[0]))  # Преобразуем посылки в кортежи

# Основные атрибуты и их возможные значения
attributes = ["назначение", "сезон", "материал", "стиль", "тип", "категория"]

attributes_values = [
    ["быт", "спорт", "рабочая", "деловая"],  # Примеры значений для "назначения"
    ["зима", "лето"],  # Примеры значений для "сезона"
    ["кожа", "мех", "шёлк", "лён"],  # Примеры значений для "материала"
    ["повседневный", "официальный"],  # Примеры значений для "стиля"
    ["верх", "низ"],  # Примеры значений для "типа"
    ["пальто", "куртка", "брюки"],  # Примеры значений для "категории"
]

# Набор правил, описывающих зависимости между посылками и заключениями
rules = [
            [[[2, 0]], [1, 0]], 
            [[[2, 1]], [1, 0]], 
            [[[2, 2]], [1, 1]], 
            [[[2, 3]], [1, 1]], 
            [[[1, 0], [0, 3]], [5, 0]], 
            [[[1, 1]], [5, 1]], 
            [[[1, 0], [0, 2]], [5, 1]], 
            [[[5, 0]], [3, 1]], 
            [[[5, 1]], [3, 0]], 
            [[[4, 0]], [0, 4]]
]

# Создаем множество всех доступных заключений
conclusions = sorted({tuple(rule[1]) for rule in rules})

# Создаем множество всех посылок из правил
premises = sorted({tuple(map(tuple, rule[0])) for rule in rules})

# Создаем словарь ключ-заключение, где значение - это список правил, приводящих к заключению
conclusion_to_group_of_rules_map = {}

for rule_number, rule in enumerate(rules):
    conclusion = tuple(rule[1])  # Заключение из посылок

    # Проверяем, существует ли уже этот ключ
    if conclusion in conclusion_to_group_of_rules_map:
        conclusion_to_group_of_rules_map[conclusion].add(rule_number)  # Добавляем правило в соответствующий список
    else:
        conclusion_to_group_of_rules_map[conclusion] = {rule_number}  # Если ключа нет, создаем новый с множеством

# Преобразуем множества в списки для удобства
conclusion_to_group_of_rules_map = {key: list(value) for key, value in conclusion_to_group_of_rules_map.items()}

# Логирование данных для отладки
logging.info(f"Список правил: \n{pprint.pformat(rules)}")
logging.info(f"Заключения: \n{pprint.pformat(conclusions)}")
logging.info(f"Посылки: \n{pprint.pformat(premises)}")
logging.info("Список правил на проверку для каждого заключения: \n"
             f"{pprint.pformat(conclusion_to_group_of_rules_map)}")
