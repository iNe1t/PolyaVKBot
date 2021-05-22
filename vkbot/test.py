import config

database = [{267303926: 'Слава Сливов', 'karma': 0},{477070134: 'Кирилл Некрасов', 'karma': 10}]
for event in config.longpoll.listen():
    print(event)
    # event.object.message['from_id']
    # config.vk.users.get(user_id=id)[0]['first_name']
    if event.type == config.VkBotEventType.MESSAGE_NEW:
        print("ID сообщения:" + str(event.object.message['id']))
    else:
        pass