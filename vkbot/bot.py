import config
import functions
import random
import games
import sqlite3

for event in config.longpoll.listen():
    id = event.object.message['from_id']
    text = event.object.message['text']
    username = config.vk.users.get(user_id=id)[0]['first_name']
    if (text in config.mat_list and config.on == True) or "$антимат" in str(event):
        functions.antimat(event, config.on)
    elif text in config.hi_list:
        functions.msg_send(event, "Привет, " + config.vk.users.get(user_id=id)[0]['first_name'])
    elif "$фраза" in str(event):
        #Обозначения полов
        #1 — женский
        #2 — мужской
        sex = config.vk.users.get(user_id = id, fields = 'sex')[0]['sex']
        if sex == 2:
            functions.msg_send(event, username + config.phrase_list_male[random.randint(0, config.list_len)])
        if sex == 1:
            functions.msg_send(event, username + config.phrase_list_female[random.randint(0, config.list_len)])
    elif '$бан' in str(event):
        functions.ban(event)
    elif '$кнбвызов' in str(event):
        games.rock_paper_scissors(event)
    elif "$дайхентай" in str(event):
        functions.send_hmtai(event)
    elif "$беседа" in str(event):
        functions.invited(event)
        
    
