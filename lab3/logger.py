import logging

def setup_logger():
    logger = logging.getLogger()  # Получаем корневой логгер
    logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования для всех сообщений

    # Проверяем, не добавлены ли уже обработчики (чтобы избежать дублирования)
    if not logger.hasHandlers():
        # Формат для сообщений
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Обработчик для записи в файл
        file_handler = logging.FileHandler('log1.txt', mode='w', encoding='utf-8')
        file_handler.setLevel(logging.INFO)  # Уровень для записи в файл
        file_handler.setFormatter(formatter)  # Применяем формат


        # Обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Уровень для вывода в консоль
        console_handler.setFormatter(formatter)  # Применяем формат

        # Добавляем обработчики в логгер
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)


