# -*- coding: utf8 -*-
import requests
import vk_api
import time
from vk_api import VkUpload 
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

tokenbot = "3a667e067e50bfb9432fc218dea67519e041ba7a0366ca1f689d382b87d04ccf020de43d1280fa4ea3fb3"
vk_session = vk_api.VkApi(token=tokenbot)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

upload = VkUpload(vk_session)

attachments = []
attachments.append('doc68106853_535852671')

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
       #Слушаем longpoll, если пришло сообщение то:			
            if event.text.lower() == 'тест': #Если написали заданную фразу
                if event.from_user:
                    vk.messages.send( #Отправляем собщение
                        user_id=event.user_id,
                        random_id=randint(1, 10**17),
                        message='Сигнал получен\n Отвечаю: Бип-Буп-Бип'
                    )
                elif event.from_chat:
                    vk.messages.send( #Отправляем собщение
                        chat_id=event.chat_id,
                        random_id=randint(1, 10**17),
                        message='Сигнал получен\n Отвечаю: Бип-Буп-Бип'
                    )
            elif event.text.lower() == 'менюшка': #Если написали заданную фразу
                if event.from_user:
                    vk.messages.send( #Отправляем собщение
                        user_id=event.user_id,
                        random_id=randint(1, 10**17),
                        message='Выбери: 1, 2 или 3?',
                    )
                elif event.from_chat:
                    vk.messages.send( #Отправляем собщение
                        chat_id=event.chat_id,
                        random_id=randint(1, 10**17),
                        message='Выбери: 1, 2 или 3?',
                        )
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        if event.text.lower() == '1' or event.text.lower() == '2' or event.text.lower() == '3': #Если написали заданную фразу              
                            if event.from_user:
                                vk.messages.send( #Отправляем собщение
                                    user_id=event.user_id,
                                    random_id=randint(1, 10**17),
                                    message='Ты выбрал '+ event.text + '. Я угадал?:)',
                                )
                                break
                            elif event.from_chat:
                                vk.messages.send( #Отправляем собщение
                                    chat_id=event.chat_id,
                                    random_id=randint(1, 10**17),
                                    message='Ты выбрал  '+ event.text + '. Я угадал?:)',
                                )
                                break
                        else:
                            if event.from_user:
                                vk.messages.send( #Отправляем собщение
                                    user_id=event.user_id,
                                    random_id=randint(1, 10**17),
                                    attachment=','.join(attachments),
                                    message='Это шо такое?',
                                )
                                break
                            elif event.from_chat:
                                vk.messages.send( #Отправляем собщение
                                    chat_id=event.chat_id,
                                    random_id=randint(1, 10**17),
                                    attachment=','.join(attachments),
                                    message='Это шо такое?',
                                )
                                break
            else:
                if event.from_user:
                    vk.messages.send( #Отправляем собщение
                        user_id=event.user_id,
                        random_id=randint(1, 10**17),
                        attachment=','.join(attachments),
                        message='Это шо такое?',
                    )
                    break
                elif event.from_chat:
                    vk.messages.send( #Отправляем собщение
                        chat_id=event.chat_id,
                        random_id=randint(1, 10**17),
                        attachment=','.join(attachments),
                        message='Это шо такое?',
                    )
            continue
    time.sleep(1)               