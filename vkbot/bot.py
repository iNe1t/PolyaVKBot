import config
import functions
import random


for event in config.longpoll.listen():
    id = event.object.message['from_id']
    text = event.object.message['text']
    username = config.vk.users.get(user_id=id)[0]['first_name']
    if text in config.hi_list:
        functions.msg_send(event, config.KEY, config.TS, config.SERVER, "Привет, " + config.vk.users.get(user_id=id)[0]['first_name'])
    elif "$фраза" in str(event):
        #Обозначения полов
        #1 — женский
        #2 — мужской
        sex = config.vk.users.get(user_id = id, fields = 'sex')[0]['sex']
        if sex == 2:
            functions.msg_send(event, config.KEY, config.TS, config.SERVER, username + config.phrase_list_male[random.randint(0, config.list_len)])
        if sex == 1:
            functions.msg_send(event, config.KEY, config.TS, config.SERVER, username + config.phrase_list_female[random.randint(0, config.list_len)])
    elif '$бан' in str(event):
        functions.ban(event, config.KEY, config.TS, config.SERVER)

    #elif "$фраза" in str(event):

    #elif "$фраза" in str(event):

    #elif "$фраза" in str(event):

    #elif "$фраза" in str(event):
