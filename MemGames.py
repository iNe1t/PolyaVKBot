import bot
import config
def mafia(config.KEY, config.SERVER, config.TS):
    for event in longpoll.listen():
        text = event.object.message['text']
        msg_id = event.object.message['id']
        username = vk.users.get(user_id=id)[0]['first_name']
        if '$мафияначать' in str(event) :
                    vk.messages.send(
                            key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                            server = config.SERVER,
                            ts = config.TS,
                            random_id = get_random_id(),
                            message= "🧠Команды🧠 \n $непозор \n $дайхентай \n $фраза \n $позор \n $бан",
                            chat_id = event.chat_id
                            )


