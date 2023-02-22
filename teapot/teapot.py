import logging
import time
from enum import Enum


from logger.logger import logging_teapot_status
from teapot.const import VOLUME, BOILING_TIME, MAX_TEMPERATURE
from teapot.utils import Celsius


class TeapotStatus(Enum):
    ON = 'Включен'
    OFF = 'Выключен'
    BOILED = 'Вскипел'
    STOPPED = 'Остановлен'


class Teapot:
    boiling_time: time.time
    volume: float
    status: TeapotStatus
    water_amount: float
    temperature: Celsius

    def __init__(self):
        self.status = TeapotStatus.OFF
        self.volume = VOLUME
        self.water_amount = 0
        self.temperature = 0

    def __str__(self):
        return {self.temperature: self.temperature}

    @logging_teapot_status
    def turn_on(self):
        """Включение чайника меняет его статус и запускает процесс кипячения"""
        self.status = TeapotStatus.ON
        logging.info('Status = %s' % self.status)
        self.start_boiling()
        return self

    @logging_teapot_status
    def turn_off(self):
        """Выключение чайника меняет его статус и останавливает программу"""
        self.status = TeapotStatus.OFF

    def show_temperature(self):
        """Вывести информацию о температуре"""
        if self.temperature > 100:
            self.temperature = 100
        logging.info('Температура чайника - %s' % self.temperature)

    def pour_water(self, water_amount):
        """Налить воды в чайник """
        if self.water_amount + float(water_amount) <= self.volume:
            self.water_amount += float(water_amount)
        else:
            logging.debug('Водички слишком много, столько не поместится!')

    def start_boiling(self):
        """Процесс кипячения включает себя изменение температуры воды """
        self.boiling_time = BOILING_TIME * (self.water_amount / self.volume)
        while self.temperature < MAX_TEMPERATURE:
            self.temperature += MAX_TEMPERATURE / self.boiling_time
            self.show_temperature()
            time.sleep(1)

        self.status = TeapotStatus.BOILED
        logging.info('Status = %s' % self.status)
        self.turn_off()
