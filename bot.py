# -*- coding: utf8 -*-
import requests
import vk_api
import vk
import time, sys
from vk_api import VkUpload 
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

def neponatno():
    vk.messages.send(
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        attachment=','.join(attachments),
        message='Это шо такое? Напиши "помощь"',
    )
def pomosh():
    vk.messages.send(  # Отправляем собщение
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        keyboard=open("keyboards/keyboard_start.json", "r", encoding="UTF-8").read(),
        message=""" 
        Возможные команды:
        - Тест
        - Меню
        - Помощь
        """
    )
def test():
    vk.messages.send(  # Отправляем собщение
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        keyboard=open("keyboards/keyboard_start.json", "r", encoding="UTF-8").read(),
        message='Сигнал получен\n Отвечаю: Бип-Буп-Бип'
    )
def valentinka():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print("{} write {}".format(event.user_id, event.text))
            if event.text.lower() == 'да':
                # прохождение анкеты
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    keyboard=open("keyboards/keyboard_menu.json", "r", encoding="UTF-8").read(),
                    message='Спасибо!'
                )
                break
            elif event.text.lower() == 'нет':
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    keyboard=open("keyboards/keyboard_menu.json", "r", encoding="UTF-8").read(),
                    message='Очень жаль'  # и оповещение о предназначении анкеты
                )
                break
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    keyboard=open("keyboards/keyboard_yes_or_no.json", "r", encoding="UTF-8").read(),
                    message='Я не знаю сейчас такой команды. Да или нет?'  # не понял что надо
                )
                
def menu():
    vk.messages.send(  # Отправляем собщение
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        keyboard=open("keyboards/keyboard_menu.json", "r", encoding="UTF-8").read(),
        message='---Меню---',
    )

def backup(users):
    w = open('users', 'w')
    for elem in users:
        values = users[elem]
        w.write(str(elem) + "\n")
        for value in values:
            w.write(str(value) + "\n")
            
        w.write("_\n")
    w.close() 

def check(name):
    for elem in users:
        values = users[elem]
        if name in values:
            return True
            
    return False

                
def addstudent():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print("{} write {}".format(event.user_id, event.text))
            try:
                text = int(event.text)
            except:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    message='Что-то пошло не так, введите ещё раз'
                )
            else:
                if users.get(text) == None or event.user_id not in users[text]:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=randint(1, 10 ** 17),
                        keyboard=open("keyboards/keyboard_yes_or_no.json", "r", encoding="UTF-8").read(),
                        message='Согласны ли вы получать информацию о расписании данной группы каждый день в 6.00 и срочные оповещения от преподавателей?'
                    )
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            print("{} write {}".format(event.user_id, event.text))
                            if event.text.lower() == 'да' and users.get(text) != None:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    message='Принято.'
                                )
                                users[text].append(event.user_id)
                                backup(users)
                                break
                            elif event.text.lower() == 'да' and users.get(text) == None:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    message='Принято.'
                                )
                                users.update({text : [event.user_id]})
                                backup(users)
                                break
                            elif event.text.lower() == 'нет':
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    message='Принято.'
                                )  
                                break
                            else:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    message='Выберите между Да и Нет'
                                )
                
                if check(event.user_id):    
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=randint(1, 10 ** 17),
                        keyboard=open("keyboards/keyboard_rasp.json", "r", encoding="UTF-8").read(),
                        message='Расписание'
                    )
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            print("{} write {}".format(event.user_id, event.text))
                            if event.text.lower() == 'назад':
                                break
                            elif event.text.lower() == 'отписаться от рассылки':
                                for elem in users:
                                    values = users[elem]
                                    if event.user_id in values:
                                        users[elem].remove(event.user_id)
                                        backup(users)
                                        break
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_rasp_2.json", "r", encoding="UTF-8").read(),
                                    message='Отписано'
                                )
                            else:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_rasp.json_2", "r", encoding="UTF-8").read(),
                                    message='Не понимаю, напиши из выбранного (Назад)'
                                )
                else:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=randint(1, 10 ** 17),
                        keyboard=open("keyboards/keyboard_rasp_2.json", "r", encoding="UTF-8").read(),
                        message='Расписание'
                    )
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text.lower() == 'назад':
                                break
                            else:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_rasp.json", "r", encoding="UTF-8").read(),
                                    message='Не понимаю, напиши из выбранного (Назад)'
                                )
                menu()
                break
                
            
                       
        
