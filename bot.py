# -*- coding: utf8 -*-
import random

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


def backupteach(teachers):
    w1 = open('teachers', 'w')
    for elem in teachers:
        values = teachers[elem]
        w1.write(str(elem) + "\n")
        for value in values:
            w1.write(str(value) + "\n")
        w1.write("_\n")
    w1.close()


def backupnot(notifications):
    w2 = open('notifications', 'w')
    for elem in notifications:
        values = notifications[elem]
        w2.write(str(elem) + "\n")
        for value in values:
            w2.write(str(value) + "\n")
        w2.write("_\n")
    w2.close()


def check(name):
    for elem in users:
        values = users[elem]
        if name in values:
            return True

    return False


def checkteach(name):
    for elem in teachers:
        values = teachers[elem]
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
                                users.update({text: [event.user_id]})
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
                        message='Расписание в процессе разработки.'
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
                        message='Расписание в процессе разработки.'
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


def addteacher():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            vk.messages.send(
                user_id=event.user_id,
                random_id=randint(1, 10 ** 17),
                message='Введите ключ'
            )
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text.lower() == '123':  # пароль
                        vk.messages.send(
                            user_id=event.user_id,
                            random_id=randint(1, 10 ** 17),
                            message='Верно, введите Ваше ФИО?'
                        )
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                try:
                                    text = event.text
                                except:
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        message='Что-то пошло не так, введите ещё раз'
                                    )
                                else:
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        keyboard=open(
                                            "keyboards/keyboard_yes_or_no.json",
                                            "r", encoding="UTF-8").read(),
                                        message='Согласны внести себя в базу?'
                                    )
                                    for event in longpoll.listen():
                                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                            print("{} write {}".format(event.user_id, event.text))
                                            if event.text.lower() == 'да' and teachers.get(text) != None:
                                                vk.messages.send(
                                                    user_id=event.user_id,
                                                    random_id=randint(1, 10 ** 17),
                                                    message='Принято.'
                                                )
                                                teachers[text].append(event.user_id)
                                                backupteach(teachers)
                                                menu()
                                                break
                                            elif event.text.lower() == 'да' and teachers.get(text) == None:
                                                vk.messages.send(
                                                    user_id=event.user_id,
                                                    random_id=randint(1, 10 ** 17),
                                                    message='Принято.'
                                                )
                                                teachers.update({text: [event.user_id]})
                                                backupteach(teachers)
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
                                    break
                        break


                    else:
                        vk.messages.send(
                            user_id=event.user_id,
                            random_id=randint(1, 10 ** 17),
                            message='Неверно, попробуйте еще раз'
                        )
                        break
            menu()
            break


def notification():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print("{} write {}".format(event.user_id, event.text))
            if checkteach(event.user_id):
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    message='Доступ разрешен, введите ваше сообщение'
                )
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        try:
                            text = event.text
                        except:
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=randint(1, 10 ** 17),
                                message='Что-то пошло не так, введите ещё раз'
                            )
                        else:
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=randint(1, 10 ** 17),
                                keyboard=open(
                                    "keyboards/keyboard_yes_or_no.json",
                                    "r", encoding="UTF-8").read(),
                                message='Сохранить сообщение??'
                            )
                            for event in longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                    print("{} write {}".format(event.user_id, event.text))
                                    if event.text.lower() == 'да' and teachers.get(text) != None:
                                        vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=randint(1, 10 ** 17),
                                            message='Принято.'
                                        )
                                        notifications[text].append(event.user_id)
                                        backupnot(notifications)
                                        break
                                    elif event.text.lower() == 'да' and teachers.get(text) == None:
                                        vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=randint(1, 10 ** 17),
                                            message='Принято.'
                                        )
                                        notifications.update({text: [event.user_id]})
                                        backupnot(notifications)
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
                            break
                break
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    message='Доступ заблокирован, пройдите регистрацию'
                )
                menu()
                break


#d090bb9a6dbdcc87319064acbc76d002c250c122b8da3333e7ba1dfe095d6f6da7777972456feb10a5985 - artem
tokenbot = "1a51e77f3a305327585f0b972bc9c6e8080b77c438b6980069bf1276f311944f06aba18c60dcc19a04321"
vk_session = vk_api.VkApi(token=tokenbot)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

upload = VkUpload(vk_session)

attachments = []
attachments.append('doc68106853_535852671')

users = {}
teachers = {}
notifications = {}
# _________________________
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
# _________________________
f2 = open('notifications', 'r')
trigger = 1
group = 0
addnot = []
for line in f2:
    if line == "":
        break

    if trigger == 1:
        group = str(line[:-1])
        trigger = 0
        addnot = []

    elif trigger == 0 and line != "_\n":
        addnot.append(int(line[:-1]))

    if line == "_\n":
        trigger = 1
        notifications[group] = addnot
f2.close()
#_________________________

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print("{} write {}".format(event.user_id, event.text))
        # Слушаем longpoll, если пришло сообщение то:
        if event.text.lower() == 'backup':  # Если написали заданную фразу
            backup(users)
            backupteach(teachers)
            backupnot(notifications)
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    keyboard=open("keyboards/keyboard_yes_or_no.json", "r", encoding="UTF-8").read(),
                    message='Saved.'
                )
        if event.text.lower() == 'помощь':  # Если написали заданную фразу
            if event.from_user:
                pomosh()

        elif event.text.lower() == 'тест':  # Если написали заданную фразу
            if event.from_user:
                test()
        elif event.text.lower() == 'оповещение':  # Если написали заданную фразу
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    keyboard=open("keyboards/keyboard_yes_or_no.json", "r",
                                  encoding="UTF-8").read(),
                    message='Тест оповещения, нажмите "Да"'
                )
                notification()
        elif event.text.lower() == 'авторизация':  # Если написали заданную фразу
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    keyboard=open("keyboards/keyboard_yes_or_no.json", "r",
                                  encoding="UTF-8").read(),
                    message='Тестовая авторизация, нажмите "Да"'
                )
                addteacher()
        elif event.text.lower() == 'меню':  # Если написали заданную фразу
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
                    elif event.text.lower() == 'оповещение':  # Если написали заданную фразу
                        if event.from_user:
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=randint(1, 10 ** 17),
                                keyboard=open("keyboards/keyboard_yes_or_no.json", "r",
                                              encoding="UTF-8").read(),
                                message='Тест оповещения, нажмите "Да"'
                            )
                            notification()
                    elif event.text.lower() == 'авторизация':  # Если написали заданную фразу
                        if event.from_user:
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=randint(1, 10 ** 17),
                                keyboard=open(
                                    "keyboards/keyboard_yes_or_no.json", "r",
                                    encoding="UTF-8").read(),
                                message='Тестовая авторизация, нажмите "Да"'
                            )
                            addteacher
                    else:  # Если написали херню
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
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        message='{}'.format(teachers)
                                    )
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=randint(1, 10 ** 17),
                                        message='{}'.format(notifications)
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
                        vk.messages.send(
                            user_id=event.user_id,
                            random_id=randint(1, 10 ** 17),
                            message='Denied.'
                        )
        else:
            if event.from_user:
                neponatno()
                break
