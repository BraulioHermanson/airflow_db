from time import sleep
from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_atv():
    logger.info("primeira atividades")
    sleep(2)

def segunda_atv():
    logger.info("segunda atividades")
    sleep(2)

def terceira_atv():
    logger.info("terceira atividades")
    sleep(2)

def pipeline():
    primeira_atv()
    segunda_atv()
    terceira_atv()

if __name__ == "__main__":
    pipeline()