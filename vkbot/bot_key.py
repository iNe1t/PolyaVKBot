#Цвета: PRIMARY/SECONDARY/POSITIVE/NEGATIVE
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api.keyboard as v_key

keyboard = v_key.VkKeyboard(one_time=True, inline=False)
keyboard.add_button(label='Да', color='positive')
keyboard.add_button(label='Нет', color='negative')

