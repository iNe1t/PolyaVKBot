import config
import functions
import random
import mafia
import yaml
import game
# yaml.load(dict) - из str в dict

# try:

for event in config.longpoll.listen():
    print(event)
    if event.type == config.VkBotEventType.MESSAGE_NEW :
        if event.object.id  == 0 or event.object.message['id'] == 0:
            # username = config.vk.users.get(user_id=id)[0]['first_name']
            if event.object.message['text'] in config.hi_list:
                functions.msg_send(event, "Привет, " + functions.get_profile(event.object.message['from_id'], event, config.database)[event.object.message['from_id']]['nickname'])
            elif event.object.message['text'].lower() in config.mat_list:
                functions.mat_punisher(event, config.database)
            elif "-фраза" in str(event):
                #Обозначения полов
                #1 — женский
                #2 — мужской
                sex = config.vk.users.get(user_id=event.object.message['from_id'], fields= 'sex')[0]['sex']
                if sex == 2:
                    functions.msg_send(event, functions.get_profile(event.object.message['from_id'], event, config.database)[
                                        event.object.message['from_id']]['nickname'] + config.phrase_list_male[random.randint(0, config.list_len)])
                if sex == 1:
                    functions.msg_send(event, functions.get_profile(event.object.message['from_id'], event, config.database)[
                                        event.object.message['from_id']]['nickname'] + config.phrase_list_female[random.randint(0, config.list_len)])
            elif '-бан' in str(event):
                functions.ban(
                    event, event.object.message['reply_message']['from_id'])
            elif "-дайхентай" in str(event):
                functions.send_hmtai(event)
            elif "-беседа" in str(event):
                functions.invited(event)
            elif "-madeby" in str(event):
                functions.msg_send(event, "@ine1t (iNe1t :D)")
            elif "-слава" in str(event):
                functions.create_chat_db(event, config.database)
            elif "-сменитьник" in str(event):
                functions.nick_change(event, config.database)
            elif "-действие" in str(event):
                functions.random_action(event)
            elif "-команды" in str(event):
                functions.msg_send(
                    event, "Префикс: - \n Команды: \n бан \n madeby \n сменитьник \n действие \n фраза \n мут \n слава")
            elif "-мут" in str(event):
                functions.msg_send(event, "Если ты читаешь это сообщение, значит ты решил кого-то заткнуть в ВК беседе. Но подумай! Во - первых, сообщение в беседе ВК сказал что нельзя удалять. Во - вторых, если ты не хочешь видеть сообщения человека, почему бы его просто не забанить :) \n Ваш разработчик.")
            # Для мафии
            elif "-мафияначать" in str(event):
                config.GAME_COUNTER = mafia.createMafiaGame(
                    event, config.GAME_COUNTER, config.GAME_LIST)
            elif "-мафияконнект" in str(event):
                config.GAME_KEYLIST = mafia.addUserToGame(
                    event, config.GAME_LIST, config.GAME_MAX_PLAYERS, config.GAME_KEYLIST)
            elif "-мафиястарт" in str(event):
                game.GameProcess(event, config.GAME_LIST, config.GAME_KEYLIST, config.ROLES_COUNTER)
            elif "-типоклава" in str(event):
                functions.MsgSendWithKeyboard(
                    event, event.object.message['from_id'], "Клава", mafia.KeyboardGenerator(event, config.GAME_LIST, config.GAME_KEYLIST))
        else:
            mafia.RolesAction(event,config.GAME_KEYLIST)
    else:
        pass

# except Exception as error:
#     functions.msg_send(event, "Я упал. Пиши разрабу @ine1t")
#     print(error)

        
    
