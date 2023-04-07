import logging

# создаем объект логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# создаем обработчик, который записывает логи в файл
handler = logging.FileHandler('app.log')
handler.setLevel(logging.DEBUG)

# создаем форматтер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# добавляем обработчик в логгер
logger.addHandler(handler)