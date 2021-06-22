import config 
import bot_key
import functions
import random
import vk_api.keyboard as v_key


def makeDeadList(event, playerlist, keylist):
    deadlist = ""
    for key in keylist:
        if GetRole(event, playerlist, keylist, key)['is_killed'] == 1:
            deadlist = str(deadlist + functions.get_profile(key, event, config.database)['nickname'] + ' ' )
    return deadlist


# создать игру "Мафия"
def createMafiaGame(event, gamecounter, playerlist):
    if gamecounter >= 1:
        functions.msg_send(event, "Игра уже начата!")
    else:
        game_name = event.object.message['text'][13:]
        gamecounter = gamecounter + 1
        functions.msg_send(event, "Создана игра " + game_name + "! Для присоединения писать '-мафияконнект'")
    return gamecounter


# генерирует  клавиатуру с людьми
def KeyboardGenerator(event, playerlist, keylist):
    SomeKeyboard = v_key.VkKeyboard(one_time=True, inline=False)
    for id in keylist:
        SomeKeyboard.add_button(label=str(functions.get_profile(id, event, config.database)[id]['nickname']), color='primary', payload=id)
    return SomeKeyboard


# получить роль пользователя
def GetRole(event, playerlist, keylist, id):
    user_role = playerlist[id]['role']
    return user_role


# подключение пользователя к игре
def addUserToGame(event, playerlist, max_players, keylist):
    print("Нынешние ключи: " + str(keylist))
    if len(playerlist) == max_players:
        functions.msg_send(event, "Достигнуто максимальное число игроков!")
    else:
        username = functions.get_profile(event.object.message['from_id'], event, config.database)[event.object.message['from_id']]['nickname']
        roles = ["Мирный", "Мафия", "Доктор", "Дон", "Шериф"]
        if event.object.message['from_id'] in keylist:
            functions.msg_send(event, "Ты уже в игре, дурашка!")
        else:
            playerlist.update([(event.object.message['from_id'], {'role':roles[random.randint(0, len(roles) - 1)] ,'is_killed':False})])
            keylist = list(playerlist) 
        print("Нынешний плеерлист: " + str(playerlist))
        print("Ключи: "+ str(keylist))    
        functions.msg_send(event, str(playerlist))      
    return keylist
# начать игру
def StartAndSendRoles(event, keylist):
    # для начала отправим сообщения пользователям в зависимости от их ролей
    for player in keylist:
        if GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, player).lower() == "мирный":
            functions.privatemsg_send(event, "Ты просто Мирный. Молись, чтобы тебя не убили :D", int(player))
        elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, player).lower() == "мафия":
            functions.MsgSendWithKeyboard(event, int(player), "Ты - Мафия! Выбирай кого ты убьешь этой ночью", KeyboardGenerator(event, config.GAME_LIST, config.GAME_KEYLIST))
        elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, player).lower() == "доктор":
            functions.MsgSendWithKeyboard(event, int(player), "Ты - Доктор! Выбирай кого ты вылечишь этой ночью", KeyboardGenerator(event, config.GAME_LIST, config.GAME_KEYLIST))
        elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, player).lower() == "дон":
            functions.MsgSendWithKeyboard(event, int(player), "Ты - Дон! Выбирай того, кого хочешь проверить на Шерифа", KeyboardGenerator(event, config.GAME_LIST, config.GAME_KEYLIST))
        elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, player).lower() == "шериф":
            functions.MsgSendWithKeyboard(event, int(player), "Ты - Шериф! Выбирай того, кого хочешь проверить на Мафия", KeyboardGenerator(event, config.GAME_LIST, config.GAME_KEYLIST))


# Функции для ролей
# Убить игрока
def kill(event, victim_id, gamelist):
    is_killed = gamelist[int(victim_id)]['is_killed']
    if is_killed == True:
        return functions.privatemsg_send(event, "Игрок уже убит. Кто-то опередил вас.", event.object.message['from_id'])
    else:
        gamelist[int(victim_id)]['is_killed'] = 1
        return functions.privatemsg_send(event, "Игрок успешно убит", event.object.message['from_id'])


# Вылечить игрока
def heal(event, victim_id, gamelist):
    is_killed = gamelist[int(victim_id)]['is_killed']
    if is_killed == False:
        return functions.privatemsg_send(event, "Игрок еще живой", event.object.message['from_id'])
    else:
        gamelist[int(victim_id)]['is_killed'] = 0
        return functions.privatemsg_send(event, "Игрок успешно вылечен", event.object.message['from_id'])


# Проверка на Дона
def don_check(event, victim_id, gamelist):
    role = gamelist[int(victim_id)]['role'].lower()
    if role == 'дон':
        return functions.privatemsg_send(event, "Данный игрок является Доном", event.object.message['from_id'])
    else:
        return functions.privatemsg_send(event, "Данный игрок не является Доном", event.object.message['from_id'])


# Проверка на Шерифа
def sheriff_check(event, victim_id, gamelist):
    role = gamelist[int(victim_id)]['role'].lower()
    if role == 'шериф':
        return functions.privatemsg_send(event, "Данный игрок является Шерифом", event.object.message['from_id'])
    else:
        return functions.privatemsg_send(event, "Данный игрок не является Шерифом", event.object.message['from_id'])


# Действия в зависимости от роли
def RolesAction(event, keylist):
    check_keys = []
    if GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, event.object.message['from_id']).lower() == 'мафия':
        kill(event, event.object.message['payload'], config.GAME_LIST)
        check_keys.append(str(event.object.message['from_id']))
    elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, event.object.message['from_id']).lower() == 'доктор':
        heal(event, event.object.message['payload'], config.GAME_LIST)
        check_keys.append(str(event.object.message['from_id']))
    elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, event.object.message['from_id']).lower() == 'дон':
        sheriff_check(event, event.object.message['payload'], config.GAME_LIST)
        check_keys.append(str(event.object.message['from_id']))
    elif GetRole(event, config.GAME_LIST, config.GAME_KEYLIST, event.object.message['from_id']).lower() == 'шериф':
        don_check(event, event.object.message['payload'], config.GAME_LIST)
        check_keys.append(str(event.object.message['from_id']))
    else:
        functions.privatemsg_send(event, "Я тебя не понял! Введи ник жертвы и я сделаю все в зависимости от твоей роли.", event.object.message['from_id'])
    check_keys = set(check_keys)
    return check_keys
    

            
