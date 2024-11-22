from math import e

from data import (
    rules,                         # Список правил
    conclusion_to_group_of_rules_map, #словарь ключ-заключение, где значение - это список правил, приводящих к заключению
)
from utils import combinate, flatten
from logger import setup_logger
import logging
setup_logger()

class ExpertSystem:
    """
    Класс ExpertSystem реализует логику экспертной системы на основе правил.
    """

    def __init__(self):
        """

        Инициализация экспертной системы. Словарь user_data хранит значения атрибутов, введенные пользователем.

        self.rules - все доступные правила
        """
        self.rules=rules
        logging.info("Система инициализирована.")

    def infer_attribute(self, t_goals, conditions=[], depth=0,max_depth=1):
        """
        выполняет поиск всех посылок приводящих к заданному заключению, анализируя правила и посылки.
        goal: текущая цель (аттрибут, значение)
        t_goals: порядок проверки целей (контекстный стек)

        :param depth: Глубина рекурсии (используется для логирования, чтобы отслеживать, насколько глубоко мы зашли в рекурсию).
        :return: Обновленные данные пользователя, если атрибуты успешно выведены.
        """

        indent = "  " * depth  # Отступ для логирования в зависимости от текущей глубины
        logging.info(f"Глубина: {depth}")
        logging.info(f"{indent} контекстный стек : {t_goals}")
        goal=t_goals[len(t_goals)-1]
        logging.info(f"{indent} ищем посылки для : {goal}")

        if depth<=max_depth:
            #находим правила, порождающие текущую цель (аттрибут, значение)
            if tuple(goal) in conclusion_to_group_of_rules_map:
                applicable_rules=conclusion_to_group_of_rules_map[tuple(goal)]
                logging.info(f"{indent}Найдено применимых правил: {len(applicable_rules)}, проходим по ним по порядку")
                conditions_for_rule=conditions.copy()
                for rule_number in applicable_rules:
                    premises=rules[rule_number][0]
                    logging.info(f"{indent}Проверяем посылки: {premises}")
                    arrays=[]


                    for i,premise in enumerate(premises):
                        new_goal=premise
                        new_t_goals=t_goals.copy()
                        new_t_goals.append(new_goal)

                        #массив групп условий, которые равносильны друг другу
                        premise_conditions=([tuple(premise)])
                        #условия, которые приводят к тому, что текущая цель (атрибут, значение) выполняется, тоесть они равносильны premise
                        new_conditions = self.infer_attribute( new_t_goals, conditions,depth+1)
                        logging.info(f"поиск вернул {new_conditions}")
                        if new_conditions != None:
                            premise_conditions.extend(new_conditions)
                        arrays.append(premise_conditions)
                        logging.info(f"условия приводящие к {premise} (равносильные ему) {arrays[i]}")


                    #так как у нас для выполнения правила необходимо чтоб все посылки выполнились, 
                    #то мы должны построить декартово произведение, где i-ое множество, это массив условий, 
                    #каждое из которых, равносильно выполнению посылки i + сама посылка

                    possible_premis_for_rule=combinate(arrays)


                    logging.info(f"условия равносильные правилу номер {rule_number}, а именно"+
                        f"{rules[rule_number][0]} -> {rules[rule_number][1]} это {possible_premis_for_rule}" )
                    conditions_for_rule.append(possible_premis_for_rule)
                logging.info(f"условия равносильные выполнимости текущей цели"+
                    f"{goal} это {conditions_for_rule}" )

                return conditions_for_rule

            else:
                return None
        else:
            return None


    def run_system(self,goal):
        """
        Выполняет вывод для заданного (целевого атрибута, его значения).
        пример goal=[5, 0]
        """
        
        t_goals=[]
        t_goals.append(goal)
        conditions=flatten(self.infer_attribute(t_goals))
        return conditions




# expert_system = ExpertSystem()
# conditions=expert_system.run_system([5, 0])
# logging.info(f"варинты посылок, приводящих к цели: {conditions}")