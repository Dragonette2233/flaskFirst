import logging
import os

# создаем объект логгера

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# создаем обработчик, который записывает логи в файл
# handler = logging.FileHandler('app.log', mode='w')
handler_s = logging.StreamHandler()
handler_s.setLevel(logging.DEBUG)
handler_f = logging.FileHandler('app.log', mode='w')

# создаем форматтер для логов
formatter = logging.Formatter('%(asctime)s-%(levelname)s | %(message)s', datefmt='%I:%M:%S')
handler_f.setFormatter(formatter)
handler_s.setFormatter(formatter)

# добавляем обработчик в логгер
logger.addHandler(handler_s)
# logger.addHandler(handler_f)