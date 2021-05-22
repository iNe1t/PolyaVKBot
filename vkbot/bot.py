import config
import functions
import random
import mafia


for event in config.longpoll.listen():
    print(event)
    # event.object.message['from_id']
    # config.vk.users.get(user_id=id)[0]['first_name']
    if event.type == config.VkBotEventType.MESSAGE_NEW:
        if event.object.message['id'] == 0:
            if event.object.message['text'] in config.hi_list:
                functions.msg_send(event, "Привет, " + config.vk.users.get(user_id=event.object.message['from_id'])[0]['first_name'])
            elif event.object.message['text'] in config.mat_list:
                functions.mat_punisher(event, config.database)
            elif "-фраза" in str(event):
                #Обозначения полов
                #1 — женский
                #2 — мужской
                sex = config.vk.users.get(user_id = id, fields = 'sex')[0]['sex']
                if sex == 2:
                    functions.msg_send(event, config.vk.users.get(user_id=id)[0]['first_name'] + config.phrase_list_male[random.randint(0, config.list_len)])
                if sex == 1:
                    functions.msg_send(event, config.vk.users.get(user_id=id)[0]['first_name'] + config.phrase_list_female[random.randint(0, config.list_len)])
            elif '-бан' in str(event):
                functions.ban(event, event.object.message['reply_message']['from_id'])
            elif '-кнбвызов' in str(event):
                games.rock_paper_scissors(event)
            elif "-дайхентай" in str(event):
                functions.send_hmtai(event)
            elif "-беседа" in str(event):
                functions.invited(event)
            elif "-madeby" in str(event):
                functions.msg_send(event, "@ine1t (iNe1t :D)")
            elif "-слава" in str(event):
                functions.create_chat_db(event, config.database)
            elif "-сменитьник" in str(event):
                functions.nick_change(event, config.users_list)
            elif "-действие" in str(event):
                functions.random_action(event)
            elif "-команды" in str(event):
                functions.msg_send(event, "Префикс: - \n Команды: \n бан \n madeby \n сменитьник \n действие \n фраза \n мут \n слава")    
            elif "-мут" in str(event):
                functions.msg_send(event, "Если ты читаешь это сообщение, значит ты решил кого-то заткнуть в ВК беседе. Но подумай! Во - первых, сообщение в беседе ВК сказал что нельзя удалять. Во - вторых, если ты не хочешь видеть сообщения человека, почему бы его просто не забанить :) \n Ваш разработчик.")
            elif "-мафияначать" in str(event):
                config.GAME_COUNTER = mafia.createMafiaGame(event, config.GAME_COUNTER, config.GAME_LIST)
            elif "-мафияконнект" in str(event):  
                mafia.addUserToGame(event, config.GAME_LIST, config.GAME_MAX_PLAYERS) 
            elif "-типоклава" in str(event):
                functions.MsgSendWithKeyboard(event, event.object.message['from_id'], "Клава", mafia.KeyboardForKillGenerator(event, config.GAME_LIST))
        else:
            functions.privatemsg_send(event, "Привет, " + config.vk.users.get(user_id=event.object.message['from_id'])[0]['first_name'] + "! Ты мне написал! Это хорошо. Здесь я ничего не делаю, кроме отправки клавы для игры 'Мафия'. Так что иди в свою беседу и развлекайся со своими друзьями :D")
    else:
        pass
    
        
    
