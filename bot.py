# Скрипт был создан автором канала IT THINGS: https://www.youtube.com/c/ITTHINGS

import vk_api
import random
import sqlite3 as sql
import time
from flask import Flask, request, json


token = "0eb84772aba8b19fa8e61c3c92cd75999e7f8c97932f711bc20c8c59cdd3a7adc9b60f84271f22eba5500"

vk = vk_api.VkApi(token=token)

DATABASE = sql.connect('vkbot.db')
DATABASE.row_factory = lambda cursor, row: row[0]
with DATABASE:
    cur = DATABASE.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `user_info` (`userid` STRING, `user_balance` INTEGER)")
    DATABASE.commit()
 

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def main():
    data = json.loads(request.data)
    if data["type"] == "confirmation":
        return "код подтверждения"
    elif data["type"] == "message_new":
        object = data["object"]
        id = object["peer_id"]
        body = object["text"]
        if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "как дела":
                vk.method("messages.send", {"peer_id": id, "message": "Я съел деда", "random_id": random.randint(1, 2147483647)})
        else:
            vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 2147483647)})
    return "ok"

app.run(debug=True)