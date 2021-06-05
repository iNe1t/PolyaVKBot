
import config 
import bot_key
import functions
import random
import vk_api.keyboard as v_key

def createMafiaGame(event, gamecounter, playerlist):
    game_name = event.object.message['text'][13:]
    if gamecounter >= 1:
        functions.msg_send(event, "Игра уже начата!")
    else:
        gamecounter = gamecounter + 1
        functions.msg_send(event, "Создана игра " + game_name + "! Для присоединения писать '-мафияконнект'")
    return gamecounter

def KeyboardForKillGenerator(event, playerlist):
    SomeKeyboard = v_key.VkKeyboard(one_time=True, inline=False)
    for player in playerlist:
        SomeKeyboard.add_button(label=str(player), color='primary')
    return SomeKeyboard

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
    
# def MafiaStart(event, gamecounter, playerlist):
#     for player in playerlist:

            
