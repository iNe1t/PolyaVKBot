import random, vk_api
import vk
import vk_api.vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token='0eb84772aba8b19fa8e61c3c92cd75999e7f8c97932f711bc20c8c59cdd3a7adc9b60f84271f22eba5500')
longpoll = VkBotLongPoll(vk_session, '203143170')
vk = vk_session.get_api()
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()
KEY = 'd8c36cdf12cccf78e77d0881b6a0b81ecedc999f'
SERVER = 'https://lp.vk.com/wh203143170'
TS = '1'

<<<<<<< HEAD
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
=======
for event in longpoll.listen():
    id = event.object.message['from_id']
    if event.type == VkBotEventType.MESSAGE_NEW:
        if id == 213344682 and event.from_chat:
            vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message='Дина, иди в жопу',
            	    chat_id = event.chat_id
                    )
        elif 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = KEY,          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = SERVER,
                    ts = TS,
                    random_id = get_random_id(),
              	    message='Привет!',
            	    chat_id = event.chat_id
                    )
        
>>>>>>> b25f2861f0edbcf242d7a420b11d62fb2bae7058
