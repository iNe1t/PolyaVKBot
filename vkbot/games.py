import random, vk_api
import vk
import vk_api.vk_api
import hmtai
import config
import bot_key
import functions
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

def rock_paper_scissors(event):
    id = event.object.message['from_id']
    enemy_id = event.object.message['reply_message']['from_id']
    username = config.vk.users.get(user_id=id)[0]['first_name']
    enemy_username = config.vk.users.get(user_id=enemy_id)[0]['first_name']
    text = event.object.message['text']
    if "$кнбвызов" in str(event):
        functions.msg_send(event, username + " бросил вызов " + enemy_username)