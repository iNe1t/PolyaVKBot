import config
import random
import hmtai

def invited(event):
    #db = sqlite3.connect('chat_db.db')
    #cursor = db.cursor()
    #cursor.execute("CREATE TABLE IF NOT EXISTS chat_db(id INTEGER, nickname TEXT)")
    users = config.vk.messages.getChat(chat_id=event.chat_id, fields='nickname')
    print(users)

def msg_send(event, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id
                    )
def ban(event):
    id_for_ban = event.object.message['reply_message']['from_id']
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
def create_chat_db(event, listik, some_database):
    if listik:
        print("already exist")
    else:
        chat_name = config.vk.messages.getChat(chat_id = event.object.gr)
        members = config.vk.messages.getConversationMembers(peer_id = event.object.message['peer_id'], group_id = event.group_id)['profiles']
        def add_user(listik):
            for user in members:
                name = user['first_name'] + ' ' + user['last_name']
                id = user['id']
                listik.append({id:name})
            return listik
        print(add_user(config.users_list))
def mat_punisher(event):
    return "you"
def mute():
    return "you"
def nick_change(event, some_list):
    nick = event.object.message['text'][12:]
    for profile in some_list:
        if event.object.message['from_id'] in profile.keys():
            profile[event.object.message['from_id']] = nick
    print(some_list)
        

