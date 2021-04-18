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
def antimat(event, on):
    text = event.object.message['text']
    if '$антимат_вкл' in str(event):
        on = True
        msg_send(event, "Антимат включен")
    elif '$антимат_выкл' in str(event):
        on = False
        msg_send(event, "Антимат отключен")
    elif text in config.mat_list and on == True:
            msg_send(event, 'Не ругайся, щука брать')
    else:
        msg_send(event, "Антимат \n Позволяет карать тех, кто обильно выражается. \n Для включения набери '$антимат_вкл'")
    return on
