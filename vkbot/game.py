import config 
import bot_key
import functions
import random
import mafia
import time

def GameProcess(event, playerlist, keylist, rolescount):
    mafia.StartAndSendRoles(event, config.GAME_KEYLIST)
    functions.msg_send(event, "Игра в Мафию Началась!")
    check_keys = []
    time.sleep(2)
    if len(check_keys) == len(keylist):
        functions.msg_send(event, "Ночь окончена! Мертвые: " + mafia.makeDeadList(event, config.GAME_LIST, config.GAME_KEYLIST))
    while rolescount["Мирный"] > 0 and (rolescount["Мафия"] >= 1 or rolescount["Мирный"]):
        day = 1
        functions.msg_send(event, "Наступила "+ day + "-я ночь. Сообщения разосланы ролям. Действуйте!")
        if event.object.id  > 0 or event.object.message['id'] > 0:
            check_keys = mafia.RolesAction(event, config.GAME_KEYLIST)