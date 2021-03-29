#Цвета: PRIMARY/SECONDARY/POSITIVE/NEGATIVE
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api.keyboard as v_key

keyboard_choose = v_key.VkKeyboard(one_time=True, inline=False)
keyboard_choose.add_button(label='Да', color='positive') #Камень
keyboard_choose.add_button(label='Нет', color='negative') #Бумага


keyboard_rps = v_key.VkKeyboard(one_time=True, inline=False)
keyboard_rps.add_button(label='✊🏻', color='positive') #Камень
keyboard_rps.add_button(label='✋🏻', color='positive') #Бумага
keyboard_rps.add_button(label='✌🏻', color='positive') #Ножницы

