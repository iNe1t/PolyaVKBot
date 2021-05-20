import config 
import bot_key
import functions
import random


def createMafiaGame(event, gamecounter, playerlist):
    game_name = event.object.message['text'][13:]
    if gamecounter >= 1:
        functions.msg_send(event, "Игра " + game_name + " уже начата!")
    else:
        gamecounter = gamecounter + 1
        functions.msg_send(event, "Создана игра " + game_name + "! Для присоединения писать '-мафияконнект'")
    return gamecounter
def addUserToGame(event, playerlist, max_players):
    if len(playerlist) == max_players:
        functions.msg_send(event, "Достигнуто максимальное число игроков!")
    else:
        id = event.object.message['from_id']
        username = config.vk.users.get(user_id=id)[0]['first_name']
        roles = ["Мирный", "Мафия", "Доктор", "Дон", "Шериф"]
        is_in_game = False
        for i in playerlist:
            if id in i:
                functions.msg_send(event, "Ты уже в игре, дурашка!")
                is_in_game = True
                break
        if is_in_game == False:
            playerlist.append({id:username, "role":roles[random.randint(0, len(roles) - 1)], 'is_killed': False})           
    return functions.msg_send(event, playerlist)
def MafiaStart(event, gamecounter, playerlist):
    for player in playerlist:
        
            
