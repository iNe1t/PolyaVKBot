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