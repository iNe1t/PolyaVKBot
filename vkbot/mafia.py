import config 
import bot_key
import functions
import random
import vk_api.keyboard as v_key

def createMafiaGame(event, gamecounter, playerlist):
    if gamecounter >= 1:
        functions.msg_send(event, "Игра уже начата!")
    else:
        game_name = event.object.message['text'][13:]
        gamecounter = gamecounter + 1
        functions.msg_send(event, "Создана игра " + game_name + "! Для присоединения писать '-мафияконнект'")
    return gamecounter

def KeyboardGenerator(event, playerlist, keylist):
    SomeKeyboard = v_key.VkKeyboard(one_time=True, inline=False)
    for id in keylist:
        SomeKeyboard.add_button(label=str(functions.get_profile(id, event, config.database)[id]['nickname']), color='primary')
    return SomeKeyboard

def GetRole(event, playerlist, keylist, id):
    user_role = playerlist[id]['role']
    return user_role

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
    
def MafiaStart(event, gamecounter, keylist):
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

            