#  4c186333ef3f740f9af02180d48bebec88587fa76f705287325595523e6a2d0dc4032107976de40d894a8
tokenbot = "4c186333ef3f740f9af02180d48bebec88587fa76f705287325595523e6a2d0dc4032107976de40d894a8"
vk_session = vk_api.VkApi(token=tokenbot)

longpoll = VkLongPoll(vk_session)
vk=vk_session.get_api()

upload = VkUpload(vk_session)

attachments = []
attachments.append('doc68106853_535852671')

users = {}

#_________________________
f = open('users', 'r')
trigger = 1
group = 0
addusr = []
for line in f:
    if line == "":
        break
    
    if trigger == 1:
        group = int(line[:-1])
        trigger = 0
        addusr = []
        
    elif trigger == 0 and line != "_\n":
        addusr.append(int(line[:-1]))
                  
    if line == "_\n":
        trigger = 1
        users[group] = addusr

f.close()
#_________________________

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print("{} write {}".format(event.user_id, event.text))
       #Слушаем longpoll, если пришло сообщение то:	
            if event.text.lower() == 'backup': #Если написали заданную фразу
                backup(users)                                
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=randint(1, 10 ** 17),
                        keyboard=open("keyboards/keyboard_yes_or_no.json", "r", encoding="UTF-8").read(),
                        message='Saved.'
                    )
            if event.text.lower() == 'помощь': #Если написали заданную фразу
                if event.from_user:
                    pomosh()

            elif event.text.lower() == 'тест': #Если написали заданную фразу
                if event.from_user:
                    test()
            elif event.text.lower() == 'меню': #Если написали заданную фразу
                if event.from_user:
                    menu()
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        print("{} write {}".format(event.user_id, event.text))
                        if event.text.lower() == 'валентинка':  # Если написали заданную фразу
                            if event.from_user:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_yes_or_no.json", "r", encoding="UTF-8").read(),
                                    message='Пройти анкету?'
                                )
                                valentinka()
                        elif event.text.lower() == 'расписание':  # Если написали заданную фразу
                            if event.from_user:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    message='Введите номер вашей группы:'
                                )
                                addstudent()
                        elif event.text.lower() == 'назад':  # Если написали заданную фразу
                            if event.from_user:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_start.json", "r", encoding="UTF-8").read(),
                                    message='Стартовое окно'
                                                         )
                            break   
                        elif event.text.lower() == 'помощь':
                            vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_menu.json", "r", encoding="UTF-8").read(),
                                    message="""
                                    Доступные команды:
                                    - Валентинка
                                    - Расписание
                                    - СТО
                                    - Денежное
                                    - Помощь
                                    - Назад"""
                            )
                        else: # Если написали херню
                            if event.from_user:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_menu.json", "r", encoding="UTF-8").read(),
                                    message='Это что такое?'
                                )
                        

            elif event.text.lower() == 'admin_panel':
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    message='Enter Password:'
                )
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        print("{} write {}".format(event.user_id, event.text))
                        if event.text.lower() == 'enter password':
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=randint(1, 10 ** 17),
                                message='Admin panel activated. Greetings, Administrator!'
                            )         
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                print("{} write {}".format(event.user_id, event.text))
                                if event.text.lower() == 'exit':
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        message='Goodbye!'
                                    )  
                                    break
                                if event.text.lower() == 'db':
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        message='{}'.format(users)
                                        )                                      
                                if event.text.lower() == 'offbot':
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        message='Sure. Bot disactivated.'
                                        ) 
                                    sys.exit()
                        break
            else:
                if event.from_user:
                    neponatno()
                    break
           
    time.sleep(1)
