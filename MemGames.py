import bot
import config
from vk_api.utils import get_random_id

def mafia(config.KEY, config.SERVER, config.TS):
    for event in longpoll.listen():
        user_id = event.object.message['from_id']
        text = event.object.message['text']
        msg_id = event.object.message['id']
        username = vk.users.get(user_id=id)[0]['first_name']
        mafia_players = {}
        if '$мафияначать' in str(event) :
                    vk.messages.send(
                            key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                            server = config.SERVER,
                            ts = config.TS,
                            random_id = get_random_id(),
                            message= "Игра Мафия начинается! \n Пишите $мафияконнект, чтобы присоединиться.",
                            chat_id = event.chat_id
                            )


