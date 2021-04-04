import config 

def msg_send(event,key, ts, server, text):
    config.vk.messages.send(
                    key = key,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = server,
                    ts = ts,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id
                    )
def ban(event, key, ts, server):
    id_for_ban = event.object.message['reply_message']['from_id']
    config.vk.messages.removeChatUser(
        user_id=id_for_ban,
        chat_id=event.chat_id,
        random_id = config.get_random_id()
    )