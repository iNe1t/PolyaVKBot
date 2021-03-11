import vk_api
import sqlite3 as sql
import time
import random
 
connection = sql.connect("vkbot.db")
 
q = connection.cursor()
 
q.execute('''CREATE TABLE user_table
(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Name Varchar (100),
User_ID INTEGER,
Balance INTEGER,
Ownment Varchar(100)
)
''')
 
connection.commit()
connection.close()
 
 
token = "вставь сюда свой токен"
 
vk = vk_api.VkApi(token=token)
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 200, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages['items'][0]['last_message']['peer_id']
            body = messages['items'][0]['last_message']['text']
            print("Я,типо, работаю")
    except:
        time.sleep(1)