import random, vk_api
import vk
import vk_api.vk_api
import hmtai
import config
import bot_key
import games
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

phrase_list_male = [", ты являешься прямым доказательством того, что человек может жить без мозгов.",
", а ты умнее, чем о тебе говорят!",
", проверьте подсоединение языка к мозгу.",
", тупость - ваш лучший друг!",
" такой умный. Интересно, ему череп не жмет?",
", отлично выглядишь! Бухал вчера?",
", тебе идёт мейк-ап а-ля дебил.",
", cделай фокус, растворись в воздухе.",
", ты тупой или да?",
]
phrase_list_female = [", ты являешься прямым доказательством того, что человек может жить без мозгов.",
", а ты умнее, чем о тебе говорят!",
", проверьте подсоединение языка к мозгу.",
", тупость - ваш лучший друг!",
" такая умная. Интересно, ей череп не жмет?",
", отлично выглядишь! Бухала вчера?",
", тебе идёт мейк-ап а-ля дебил.",
", cделай фокус, растворись в воздухе.",
", ты тупой или да?",
]
hi_list = ['Ку', 'Привет', 'Здорово', 'Здарова', 'Здорова', 'Хай', 'Охае', 'Салам алейкум']

KEY = 'd8c36cdf12cccf78e77d0881b6a0b81ecedc999f'
SERVER = 'https://lp.vk.com/wh203143170'
TS = '1'

pozor_list = []
ban_list = []
admin_list = []

hmtai_categories = ["wallpaper", "mobileWallpaper", "neko", "jahy", "manga", 
                    "hentai", "ahegao", "nsfwMobileWallpaper", "gif", "nsfwNeko", "gangbang", "uniform", "foot",
                    "pantsu", "tentacles", "thighs"]
hc_len = len(hmtai_categories) - 1
list_len = len(phrase_list_male) - 1

vk_session = vk_api.VkApi(token='44da98deef5d1311d2ca99d31e942a14c7e04db89630e25ce9e4775c9a3279d6ec7474e5974d582adbe74')
longpoll = VkBotLongPoll(vk_session, '203143170')
vk = vk_session.get_api()

