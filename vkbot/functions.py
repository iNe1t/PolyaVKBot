import config
import random
import hmtai
#1 — женский;
#2 — мужской;
#0 — пол не указан.
def invited(event):
    users = config.vk.messages.getChat(chat_id=event.chat_id, fields='nickname')
    print(users)



def msg_send(event, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id
                    )
def privatemsg_send(event,receiver_id, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id,
                    peer_id = receiver_id
                    )



def ban(event, id_for_ban):
    config.vk.messages.removeChatUser(
        user_id=id_for_ban,
        chat_id=event.chat_id,
        random_id = config.get_random_id()
    )



def send_private_msg(event, text):
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message=text,
            	    chat_id = event.chat_id
                    )



def send_hmtai(event):
    category = config.hmtai_categories[random.randint(0, config.hc_len)]
    link = hmtai.useHM(version="v2", category=str(category))
    config.vk.messages.send(
                    key = config.KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = config.SERVER,
                    ts = config.TS,
                    random_id = config.get_random_id(),
              	    message="Немного " + category + " вам в ленту",
            	    chat_id = event.chat_id,
                    attachment= str(link)
                    )



def create_chat_db(event, listik):
    if listik:
        msg_send(event, "База данных уже существует!")
    else:
        members = config.vk.messages.getConversationMembers(peer_id = event.object.message['peer_id'], group_id = event.group_id)['profiles']
        def add_user(listik):
            for user in members:
                name = user['first_name'] + ' ' + user['last_name']
                id = user['id']
                karma_counter = 0
                listik.append({id:name, "karma":karma_counter})
            print(listik)
            return msg_send(event, listik) 
        print(add_user(config.database))



def mat_punisher(event, database):
    id = int(event.object.message['from_id'])
    username = config.vk.users.get(user_id=id)[0]['first_name']
    for i in database:
        print(i)
        if id in i:
            i['karma'] = i['karma'] + 1
            if i['karma'] >= 3:
                ban(event, id)
                i['karma'] = 0
    return msg_send(event, config.vk.users.get(user_id=event.object.message['from_id'])[0]['first_name'] + ', не ругайся, щука брать')



def nick_change(event, some_list):
    nick = event.object.message['text'][12:]
    for profile in some_list:
        if event.object.message['from_id'] in profile.keys():
            profile[event.object.message['from_id']] = nick
    msg_send(event, some_list)



def random_action(event):
    name1 = config.vk.users.get(user_ids = event.object.message['from_id'], fields = "sex")[0]["first_name"]
    name1_sex = sex = config.vk.users.get(user_ids = event.object.message['from_id'], fields = "sex")[0]["sex"]

    name2 = config.vk.users.get(user_ids = event.object.message['reply_message']['from_id'], fields = "sex")[0]["first_name"]
    name2_sex = config.vk.users.get(user_ids = event.object.message['reply_message']['from_id'], fields = "sex")[0]["sex"]
    if int(name1_sex) == 2:
        msg_send(event, name1 + " " + config.action_list_male[random.randint(0, config.alm_lenght)] + " " + name2)
    else:
        msg_send(event, name1 + " " +  config.action_list_male[random.randint(0, config.alfm_lenght)] + " " + name2)
    
    
        

