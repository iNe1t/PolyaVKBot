import config
import random
import hmtai
import bot_key
import json
import os

#1 — женский;
#2 — мужской;
#0 — пол не указан.
def invited(event):
    users = config.vk.messages.getChat(chat_id=event.chat_id, fields='nickname')
    print(users)

def get_username(id, event, database):
    username = ''
    for profile in database:
        if id in profile.keys():
            print(profile)
            if id in profile:
                username = profile[id]['nickname']
    return username
     

def msg_send(event, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id,
                    )
def privatemsg_send(event, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
                    peer_id = event.object.message['from_id']
                    )
                    
def MsgSendWithKeyboard(event,receiver_id, text, somekeyboard):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id,
                    peer_id = receiver_id,
                    keyboard = somekeyboard.get_keyboard()
                    )



def ban(event, id_for_ban):
    config.vk.messages.removeChatUser(
        user_id=id_for_ban,
        chat_id=event.chat_id,
        random_id = config.get_random_id()
    )



def send_private_msg(event, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id
                    )



def send_hmtai(event):
    category = config.hmtai_categories[random.randint(0, config.hc_len)]
    link = hmtai.useHM(version="v2", category=str(category))
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message="Немного " + category + " вам в ленту",
            	    chat_id = event.chat_id,
                    attachment= str(link)
                    )



def create_chat_db(event, listik):
    if listik:
        msg_send(event, "База данных уже существует!")
    else:
        members = config.vk.messages.getConversationMembers(peer_id = event.object.message['peer_id'], group_id = event.group_id)['profiles']
        def add_user(listik):
            for user in members:
                name = user['first_name'] + ' ' + user['last_name']
                id = user['id']
                karma_counter = 0
                listik.append({id:{'nickname': name,"karma":karma_counter, 'role': "none", 'is_killed': False}})
            print(listik)
            return msg_send(event, listik) 
        print(add_user(config.database))



def mat_punisher(event, database):
    username = ''
    id = int(event.object.message['from_id'])
    for profile in database:
        if event.object.message['from_id'] in profile.keys():
            print(profile)
            if id in profile:
                username = profile[id]['nickname']
                profile[id]['karma'] = profile[id]['karma'] + 1
                if profile[id]['karma'] >= 3:
                    ban(event, id)
                    profile[id]['karma'] = 0
    return msg_send(event, username + ', не ругайся, щука брать')

def nick_change(event, some_list):
    nick = event.object.message['text'][12:]
    for profile in some_list:
        if event.object.message['from_id'] in profile.keys():
            profile[event.object.message['from_id']]['nickname'] = nick
    msg_send(event, some_list)

def random_action(event):
    if int(event.object.message['reply_message']['from_id']) < 0:
        msg_send(event, "Меня трогать нинада!")
    else:
        name1 = get_username(event.object.message['from_id'], event, config.database)
        name1_sex = sex = config.vk.users.get(user_ids = event.object.message['from_id'], fields = "sex")[0]["sex"]

        name2 = get_username(event.object.message['reply_message']['from_id'], event, config.database)
        name2_sex = config.vk.users.get(user_ids = event.object.message['reply_message']['from_id'], fields = "sex")[0]["sex"]
        if int(name1_sex) == 2:
            msg_send(event, name1 + " " + config.action_list_male[random.randint(0, config.alm_lenght)] + " " + name2)
        else:
            msg_send(event, name1 + " " +  config.action_list_male[random.randint(0, config.alfm_lenght)] + " " + name2)
    
    
        

