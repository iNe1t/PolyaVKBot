import random, vk_api
import vk
import vk_api.vk_api
import hmtai
import config
import bot_key
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType



def rock_paper_scissors(event, key, ts, server):
    username = config.vk.users.get(user_id=id)[0]['first_name']
    text = event.object.message['text']
    enemy_username = config.vk.users.get(user_id=id)[0]['first_name']
    enemy_id = event.object.message['reply_message']['from_id']
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = get_random_id(),
              	    message='Чел, я тут ничего не делаю',
            	    chat_id = event.chat_id
                    )