import vk_api
import sqlite3 as sql
import time
import random
 
DATABASE = sql.connect('vkbot.db')
DATABASE.row_factory = lambda cursor, row: row[0]
with DATABASE:
    cur = DATABASE.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `user_info` (`userid` STRING, `user_balance` INTEGER)")
    DATABASE.commit()
 
 
token = "0eb84772aba8b19fa8e61c3c92cd75999e7f8c97932f711bc20c8c59cdd3a7adc9b60f84271f22eba5500"
 
vk = vk_api.VkApi(token=token)
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 200, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages['items'][0]['last_message']['peer_id']
            body = messages['items'][0]['last_message']['text']
            if body.lower() == "начать":
                print("Я,типо, работаю")
                vk.method("messages.send", {"peer_id": id, "message": "Привет", "random_id": random.randint(0)})
    except Exception as E:
        print(E)
        time.sleep(1)