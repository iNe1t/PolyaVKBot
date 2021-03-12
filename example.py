import vk_api
import sqlite3 as sql
import time
import random
 
connection = sql.connect("user.sqlite", check_same_thread=False)
 
q = connection.cursor()
 
q.execute('''CREATE TABLE user_info
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
            if body.lower() == "начать" or body.lower() == "помощь":
                connection = sql.connect("user.sqlite", check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = '%s'" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance, Ownment) VALUES ('%s', '%s', '%s', '%s')" % (
                        user_name,
                        id, 0, ""))
                    connection.commit()
                    connection.close()
                else:
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    print(result)
                    user_name = result[0][1]
                vk.method("messages.send", {"peer_id": id, "message": user_name + """, мои команды:
                Профиль
                Казино [сумма]
                Кубик [грань]
                Недвижимость [id]:
                Дом - 1(100000$)
                Машина - 2(50000$)
                Дача - 3(40000$)""", "random_id": random.randint(1, 2147483647)})
            elif "кубик" in body.lower():
                cube = random.randint(1, 6)
                user_cube = str(body.lower()[-1])
                user_win = random.randint(100, 1000)
                connection = sql.connect("user.sqlite", check_same_thread=False)
                q = connection.cursor()
				q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                      id, 0))
                    connection.commit()
                    connection.close()
                else:
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    print(result)
                    user_name = result[0][1]
                    if user_cube == str(cube):
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": user_name + ", вы угадали! 😯 Выйгрыш " + str(
                                                        user_win) + "$", "random_id": random.randint(1, 2147483647)})
                        q = connection.cursor()
                        q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                        result = q.fetchall()
                        q.execute(
                            "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (result[0][3] + user_win, id))
                        connection.commit()
                        connection.close()
 
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": user_name + ", вы проиграли! Выпало число " + str(
                                                        cube) + " 😔", "random_id": random.randint(1, 2147483647)})
            elif "казино" in body.lower():
                connection = sql.connect('user.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                      id, 0))
                    connection.commit()
                    connection.close()
                else:
                    kazino = random.randint(1, 2)
                    try:
                        rate = int(body.lower().split("казино ")[-1])
                        if result[0][3] >= rate:
                            if kazino == 1:
                                coefficient = random.randint(1, 3)
                                if coefficient == 1:
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(money) +
                                                                                                            rate * 2, id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send",
                                              {"peer_id": id, "message": "Вы выиграли " + str(rate * 2) + "!", "random_id": random.randint(1, 2147483647)})
                                elif coefficient == 2:
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(money) +
                                                                                                            rate * 3, id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send",
                                              {"peer_id": id, "message": "Вы выиграли " + str(rate * 3) + "!", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                                    result = q.fetchall()
                                    money = result[0][3]
                                    connection = sql.connect('user.sqlite', check_same_thread=False)
                                    q = connection.cursor()
                                    q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (int(money) +
                                                                                                            rate * 7, id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send",
                                              {"peer_id": id, "message": "Вы выиграли " + str(rate * 7) + "!", "random_id": random.randint(1, 2147483647)})
                            elif kazino == 2:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Вы проиграли " + str(rate) + ":(", "random_id": random.randint(1, 2147483647)})
                                connection = sql.connect('user.sqlite', check_same_thread=False)
                                q = connection.cursor()
                                q.execute("UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (result[0][3] - rate, id))
                                connection.commit()
                                connection.close()
                        else:
                            vk.method("messages.send",
                          {"peer_id": id, "message": "Недостаточно средств!", "random_id": random.randint(1, 2147483647)})
                    except:
                        vk.method("messages.send", {"peer_id": id, "message": "Введите корректную сумму ставки!", "random_id": random.randint(1, 2147483647)})
            elif "недвижимость" in body.lower():
                try:
                    connection = sql.connect('user.sqlite', check_same_thread=False)
                    q = connection.cursor()
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    if len(result) == 0:
                        user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                        user_name = user_info[0]["first_name"]
                        print("Time to добавить юзера")
                        q.execute(
                            "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                          id, 0))
                        connection.commit()
                        connection.close()
                    else:
                        realty = int(body.lower().split("недвижимость")[1])
                        if realty == 1:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 100000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "1,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 100000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили дом&#127968;!", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("1,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 100000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили дом&#127968;!", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 2:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 50000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "2,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 50000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили машину!&#128664;", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("2,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 50000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили машину!&#128664;", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                        elif realty == 3:
                            connection = sql.connect('user.sqlite', check_same_thread=False)
                            q = connection.cursor()
                            q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                            result = q.fetchall()
                            money = result[0][3]
                            ownment = result[0][4]
                            if money >= 40000:
                                if ownment != None:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % (
                                    str(ownment) + "3,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 40000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили дачу!&#127969;", "random_id": random.randint(1, 2147483647)})
                                else:
                                    q.execute("UPDATE user_info SET Ownment = '%s' WHERE User_ID = '%s'" % ("3,", id))
                                    q.execute(
                                        "UPDATE user_info SET Balance = '%s' WHERE User_ID = '%s'" % (money - 40000,
                                                                                                      id))
                                    connection.commit()
                                    connection.close()
                                    vk.method("messages.send", {"peer_id": id, "message": "Вы купили дачу!&#127969;", "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send",
                                          {"peer_id": id, "message": "Недостаточно денег для покупки!", "random_id": random.randint(1, 2147483647)})
                except:
                    vk.method("messages.send", {"peer_id": id, "message": "Введите корректный id недвижимости!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "профиль":
                connection = sql.connect('user.sqlite', check_same_thread=False)
                q = connection.cursor()
                q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                result = q.fetchall()
                if len(result) == 0:
                    user_info = vk.method("users.get", {"user_ids": id, "fields": "first_name"})
                    user_name = user_info[0]["first_name"]
                    print("Time to добавить юзера")
                    q.execute(
                        "INSERT INTO user_info (Name, User_ID, Balance) VALUES ('%s', '%s', '%s')" % (user_name,
                                                                                                      id, 0))
                    connection.commit()
                    connection.close()
                else:
                    q.execute("SELECT * FROM user_info WHERE User_ID = %s" % (id))
                    result = q.fetchall()
                    user_id = result[0][0]
                    name = result[0][1]
                    balance = result[0][3]
                    ownment = result[0][4]
 
                    ownment_message = ""
                    if ownment != None:
                        ownment = ownment.split(",")
                        ownment = ownment[:-1]
                        for own in ownment:
                            if int(own) == 1:
                                ownment_message += "Дом 🏠\n"
                            elif int(own) == 2:
                                ownment_message += "Машина 🚘\n"
                            elif int(own) == 3:
                                ownment_message += "Дача 🏡\n"
                    vk.method("messages.send", {"peer_id": id,
                                                "message": "ID: " + str(user_id) + "\nВаше имя: " + str(
                                                    name) + "\n💰Денег: " + str(balance) +
                                                           "\nВаши владения:\n " + ownment_message, "random_id": random.randint(1, 2147483647)})
    except:
        time.sleep(1)