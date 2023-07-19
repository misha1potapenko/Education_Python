import logging

logger = logging.getLogger(__name__)


def log_all():
    logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
    logger.info('Немного информации о работе кода')
    logger.warning('Внимание! Надвигается буря!')
    logger.error('Поймали ошибку. Дальше только неизвестность')
    logger.critical('На этом всё')