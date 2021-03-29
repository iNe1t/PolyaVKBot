import random, vk_api
import vk
import vk_api.vk_api
import hmtai
import config
import sqlite3 as sql
import bot_key
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

DATABASE = sql.connect('vk_mafia.db')
with DATABASE:
    cur = DATABASE.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `mafia` (`userid` INTEGER, `role` STRING)")

vk_session = vk_api.VkApi(token='44da98deef5d1311d2ca99d31e942a14c7e04db89630e25ce9e4775c9a3279d6ec7474e5974d582adbe74')
longpoll = VkBotLongPoll(vk_session, '203143170')
vk = vk_session.get_api()

global game
game = False
# Это клава (не кока)
#keyboard = bot_key.keyboard.get_keyboard()
for event in longpoll.listen():
#Переменные 
    text = event.object.message['text']
    msg_id = event.object.message['id']
    id = event.object.message['from_id']
    username = vk.users.get(user_id=id)[0]['first_name']
#Куча функций (да, я знаю, что можно и из файла, но я встал из-за кругового импорта(во всем виноват event >:( )))
    def rock_paper_scissors(KEY, SERVER, TS, id, type, text, msg_id, username, game):
        if '$кнбпомощь' in str(event):
            vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message= "Игра 'Камень-Ножницы-Бумага' \n Чтобы вызвать кого-то, ответьте на сообщение с командой '$кнбвызов', Сообщение будет отправлено оппоненту, дождитесь его ответа.",
                        chat_id = event.chat_id
                        )
        elif '$кнбвызов' in str(event):
            reply_msg_id = event.object.message['reply_message']['from_id']
            enemy_username = vk.users.get(user_id=reply_msg_id)[0]['first_name']
            vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message= "Вы бросили вызов игроку " + enemy_username,
                        chat_id = event.chat_id,
                        )
            vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message= username + " бросил вам вызов. Принимаете его?",
                        user_id = reply_msg_id,
                        id = 1,
                        keyboard = bot_key.keyboard_choose.get_keyboard()
                        )




    def mafia(KEY, SERVER, TS, id, type, text, msg_id, username, game):
            mafia_roles = ['Мирный', 'Мафия', 'Доктор', 'Шериф']
            role = mafia_roles[random.randint(0, len(mafia_roles)-1)]
            if '$мафияначать' in str(event):
                if game == True:
                    vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message= username + " Игра уже начата!",
                        chat_id = event.chat_id
                        )
                cur.execute(f"INSERT INTO `mafia` VALUES ('{id}', '{role}')")
                db = cur.execute("SELECT * FROM mafia").fetchall()
                game = True
                print(db)
                vk.messages.send(
                        key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = SERVER,
                        ts = TS,
                        random_id = get_random_id(),
                        message= username + " начинает игру Мафия! \n Пишите $мафияконнект, чтобы присоединиться.",
                        chat_id = event.chat_id
                        )
            elif '$мафияконнект' in str(event):
                existance = cur.execute("SELECT role FROM mafia WHERE userid=?", (id,)).fetchall()
                db = cur.execute("SELECT * FROM mafia").fetchall()
                if existance:
                    vk.messages.send(
                            key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                            server = SERVER,
                            ts = TS,
                            random_id = get_random_id(),
                            message= username + " уже в игре!",
                            chat_id = event.chat_id
                            )
                else:
                    print(db) 
                    cur.execute(f"INSERT INTO `mafia` VALUES ('{id}', '{role}')")
                    vk.messages.send(
                            key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                            server = SERVER,
                            ts = TS,
                            random_id = get_random_id(),
                            message= username + " присоединяется к игре",
                            chat_id = event.chat_id
                            )
            else:
                vk.messages.send(
                            key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                            server = SERVER,
                            ts = TS,
                            random_id = get_random_id(),
                            message= "За командами к игре 'Мафия' пишите '$команды'",
                            chat_id = event.chat_id
                            )

    
# Тело самого бота
    if event.type == VkBotEventType.MESSAGE_NEW:
        if msg_id == 1:
            vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message='Чел, я тут ничего не делаю',
            	    chat_id = event.chat_id
                    )
        if '$непозор' in str(event):
            def depozor(text):
                reply_msg_id = event.object.message['reply_message']['from_id']
                print("ID юзера для позора:" + str(reply_msg_id))
                config.pozor_list.remove(reply_msg_id)
                return vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message='Пользователь больше не опозорен!',
            	    chat_id = event.chat_id
                    )
            depozor(text)
        elif (id in config.pozor_list) and event.from_chat:
            vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message=username + ', иди в жопу',
            	    chat_id = event.chat_id
                    )
        elif 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message='Привет, ' + username +"!",
            	    chat_id = event.chat_id
                    )
        elif '$бан' in str(event):
            def ban(text):
                reply_msg_id = event.object.message['reply_message']['from_id']
                config.ban_list.append(reply_msg_id)
                vk.messages.removeChatUser(
                    chat_id=event.chat_id,
                    user_id=reply_msg_id,
                )
                return vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message='Пользователь забанен!',
            	    chat_id = event.chat_id
                    )
            ban(text)
        elif '$позор' in str(event):
            def pozor(text):
                reply_msg_id = event.object.message['reply_message']['from_id']
                print("ID юзера для позора: " + str(reply_msg_id))
                config.pozor_list.append(reply_msg_id)
                print("Добавлен в позор лист")
                return vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message='Пользователь опозорен!',
            	    chat_id = event.chat_id
                    )
            pozor(text)
        elif '$фраза' in str(event) :
            sex = vk.users.get(user_id=id, fields='sex')[0]['sex']
            if sex == 2:
                vk.messages.send(
                        key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = config.SERVER,
                        ts = config.TS,
                        random_id = get_random_id(),
                        message=username + config.phrase_list_male[random.randint(0, config.list_len)],
                        chat_id = event.chat_id
                        )
            elif sex == 1:
                vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message=username + config.phrase_list_female[random.randint(0, config.list_len)],
            	    chat_id = event.chat_id
                    )
        elif '$дайхентай' in str(event) :
                link = config.hmtai_categories[random.randint(0, config.hc_len)]
                picturelink = hmtai.useHM("v2", link)
                vk.messages.send(
                        key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = config.SERVER,
                        ts = config.TS,
                        random_id = get_random_id(),
                        message= "Рандом " + str(link) + " из архивов: " + str(picturelink),
                        chat_id = event.chat_id
                        )
        elif '$команды' in str(event) :
                vk.messages.send(
                        key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = config.SERVER,
                        ts = config.TS,
                        random_id = get_random_id(),
                        message= "🧠Команды🧠 \n $непозор \n $дайхентай \n $фраза \n $позор \n $бан \n $мафияначать \n $мафияконнект \n $кнб \n $кнбвызов",
                        chat_id = event.chat_id
                        )
        elif '$мафия' in str(event) :
            mafia(config.KEY, config.SERVER, config.TS, id, type, text, msg_id, username, game)
        elif '$кнб' in str(event) :
            rock_paper_scissors(config.KEY, config.SERVER, config.TS, id, type, text, msg_id, username, game)