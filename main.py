# -*- coding: utf-8 -*-
import vk_api
import RPi.GPIO as GPIO
import time
# Подключаем конфиг
from conf import *


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)


vk = vk_api.VkApi(login, password)
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

def main():
    while True:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            if (str(item[u'user_id']) == idBoss):
                write_msg(item[u'user_id'],u'Слушаюсь, хозяин')
                if item[u'body'] == '+light':
                    write_msg(item[u'user_id'],u'Включаю свет')
                    GPIO.output(LED,True)
                if item[u'body'] == '-light':
                    write_msg(item[u'user_id'],u'Выключаю свет')
                    GPIO.output(LED,False)
                if item[u'body'] == '?light':
                    write_msg(item[u'user_id'], GPIO.input(LED))
            else:
                write_msg(item[u'user_id'],u'Пшёл на')
        time.sleep(1)

if __name__ == '__main__':
    main()



