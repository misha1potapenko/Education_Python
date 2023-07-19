import logging
from other import log_all


logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
