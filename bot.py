import random, vk_api
import vk
import vk_api.vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
import hmtai
import phrases
import requests

vk_session = vk_api.VkApi(token='0eb84772aba8b19fa8e61c3c92cd75999e7f8c97932f711bc20c8c59cdd3a7adc9b60f84271f22eba5500')
longpoll = VkBotLongPoll(vk_session, '203143170')
vk = vk_session.get_api()
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()
KEY = 'd8c36cdf12cccf78e77d0881b6a0b81ecedc999f'
SERVER = 'https://lp.vk.com/wh203143170'
TS = '1'
global pozor_list
pozor_list = []

global ban_list
ban_list = []

for event in longpoll.listen():

    id = event.object.message['from_id']
    type = event.type
    text = event.object.message['text']
    msg_id = event.object.message['id']
    username = vk.users.get(user_id=id)[0]['first_name']

    if event.type == VkBotEventType.MESSAGE_NEW:
        if '$непозор' in str(event):
            def depozor(text):
                reply_msg_id = event.object.message['reply_message']['from_id']
                print("ID юзера для позора:" + str(reply_msg_id))
                pozor_list.remove(reply_msg_id)
                print("Удален из позор листа")
                print(pozor_list)
                print(reply_msg_id in pozor_list)
                return vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message='Пользователь больше не опозорен!',
            	    chat_id = event.chat_id
                    )
            depozor(text)
        elif (id in pozor_list) and event.from_chat:
            vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message=username + ', иди в жопу',
            	    chat_id = event.chat_id
                    )
        elif 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message='Привет, ' + username +"!",
            	    chat_id = event.chat_id
                    )
        elif '$бан' in str(event):
            def ban(text):
                reply_msg_id = event.object.message['reply_message']['from_id']
                print("ID юзера для бана: " + str(reply_msg_id))
                ban_list.append(reply_msg_id)
                print("добавлен в бан лист")
                vk.messages.removeChatUser(
                    chat_id=event.chat_id,
                    user_id=reply_msg_id,
                )
                return vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message='Пользователь забанен!',
            	    chat_id = event.chat_id
                    )
            ban(text)
        elif '$позор' in str(event):
            def pozor(text):
                reply_msg_id = event.object.message['reply_message']['from_id']
                print("ID юзера для позора: " + str(reply_msg_id))
                pozor_list.append(reply_msg_id)
                print("Добавлен в позор лист")
                print(pozor_list)
                print(reply_msg_id in pozor_list)
                return vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message='Пользователь опозорен!',
            	    chat_id = event.chat_id
                    )
            pozor(text)
        elif '$фраза' in str(event) :
            sex = vk.users.get(user_id=id, fields='sex')[0]['sex']
            if sex == 2:
                vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message=username + phrases.phrase_list_male[random.randint(0, phrases.list_len)],
                        chat_id = event.chat_id
                        )
            elif sex == 1:
                vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message=username + phrases.phrase_list_female[random.randint(0, phrases.list_len)],
            	    chat_id = event.chat_id
                    )
        elif '$дайхентай' in str(event) :
                link = phrases.hmtai_categories[random.randint(0, phrases.hc_len)]
                print(link)
                picturelink = hmtai.useHM("v2", link)
                vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message= "Рандом " + str(link) + " из архивов: " + str(picturelink),
                        chat_id = event.chat_id
                        )