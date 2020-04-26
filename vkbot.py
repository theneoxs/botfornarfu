# -*- coding: utf8 -*-
import random
import sys
import numpy as np

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType


class VkBot:

    def __init__(self, user_id):
        print("\nAdd bot")
        self.USER_ID = event.user_id

        self.COMMANDS = ["тест", "помощь", "валентинка", "меню", "расписание", "admin panel", "игра"]

    def new_message(self, message):
        if message.lower() == self.COMMANDS[0]:
            return "Сигнал получен\n Отвечаю: Бип-Буп-Бип"
            # (vk.method("messages.send",
            #       {'user_id': event.user_id, 'message': "Сигнал получен\n Отвечаю: Бип-Буп-Бип",
            #        'random_id': random.randint(0, 2048)}))
        if message.lower() == self.COMMANDS[1]:
            return """
                        Возможные команды:
                        - Тест
                        - Меню
                        - Помощь
                        """
        if message.lower() == self.COMMANDS[2]:
            (vk.method("messages.send",
                       {'user_id': event.user_id, 'message': "Желаете пройти анкету?",
                        'random_id': random.randint(0, 2048)}))
            self.valentinka()
        if message.lower() == self.COMMANDS[3]:
            return """
                Доступные команды:
                - Валентинка
                - Расписание
                - СТО
                - Денежное
                - Помощь
                - Назад
                - Игра"""
        if message.lower() == self.COMMANDS[4]:
            (vk.method("messages.send",
                       {'user_id': event.user_id, 'message': "Введите номер группы?",
                        'random_id': random.randint(0, 2048)}))
            self.addstudent()
        if message.lower() == self.COMMANDS[5]:
            (vk.method("messages.send",
                       {'user_id': event.user_id, 'message': "Enter Password:",
                        'random_id': random.randint(0, 2048)}))
            self.admin_panel()
        if message.lower() == self.COMMANDS[6]:
            (vk.method("messages.send",
                       {'user_id': event.user_id, 'message': "Хотите сыграть в игру?",
                        'random_id': random.randint(0, 2048)}))
            self.game()

        if message.lower() != self.COMMANDS:
            return "Воспользуйтесь командой 'Помощь'"

    def admin_panel(self):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text.lower() == 'enter password':
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Admin panel activated. Greetings, Administrator!",
                                'random_id': random.randint(0, 2048)}))
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text.lower() == 'exit':
                                (vk.method("messages.send",
                                           {'user_id': event.user_id, 'message': "Goodbye!",
                                            'random_id': random.randint(0, 2048)}))
                                return
                            if event.text.lower() == 'db':
                                (vk.method("messages.send",
                                           {'user_id': event.user_id, 'message': '{}'.format(users),
                                            'random_id': random.randint(0, 2048)}))

                            if event.text.lower() == 'offbot':
                                (vk.method("messages.send",
                                           {'user_id': event.user_id, 'message': "Sure. Bot disactivated.",
                                            'random_id': random.randint(0, 2048)}))
                                sys.exit()
                    return
                else:
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Denied!",
                                'random_id': random.randint(0, 2048), }))
                    return

    def backup(self):
        w = open('users', 'w')
        for elem in users:
            values = users[elem]
            w.write(str(elem) + "\n")
            for value in values:
                w.write(str(value) + "\n")

            w.write("_\n")
        w.close()

    def check(self, name):
        for elem in users:
            values = users[elem]
            if name in values:
                return True

        return False

    def valentinka(self):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text.lower() == 'да':
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Спасибо!",
                                'random_id': random.randint(0, 2048)}))
                    return
                if event.text.lower() == 'нет':
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Очень жаль",
                                'random_id': random.randint(0, 2048)}))
                    return
                else:
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Введите 'Да' или 'Нет'",
                                'random_id': random.randint(0, 2048), 'attachments': ','.join(attachments)}))

    def addstudent(self):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                try:
                    text = int(event.text)
                except:
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Что-то пошло не так",
                                'random_id': random.randint(0, 2048)}))
                else:
                    if users.get(text) == None or event.user_id not in users[text]:
                        (vk.method("messages.send",
                                   {'user_id': event.user_id,
                                    'message': "Согласны ли вы получать информацию о расписании данной группы каждый день в 6.00 и срочные оповещения от преподавателей?",
                                    'random_id': random.randint(0, 2048)}))
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                if event.text.lower() == 'да' and users.get(text) != None:
                                    (vk.method("messages.send",
                                               {'user_id': event.user_id, 'message': "Принято",
                                                'random_id': random.randint(0, 2048)}))
                                    users[text].append(event.user_id)
                                    self.backup()
                                    return
                                elif event.text.lower() == 'да' and users.get(text) == None:
                                    (vk.method("messages.send",
                                               {'user_id': event.user_id, 'message': "Принято",
                                                'random_id': random.randint(0, 2048)}))
                                    users.update({text: [event.user_id]})
                                    self.backup()
                                    return
                                elif event.text.lower() == 'нет':
                                    (vk.method("messages.send",
                                               {'user_id': event.user_id, 'message': "Принято",
                                                'random_id': random.randint(0, 2048)}))
                                    return
                                else:
                                    (vk.method("messages.send",
                                               {'user_id': event.user_id, 'message': "Введите 'Да' или 'Нет'",
                                                'random_id': random.randint(0, 2048)}))
                    if self.check(event.user_id):
                        (vk.method("messages.send",
                                   {'user_id': event.user_id, 'message': "Расписание в процессе разработки.",
                                    'random_id': random.randint(0, 2048)}))
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                if event.text.lower() == 'назад':
                                    return
                                elif event.text.lower() == 'отписаться от рассылки':
                                    for elem in users:
                                        values = users[elem]
                                        if event.user_id in values:
                                            users[elem].remove(event.user_id)
                                            self.backup(users)
                                            return
                                        (vk.method("messages.send",
                                                   {'user_id': event.user_id,
                                                    'message': "Отписано",
                                                    'random_id': random.randint(0, 2048)}))
                                else:
                                    (vk.method("messages.send",
                                               {'user_id': event.user_id,
                                                'message': "Не понимаю, напиши из выбранного (Назад)",
                                                'random_id': random.randint(0, 2048)}))
                    else:
                        (vk.method("messages.send",
                                   {'user_id': event.user_id, 'message': "Расписание в процессе разработки.",
                                    'random_id': random.randint(0, 2048)}))
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                if event.text.lower() == 'назад':
                                    return
                                else:
                                    (vk.method("messages.send",
                                               {'user_id': event.user_id,
                                                'message': "Не понимаю, напиши из выбранного (Назад)",
                                                'random_id': random.randint(0, 2048)}))

    def game(self):
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text.lower() == 'да':
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Замечательно, давай начнем!\n"
                                                                     "Введите число от 1 до 100, чье число окажется ближе к рандомному числу которое я создам, тот и победил.",
                                'random_id': random.randint(0, 2048)}))
                    self.gameplay()
                if event.text.lower() == 'нет':
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Очень жаль, заходи еще!",
                                'random_id': random.randint(0, 2048)}))
                    return
                return

    def gameplay(self):

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:


                try:
                    a = random.randint(1, 100)  # рандомное число
                    b = random.randint(1, 100)  # число загаданная ботом
                    c = int(event.text)  # число игрока
                except:
                    (vk.method("messages.send",
                               {'user_id': event.user_id, 'message': "Введите число, а не что-то другое!",
                                'random_id': random.randint(0, 2048)}))

                else:
                    if abs(a - b) > abs(a - c):  # побед игрок
                        (vk.method("messages.send",
                                   {'user_id': event.user_id, 'message': "Рандомное число - " + str(a) + "\n" +
                                                                         "Ваше число - " + str(c) + "\n" +
                                                                         "Мое число - " + str(b) + "\n" +
                                                                         "Вы победили! Сыграем еще раз?\n",
                                    'random_id': random.randint(0, 2048)}))
                        self.game()
                        return

                    if abs(a - b) < abs(a - c):  # побед бот
                        (vk.method("messages.send",
                                   {'user_id': event.user_id, 'message': "Рандомное число - " + str(a) + "\n" +
                                                                         "Ваше число - " + str(c) + "\n" +
                                                                         "Мое число - " + str(b) + "\n" +
                                                                         "Я победил! Сыграем еще раз?\n",
                                    'random_id': random.randint(0, 2048)}))
                        self.game()
                        return

                    if abs(a - b) == abs(a - c):  # ничья
                        (vk.method("messages.send",
                                   {'user_id': event.user_id, 'message': "Рандомное число - " + str(a) + "\n" +
                                                                         "Ваше число - " + str(c) + "\n" +
                                                                         "Мое число - " + str(b) + "\n" +
                                                                         "Ничья! Сыграем еще раз?\n",
                                    'random_id': random.randint(0, 2048)}))
                        self.game()
                        return

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# 18d28ce73b747190a67dcc56a20017e3f8363de4fe3e37ebaf2d09023aae7b00b62280a4dd6190f587022 - main
# 1a51e77f3a305327585f0b972bc9c6e8080b77c438b6980069bf1276f311944f06aba18c60dcc19a04321 - test
tokenbot = "1a51e77f3a305327585f0b972bc9c6e8080b77c438b6980069bf1276f311944f06aba18c60dcc19a04321"
vk = vk_api.VkApi(token=tokenbot)

longpoll = VkLongPoll(vk)

upload = VkUpload(vk)
bots = {}
attachments = []
attachments.append('doc68106853_535852671')

users = {}

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        print(f'New message from', event.user_id, end='')

        if bots.get(event.user_id) == None:
            bots[event.user_id] = VkBot(event.user_id)

        write_msg(event.user_id, bots[event.user_id].new_message(event.text))

        print('Text: ', event.text)
        print("-------------------")
        print(bots)
