import config
import functions
import random
import games
import sqlite3

for event in config.longpoll.listen():
    #print(event)
    id = event.object.message['from_id']
    text = event.object.message['text']
    username = config.vk.users.get(user_id=id)[0]['first_name']
    if text in config.hi_list:
        functions.msg_send(event, "Привет, " + config.vk.users.get(user_id=id)[0]['first_name'])
    elif event.object.message['text'] in config.mat_list:
        functions.mat_punisher(event, config.database)
    elif "-фраза" in str(event):
        #Обозначения полов
        #1 — женский
        #2 — мужской
        sex = config.vk.users.get(user_id = id, fields = 'sex')[0]['sex']
        if sex == 2:
            functions.msg_send(event, username + config.phrase_list_male[random.randint(0, config.list_len)])
        if sex == 1:
            functions.msg_send(event, username + config.phrase_list_female[random.randint(0, config.list_len)])
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
    elif "-мут" in str(event):
        functions.msg_send(event, "Если ты читаешь это сообщение, значит ты решил кого-то заткнуть в ВК беседе. Но подумай! Во - первых, сообщение в беседе ВК сказал что нельзя удалять. Во - вторых, если ты не хочешь видеть сообщения человека, почему бы его просто не забанить :) \n Ваш разработчик.")

    
        
    
