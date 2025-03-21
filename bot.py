import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message

# BotFather tomonidan berilgan token
TOKEN = "7267797063:AAHjnlqhlLYU1rEAXf2S1VWLbKrTICagnak"  # Bu yerga haqiqiy tokenni qo'ying
ADMIN_IDS = [6588255887]  # Admin IDlari

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Test savollari
quizzes = {
    "state": [
        {"question": "Ko'rmoq/tushunmoq", "options": ["SEE", "LOOK", "NOTICE", "WATCH"], "correct": 0},
    {"question": "Rohatlanmoq", "options": ["LIKE", "ENJOY", "PREFER", "LOVE"], "correct": 1},
    {"question": "His qilmoq", "options": ["THINK", "FEEL", "EXPECT", "HOPE"], "correct": 1},
    {"question": "Yoqtirmoq", "options": ["LOVE", "LIKE", "HATE", "DISLIKE"], "correct": 1},
    {"question": "Yoqtirmaslik", "options": ["HATE", "DISLIKE", "DETEST", "AVOID"], "correct": 1},
    {"question": "O'z ichiga olmoq", "options": ["INCLUDE", "CONTAIN", "FIT", "BELONG"], "correct": 0},
    {"question": "Ahamiyat kasb etmoq", "options": ["MATTER", "BELONG", "MEAN", "KEEP"], "correct": 0},
    {"question": "Muhtoj bo'lmoq", "options": ["REQUIRE", "NEED", "EXPECT", "WISH"], "correct": 0},
    {"question": "Xohlamoq/tilak bildirmoq", "options": ["WISH", "WANT", "DESIRE", "PREFER"], "correct": 0},
    {"question": "Sevmoq", "options": ["LIKE", "ENJOY", "LOVE", "ADORE"], "correct": 2},
    {"question": "Nafratlanmoq", "options": ["HATE", "DISLIKE", "DETEST", "IGNORE"], "correct": 0},
    {"question": "Tuyulmoq (tashqi ko'rinish)", "options": ["SEEM", "APPEAR", "LOOK", "SOUND"], "correct": 1},
    {"question": "Tuyulmoq (holat)", "options": ["SEEM", "APPEAR", "SOUND", "LOOK"], "correct": 0},
    {"question": "Ishonmoq", "options": ["BELIEVE", "SUPPOSE", "EXPECT", "TRUST"], "correct": 0},
    {"question": "Tegishli bo'lmoq", "options": ["BELONG", "FIT", "INCLUDE", "OWN"], "correct": 0},
    {"question": "Unutmoq", "options": ["REMEMBER", "FORGET", "IGNORE", "REGRET"], "correct": 1},
    {"question": "Eshitmoq", "options": ["HEAR", "LISTEN", "NOTICE", "SOUND"], "correct": 0},
    {"question": "Bilmoq", "options": ["KNOW", "UNDERSTAND", "THINK", "BELIEVE"], "correct": 0},
    {"question": "Vaznga ega bo'lmoq", "options": ["WEIGH", "MEASURE", "FIT", "CONTAIN"], "correct": 0},
    {"question": "Kutmoq", "options": ["EXPECT", "WISH", "HOPE", "SUPPOSE"], "correct": 0},
    {"question": "Hurmat qilmoq", "options": ["LOVE", "ADORE", "APPRECIATE", "RESPECT"], "correct": 1},
    {"question": "Ovozga nisbatan tuyulmoq", "options": ["SOUND", "SEEM", "APPEAR", "LOOK"], "correct": 0},
    {"question": "Payqamoq", "options": ["NOTICE", "REALISE", "SEE", "LOOK"], "correct": 0},
    {"question": "Egalik qilmoq", "options": ["OWN", "HAVE", "KEEP", "BELONG"], "correct": 0},
    {"question": "Saqlamoq", "options": ["KEEP", "HAVE", "OWN", "BELONG"], "correct": 0},
    {"question": "Arzimoq/qiymatga ega bo'lmoq", "options": ["COST", "PRICE", "VALUE", "WORTH"], "correct": 0},
    {"question": "Qarzdor bo'lib qolmoq", "options": ["OWE", "PAY", "OWN", "BORROW"], "correct": 0},
    {"question": "Kerak bo'lmoq", "options": ["NEED", "REQUIRE", "EXPECT", "WANT"], "correct": 0},
    {"question": "Shikast yetkazmoq/og'rimoq", "options": ["HURT", "ACHE", "PAIN", "INJURE"], "correct": 0},
    {"question": "Og'rimoq", "options": ["ACHE", "HURT", "PAIN", "SORE"], "correct": 0},
    {"question": "Eslamoq", "options": ["REMEMBER", "FORGET", "NOTICE", "RECOGNISE"], "correct": 0},
    {"question": "Hid taratmoq", "options": ["SMELL", "TASTE", "SCENT", "AROMA"], "correct": 0},
    {"question": "O'ylamoq", "options": ["THINK", "SUPPOSE", "BELIEVE", "IMAGINE"], "correct": 0},
    {"question": "Tushunmoq", "options": ["UNDERSTAND", "KNOW", "THINK", "REALISE"], "correct": 0},
    {"question": "Afzal ko'rmoq", "options": ["PREFER", "LIKE", "WANT", "CHOOSE"], "correct": 0},
    {"question": "Anglab yetmoq", "options": ["REALISE", "RECOGNISE", "KNOW", "NOTICE"], "correct": 0},
    {"question": "Tanimoq", "options": ["RECOGNISE", "REMEMBER", "REALISE", "ACKNOWLEDGE"], "correct": 0},
    {"question": "Deb hisoblamoq", "options": ["SUPPOSE", "EXPECT", "BELIEVE", "THINK"], "correct": 0},
    {"question": "Anglatmoq", "options": ["MEAN", "DEFINE", "EXPLAIN", "SUPPOSE"], "correct": 0},
    {"question": "Mos kelmoq", "options": ["FIT", "INCLUDE", "BELONG", "MEASURE"], "correct": 0},
    {"question": "Ta'm bermoq", "options": ["TASTE", "SMELL", "FLAVOUR", "EAT"], "correct": 0},
    {"question": "Rozi bo'lmoq", "options": ["AGREE", "ACCEPT", "ALLOW", "APPROVE"], "correct": 0},
    {"question": "Rad qilmoq", "options": ["DENY", "REFUSE", "DISAGREE", "IGNORE"], "correct": 0},
    {"question": "Juda yomon ko'rmoq", "options": ["DETEST", "HATE", "DISLIKE", "AVOID"], "correct": 0},
    {"question": "Qattiq istamoq", "options": ["DESIRE", "WISH", "WANT", "PREFER"], "correct": 0},
    {"question": "Shubhalanmoq", "options": ["DOUBT", "SUPPOSE", "BELIEVE", "MEAN"], "correct": 0},
    {"question": "Hasad/rashk qilmoq", "options": ["ENVY", "HATE", "DISLIKE", "DETEST"], "correct": 0},
    {"question": "Ko‘rinmoq/tuyulmoq", "options": ["LOOK", "SEEM", "APPEAR", "NOTICE"], "correct": 0},
    {"question": "Tasavvur qilmoq", "options": ["IMAGINE", "THINK", "BELIEVE", "EXPECT"], "correct": 0},
    {"question": "Umid qilmoq", "options": ["HOPE", "EXPECT", "WISH", "BELIEVE"], "correct": 0},
    {"question": "Keçhirmoq", "options": ["FORGIVE", "FORGET", "IGNORE", "REMEMBER"], "correct": 0}
    ],
  "p_verb_1":[
    {
        "question": "Yo’q bo‘lmoq",
        "options": ["Absent from", "Accompanied by", "According to", "Account for"],
        "correct": 0
    },
    {
        "question": "Bilan hamroh",
        "options": ["Accuse smb of", "Accompanied by", "Afraid of", "Account for"],
        "correct": 1
    },
    {
        "question": "… ga muvofiq",
        "options": ["Advantage of", "Advice on", "According to", "Addicted to"],
        "correct": 2
    },
    {
        "question": "Hisobga olmoq",
        "options": ["Account for", "Accompanied by", "Absent from", "Afraid of"],
        "correct": 0
    },
    {
        "question": "Ayblamoq",
        "options": ["Accused smb of", "Afraid of", "Addicted to", "Account for"],
        "correct": 0
    },
    {
        "question": "Odatlangan",
        "options": ["According to", "Afraid of", "Accustomed to", "Advice on"],
        "correct": 2
    },
    {
        "question": "Berilib ketgan",
        "options": ["Addicted to", "Advantage of", "Account for", "Accompanied by"],
        "correct": 0
    },
    {
        "question": "Ustunlik, afzallik",
        "options": ["Absent from", "Advantage of", "Account for", "According to"],
        "correct": 1
    },
    {
        "question": "Maslahat",
        "options": ["Afraid of", "Account for", "Advice on", "Absent from"],
        "correct": 2
    },
    {
        "question": "Qo‘rqqan",
        "options": ["Accompanied by", "Accuse smb of", "Afraid of", "Advantage of"],
        "correct": 2
    }
],
"p_verb_2": [
    {
        "question": "Ko’nmoq, rozi bo‘lmoq",
        "options": ["Agree to", "Agree on smth", "Agree with smb", "Ahead of"],
        "correct": 0
    },
    {
        "question": "Kelishmoq",
        "options": ["Ahead of", "Agree on smth", "Agree with smb", "Aim at"],
        "correct": 1
    },
    {
        "question": "Hamfikr bo‘lmoq, rozi bo‘lmoq",
        "options": ["Agree with smb", "Allergic to", "Amazed at/by", "Angry at what smb does"],
        "correct": 0
    },
    {
        "question": "Oldida",
        "options": ["Aim at", "Agree on smth", "Ahead of", "Amused at/with"],
        "correct": 2
    },
    {
        "question": "Maqsad",
        "options": ["Agree to", "Allergic to", "Aim at", "Amazed at/by"],
        "correct": 2
    },
    {
        "question": "Allergiyali",
        "options": ["Agree with smb", "Agree on smth", "Allergic to", "Angry with smb about smth"],
        "correct": 2
    },
    {
        "question": "Hayratda qolgan",
        "options": ["Angry at what smb does", "Amazed at/by", "Agree to", "Amused at/with"],
        "correct": 1
    },
    {
        "question": "Xursand",
        "options": ["Angry with smb about smth", "Amazed at/by", "Amused at/with", "Agree with smb"],
        "correct": 2
    },
    {
        "question": "Jahl chiqmoq (kimdandir nimadir haqida)",
        "options": ["Angry at what smb does", "Agree to", "Angry with smb about smth", "Aim at"],
        "correct": 2
    },
    {
        "question": "Jahl chiqmoq (kimningdir qilgan ishidan)",
        "options": ["Allergic to", "Ahead of", "Amazed at/by", "Angry at what smb does"],
        "correct": 3
    }
],
    "p_verb_3":[
    {
        "question": "Jahl chiqmoq (kimdandir nimadir qilgani uchun)",
        "options": ["Angry with smb for doing smth", "Annoyed with smb about smth", "Anxious about smth", "Apply to smb for smth"],
        "correct": 0
    },
    {
        "question": "Achchiqlanmoq (nimadir haqida)",
        "options": ["Annoyed with smb about smth", "Apologize to smb for smth", "Appeal to/against", "Approve of"],
        "correct": 0
    },
    {
        "question": "Javob",
        "options": ["Answer to", "Anxious about smth", "Apply to smb for smth", "Appeal to smb for smth"],
        "correct": 0
    },
    {
        "question": "Xavotirlanmoq, tashvishlanmoq",
        "options": ["Approve of", "Angry with smb for doing smth", "Anxious about smth", "Appeal to/against"],
        "correct": 2
    },
    {
        "question": "Xavotirlanmoq (nimadir sodir bo‘lishini kutib)",
        "options": ["Apply to smb for smth", "Anxious for smth to happen", "Apologize to smb for smth", "Annoyed with smb about smth"],
        "correct": 1
    },
    {
        "question": "Kechirim so‘ramoq",
        "options": ["Approve of", "Appeal to smb for smth", "Apologize to smb for smth", "Answer to"],
        "correct": 2
    },
    {
        "question": "Shikoyat qilmoq",
        "options": ["Anxious about smth", "Appeal to smb for smth", "Apply to smb for smth", "Annoyed with smb about smth"],
        "correct": 1
    },
    {
        "question": "Appilyatsiya bermoq",
        "options": ["Appeal to/against", "Answer to", "Approve of", "Apologize to smb for smth"],
        "correct": 0
    },
    {
        "question": "Murojaat qilmoq",
        "options": ["Answer to", "Anxious for smth to happen", "Apply to smb for smth", "Angry with smb for doing smth"],
        "correct": 2
    },
    {
        "question": "Ma’qullamoq",
        "options": ["Apply to smb for smth", "Appeal to/against", "Approve of", "Answer to"],
        "correct": 2
    }
],
    "p_verb_4": [
    {
        "question": "Bahslashmoq",
        "options": ["Argue with smb about smth", "Arrest smb for smth", "Arrive at", "Arrive in"],
        "correct": 0
    },
    {
        "question": "Xibsga olmoq",
        "options": ["Arrive at", "Ask for", "Arrest smb for smth", "Attach to"],
        "correct": 2
    },
    {
        "question": "Yetib kelmoq (kichik joyga)",
        "options": ["Arrive at", "Arrive in", "Ashamed of", "Astonished at/by"],
        "correct": 0
    },
    {
        "question": "Yetib kelmoq (atoqli joyga)",
        "options": ["Arrive at", "Arrive in", "Assure smb of", "Attach to"],
        "correct": 1
    },
    {
        "question": "Uyalgan",
        "options": ["Ashamed of", "Attach to", "Astonished at/by", "Ask for"],
        "correct": 0
    },
    {
        "question": "So‘ramoq",
        "options": ["Assure smb of", "Ask for", "Astonished at/by", "Attach to"],
        "correct": 1
    },
    {
        "question": "Ishontirmoq",
        "options": ["Argue with smb about smth", "Arrest smb for smth", "Assure smb of", "Arrive at"],
        "correct": 2
    },
    {
        "question": "Hayratda qolgan",
        "options": ["Attach to", "Astonished at/by", "Arrive at", "Ashamed of"],
        "correct": 1
    },
    {
        "question": "Mahkamlamoq",
        "options": ["Attach to", "Ask for", "Arrive in", "Arrest smb for smth"],
        "correct": 0
    },
    {
        "question": "Ko‘ngil qo‘ymoq (m-n: pulga)",
        "options": ["Assure smb of", "Attach for smth", "Argue with smb about smth", "Ashamed of"],
        "correct": 1
    }
],
"irregular_verbs_1": [
        {
       "question": "Bo‘lmoq",
        "options": ["Be - Was/Were - Been", "Beat - Beat - Beaten", "Begin - Began - Begun", "Buy - Bought - Bought"],
            "correct": 0
        },
        {
            "question": "Urmoq",
            "options": ["Blow - Blew - Blown", "Beat - Beat - Beaten", "Bring - Brought - Brought", "Catch - Caught - Caught"],
            "correct": 1
        },
        {
            "question": "Boshlamoq",
            "options": ["Begin - Began - Begun", "Bite - Bit - Bitten", "Break - Broke - Broken", "Cut - Cut - Cut"],
            "correct": 0
        },
        {
            "question": "Egmoq",
            "options": ["Bend - Bent - Bent", "Broadcast - Broadcast - Broadcast", "Build - Built - Built", "Come - Came - Come"],
            "correct": 0
        },
        {
            "question": "Tishlamoq",
            "options": ["Bite - Bit - Bitten", "Cost - Cost - Cost", "Creep - Crept - Crept", "Cut - Cut - Cut"],
            "correct": 0
        },
        {
            "question": "Sindirmoq",
            "options": ["Blow - Blew - Blown", "Break - Broke - Broken", "Bring - Brought - Brought", "Buy - Bought - Bought"],
            "correct": 1
        },
        {
            "question": "Olib kelmoq",
            "options": ["Burst - Burst - Burst", "Buy - Bought - Bought", "Bring - Brought - Brought", "Be - Was/Were - Been"],
            "correct": 2
        },
        {
            "question": "Sotib olmoq",
            "options": ["Buy - Bought - Bought", "Catch - Caught - Caught", "Choose - Chose - Chosen", "Come - Came - Come"],
            "correct": 0
        },
        {
            "question": "Ushlamoq",
            "options": ["Choose - Chose - Chosen", "Cost - Cost - Cost", "Catch - Caught - Caught", "Cut - Cut - Cut"],
            "correct": 2
        },
        {
            "question": "Kelmoq",
            "options": ["Cut - Cut - Cut", "Come - Came - Come", "Broadcast - Broadcast - Broadcast", "Bend - Bent - Bent"],
            "correct": 1
        }
    ],

    "irregular_verbs_2": [
    {
        "question": "Tarqatmoq, hal qilmoq",
        "options": ["deal - dealt - dealt", "dig - dug - dug", "do - did - done", "draw - drew - drawn"],
        "correct": 0
    },
    {
        "question": "Kovlamoq",
        "options": ["deal - dealt - dealt", "dig - dug - dug", "do - did - done", "drink - drank - drunk"],
        "correct": 1
    },
    {
        "question": "Qilmoq, bajarmoq",
        "options": ["draw - drew - drawn", "do - did - done", "deal - dealt - dealt", "fly - flew - flown"],
        "correct": 1
    },
    {
        "question": "Chizmoq",
        "options": ["drink - drank - drunk", "drive - drove - driven", "draw - drew - drawn", "eat - ate - eaten"],
        "correct": 2
    },
    {
        "question": "Ichmoq",
        "options": ["drink - drank - drunk", "deal - dealt - dealt", "fly - flew - flown", "forgive - forgave - forgiven"],
        "correct": 0
    },
    {
        "question": "Haydamoq (mashinani…) ",
        "options": ["find - found - found", "forbid - forbade - forbidden", "drive - drove - driven", "fight - fought - fought"],
        "correct": 2
    },
    {
        "question": "Yemoq",
        "options": ["forgive - forgave - forgiven", "eat - ate - eaten", "feel - felt - felt", "fly - flew - flown"],
        "correct": 1
    },
    {
        "question": "Yiqilmoq",
        "options": ["fight - fought - fought", "fall - fell - fallen", "freeze - froze - frozen", "feed - fed - fed"],
        "correct": 1
    },
    {
        "question": "Boqmoq, ovqatlantirmoq",
        "options": ["feed - fed - fed", "fight - fought - fought", "forgive - forgave - forgiven", "flee - fled - fled"],
        "correct": 0
    },
    {
        "question": "His qilmoq",
        "options": ["find - found - found", "feel - felt - felt", "forgive - forgave - forgiven", "get - got - got"],
        "correct": 1
    },
    {
        "question": "Kurashmoq",
        "options": ["fight - fought - fought", "feed - fed - fed", "find - found - found", "freeze - froze - frozen"],
        "correct": 0
    },
    {
        "question": "Topmoq",
        "options": ["flee - fled - fled", "find - found - found", "forbid - forbade - forbidden", "fly - flew - flown"],
        "correct": 1
    },
    {
        "question": "Qochmoq, qochib ketmoq",
        "options": ["fly - flew - flown", "forbid - forbade - forbidden", "flee - fled - fled", "fall - fell - fallen"],
        "correct": 2
    },
    {
        "question": "Uchmoq",
        "options": ["freeze - froze - frozen", "fly - flew - flown", "forgive - forgave - forgiven", "forget - forgot - forgotten"],
        "correct": 1
    },
    {
        "question": "Ta’qiqlamoq",
        "options": ["forgive - forgave - forgiven", "forget - forgot - forgotten", "forbid - forbade - forbidden", "fly - flew - flown"],
        "correct": 2
    },
    {
        "question": "Unutmoq",
        "options": ["forgive - forgave - forgiven", "forget - forgot - forgotten", "get - got - got", "give - gave - given"],
        "correct": 1
    },
    {
        "question": "Kechirmoq",
        "options": ["give - gave - given", "get - got - got", "forgive - forgave - forgiven", "freeze - froze - frozen"],
        "correct": 2
    },
    {
        "question": "Muzlamoq",
        "options": ["freeze - froze - frozen", "forgive - forgave - forgiven", "forget - forgot - forgotten", "fight - fought - fought"],
        "correct": 0
    },
    {
        "question": "Olmoq, yetmoq",
        "options": ["get - got - got", "give - gave - given", "fall - fell - fallen", "flee - fled - fled"],
        "correct": 0
    },
    {
        "question": "Bermoq",
        "options": ["give - gave - given", "forget - forgot - forgotten", "find - found - found", "fly - flew - flown"],
        "correct": 0
    }
],

"irregular_verbs_3": [
    {
        "question": "Ketmoq, bormoq",
        "options": ["go - went - gone", "grow - grew - grown", "hang - hung - hung", "hear - heard - heard"],
        "correct": 0
    },
    {
        "question": "O‘smoq, o‘stirmoq",
        "options": ["hit - hit - hit", "grow - grew - grown", "hide - hid - hidden", "hold - held - held"],
        "correct": 1
    },
    {
        "question": "Ilmoq",
        "options": ["hear - heard - heard", "hang - hung - hung", "keep - kept - kept", "kneel - knelt - knelt"],
        "correct": 1
    },
    {
        "question": "Eshitmoq",
        "options": ["hide - hid - hidden", "hear - heard - heard", "hit - hit - hit", "hurt - hurt - hurt"],
        "correct": 1
    },
    {
        "question": "Yashirmoq, berkitmoq",
        "options": ["hold - held - held", "hit - hit - hit", "hide - hid - hidden", "hurt - hurt - hurt"],
        "correct": 2
    },
    {
        "question": "Urmoq",
        "options": ["hit - hit - hit", "hold - held - held", "keep - kept - kept", "kneel - knelt - knelt"],
        "correct": 0
    },
    {
        "question": "Ushlamoq, o‘tkazmoq",
        "options": ["hurt - hurt - hurt", "keep - kept - kept", "hold - held - held", "kneel - knelt - knelt"],
        "correct": 2
    },
    {
        "question": "Jarohatlamoq, og‘rimoq",
        "options": ["keep - kept - kept", "hurt - hurt - hurt", "kneel - knelt - knelt", "lay - laid - laid"],
        "correct": 1
    },
    {
        "question": "Saqlamoq",
        "options": ["lay - laid - laid", "keep - kept - kept", "kneel - knelt - knelt", "know - knew - known"],
        "correct": 1
    },
    {
        "question": "Tizzalamoq",
        "options": ["kneel - knelt - knelt", "know - knew - known", "lead - led - led", "leave - left - left"],
        "correct": 0
    },
    {
        "question": "Bilmoq",
        "options": ["lay - laid - laid", "leave - left - left", "know - knew - known", "lend - lent - lent"],
        "correct": 2
    },
    {
        "question": "Qo‘ymoq",
        "options": ["let - let - let", "lie - lay - lain", "lay - laid - laid", "light - lit - lit"],
        "correct": 2
    },
    {
        "question": "Yetaklamoq",
        "options": ["lend - lent - lent", "light - lit - lit", "lie - lay - lain", "lead - led - led"],
        "correct": 3
    },
    {
        "question": "Jo‘nab ketmoq, qoldirmoq",
        "options": ["light - lit - lit", "lose - lost - lost", "leave - left - left", "mean - meant - meant"],
        "correct": 2
    },
    {
        "question": "Qarz bermoq",
        "options": ["lend - lent - lent", "let - let - let", "mean - meant - meant", "lose - lost - lost"],
        "correct": 0
    },
    {
        "question": "Ruxsat bermoq",
        "options": ["lie - lay - lain", "let - let - let", "mean - meant - meant", "lead - led - led"],
        "correct": 1
    },
    {
        "question": "Yotmoq, aldamoq",
        "options": ["lie - lay - lain", "light - lit - lit", "lend - lent - lent", "lose - lost - lost"],
        "correct": 0
    },
    {
        "question": "Yoqmoq",
        "options": ["light - lit - lit", "lead - led - led", "lie - lay - lain", "mean - meant - meant"],
        "correct": 0
    },
    {
        "question": "Yo‘qotmoq",
        "options": ["lose - lost - lost", "let - let - let", "light - lit - lit", "lay - laid - laid"],
        "correct": 0
    },
    {
        "question": "Anglatmoq",
        "options": ["lead - led - led", "lose - lost - lost", "mean - meant - meant", "lie - lay - lain"],
        "correct": 2
    }
]

}

# Foydalanuvchi ma'lumotlari
user_data = {}
ratings = {}  # Reyting tizimi

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧠❤️👀 State Verbs")],
            [KeyboardButton(text="📜 Preposition Verbs")],  # Preposition Verbs tugmasi
            [KeyboardButton(text="🌟 Irregular Verbs")],  # Irregular Verbs tugmasi
            [KeyboardButton(text="👤 Profil")],
            [KeyboardButton(text="📈 Reyting")],
            [KeyboardButton(text="📞 Adminga murojaat")],
        ],
        resize_keyboard=True
    )
    await message.answer("Quyidagi funksiyalardan birini tanlang:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "📜 Preposition Verbs")
async def show_preposition_verbs(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📜 P verb 1"), KeyboardButton(text="📜 P verb 2")],
            [KeyboardButton(text="📜 P verb 3"), KeyboardButton(text="📜 P verb 4")],
            [KeyboardButton(text="⬅️ Ortga")],  # Ortga qaytish tugmasi
        ],
        resize_keyboard=True
    )
    await message.answer("Quyidagi Preposition Verbs bo‘limlaridan birini tanlang:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "🌟 Irregular Verbs")
async def show_irregular_verbs(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌟 I verb 1"), KeyboardButton(text="🌟 I verb 2"), KeyboardButton(text="🌟 I verb 3")],
            [KeyboardButton(text="⬅️ Ortga")],  # Ortga qaytish tugmasi
        ],
        resize_keyboard=True
    )
    await message.answer("Quyidagi Irregular Verbs bo‘limlaridan birini tanlang:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "⬅️ Ortga")
async def back_to_main_menu(message: types.Message):
    await start(message)
# Profil ko'rsatish
@dp.message(lambda message: message.text == "👤 Profil")
async def show_profile(message: types.Message):
    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    if not user_info or "subjects" not in user_info:
        await message.answer("Siz hali test ishlamagansiz! 📌")
        return
    
    profile_text = "👤 *Sizning profilingiz:*\n\n"
    
    for subject, stats in user_info["subjects"].items():
        profile_text += (
            f"📚 *{subject.capitalize()}*\n"
            f"✅ To‘g‘ri javoblar: {stats['correct']}\n"
            f"❌ Xato javoblar: {stats['wrong']}\n"
            f"📊 Jami savollar: {stats['total']}\n\n"
        )
    
    await message.answer(profile_text, parse_mode="Markdown")


# Reyting tizimi
@dp.message(lambda message: message.text == "📈 Reyting")
async def show_ratings(message: types.Message):
    if not ratings:
        await message.answer("📌 Hali hech kim test ishlamagan!")
        return

    # Reyting bo‘yicha tartiblash (katta ball birinchi bo‘lishi uchun)
    sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)

    result = "🏆 *Top 10 Reyting:*\n\n"
    for idx, (user_id, score) in enumerate(sorted_ratings[:10], 1):
        try:
            user = await bot.get_chat(user_id)
            result += f"{idx}. *{user.first_name}* — {score} ball\n"
        except Exception:
            result += f"{idx}. Ism mavjud emas — {score} ball\n"

    await message.answer(result, parse_mode="Markdown")


# Test boshlash
@dp.message(lambda message: message.text in ["🧠❤️👀 State Verbs", "📜 P verb 1", "📜 P verb 2", "📜 P verb 3", "📜 P verb 4", "🌟 I verb 1", "🌟 I verb 2", "🌟 I verb 3"],)
async def start_quiz(message: types.Message):
    user_id = message.from_user.id

    if message.text == "🧠❤️👀 State Verbs":
        subject = "state"
    elif message.text == "📜 P verb 1":
        subject = "p_verb_1"
    elif message.text == "📜 P verb 2":
        subject = "p_verb_2"
    elif message.text == "📜 P verb 3":
        subject = "p_verb_3"
    elif message.text == "📜 P verb 4":
        subject = "p_verb_4"
    elif message.text == "🌟 I verb 1":
        subject = "irregular_verbs_1"
    elif message.text == "🌟 I verb 2":
        subject = "irregular_verbs_2"
    elif message.text == "🌟 I verb 3":
        subject = "irregular_verbs_3"
    else:
        subject = "unknown"

    # Foydalanuvchi ma'lumotlarini tekshiramiz va yangilaymiz
    if user_id not in user_data:
        user_data[user_id] = {"subjects": {}, "score": 0}
    
    if subject not in user_data[user_id]["subjects"]:
        user_data[user_id]["subjects"][subject] = {"correct": 0, "wrong": 0, "total": 0}

    # Test boshlangani haqida bitta xabar yuboramiz
    await message.answer(f"📢 {message.text} bo‘yicha test boshlandi!")

    # Savolni faqat bitta marta yuboramiz
    await send_next_question(user_id, subject)

async def send_next_question(user_id, subject):
    user_info = user_data[user_id]
    questions = quizzes[subject].copy()
    
    # Agar foydalanuvchi barcha savollarga javob bergan bo'lsa, testni tugatish
    if user_info["subjects"][subject]["total"] >= len(questions):
        await bot.send_message(user_id, f"🎉 Test tugadi! Sizning natijangiz: {user_info['subjects'][subject]['correct']}/{user_info['subjects'][subject]['total']}")
        
        # Reytingda o'rni
        sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
        user_rank = next((idx for idx, (uid, _) in enumerate(sorted_ratings, 1) if uid == user_id), None)
        await bot.send_message(user_id, f"📊 Sizning reytingdagi o'rningiz: {user_rank}")

        # **Testni qayta ishlashga ruxsat berish**
        user_info["subjects"][subject]["total"] = 0
        user_info["subjects"][subject]["correct"] = 0
        user_info["subjects"][subject]["wrong"] = 0
        
        return
    
    # Keyingi savolni yuborish
    question_data = random.choice(questions)

    # Variantlarni aralashtirish va to‘g‘ri javobning yangi indeksini topish
    original_options = question_data["options"]
    correct_answer = original_options[question_data["correct"]]

    shuffled_options = original_options[:]  # Variantlarni nusxalash
    random.shuffle(shuffled_options)  # Random tartibga keltirish
    new_correct_index = shuffled_options.index(correct_answer)  # Yangi indeks

    # Telegram poll (so‘rovnoma) yaratish
    poll_msg = await bot.send_poll(
        chat_id=user_id,
        question=question_data["question"],
        options=shuffled_options,  # Aralashtirilgan variantlar
        type="quiz",
        correct_option_id=new_correct_index,  # Yangi indeks bo‘yicha to‘g‘ri javob
        is_anonymous=False
    )

    # Foydalanuvchining tanlovini tekshirish uchun ma’lumot saqlash
    user_info["current_poll"] = {
        "poll_id": poll_msg.poll.id,
        "subject": subject,
        "correct_option": new_correct_index  # To‘g‘ri javobning yangi indeksini saqlash
    }
# Test javobini qayta ishlash
@dp.poll_answer()
async def handle_poll_answer(poll_answer: types.PollAnswer):
    user_id = poll_answer.user.id
    user_info = user_data.get(user_id)
    
    if not user_info or "current_poll" not in user_info:
        return
    
    selected_option = poll_answer.option_ids[0]
    subject = user_info["current_poll"]["subject"]
    correct_answer = user_info["current_poll"]["correct_option"]
    
    if selected_option == correct_answer:
        user_info["subjects"][subject]["correct"] += 1
        user_info["score"] += 1
    else:
        user_info["subjects"][subject]["wrong"] += 1
    
    user_info["subjects"][subject]["total"] += 1
    
    # Reytingni yangilash
    ratings[user_id] = user_info["score"]
    
    # Javob berilganligini bildirish
    await bot.send_message(user_id, f"✅ Javobingiz qabul qilindi! Sizning natijangiz: {user_info['subjects'][subject]['correct']}/{user_info['subjects'][subject]['total']}")
    
    # Keyingi savolni yuborish
    await send_next_question(user_id, subject)

# 📞 Foydalanuvchi "Adminga murojaat" tugmasini bossachi
@dp.message(lambda message: message.text == "📞 Adminga murojaat")
async def contact_admin(message: Message):
    await message.answer("✍️ Adminga xabar yuborish uchun matn, rasm, video yoki fayl yuboring.")

# 📩 Foydalanuvchi adminlarga xabar yuborsa
@dp.message(lambda message: message.from_user.id not in ADMIN_IDS)
async def user_to_admin(message: Message):
    for admin_id in ADMIN_IDS:
        try:
            if message.text:
                sent_msg = await bot.send_message(admin_id, f"📬 Yangi xabar:\n"
                                                            f"👤 Foydalanuvchi ID: {message.from_user.id}\n"
                                                            f"📝 Xabar: {message.text}")
            elif message.photo:
                sent_msg = await bot.send_photo(admin_id, message.photo[-1].file_id, caption=f"📬 Yangi xabar:\n"
                                                                                             f"👤 Foydalanuvchi ID: {message.from_user.id}")
            elif message.video:
                sent_msg = await bot.send_video(admin_id, message.video.file_id, caption=f"📬 Yangi xabar:\n"
                                                                                         f"👤 Foydalanuvchi ID: {message.from_user.id}")
            elif message.document:
                sent_msg = await bot.send_document(admin_id, message.document.file_id, caption=f"📬 Yangi xabar:\n"
                                                                                               f"👤 Foydalanuvchi ID: {message.from_user.id}")

            await message.answer("✅ Xabaringiz adminlarga yuborildi. Iltimos, javobni kuting.")
        except Exception as e:
            print(f"❌ Xabar yuborilmadi: {e}")

# 📩 Admin foydalanuvchiga javob bersa
@dp.message(lambda message: message.reply_to_message and message.from_user.id in ADMIN_IDS)
async def admin_to_user(message: Message):
    if "📬 Yangi xabar:" in message.reply_to_message.text:
        try:
            user_id_line = [line for line in message.reply_to_message.text.split("\n") if "Foydalanuvchi ID:" in line]
            if user_id_line:
                user_id = int(user_id_line[0].split(": ")[1])
                await bot.send_message(user_id, f"📩 Admin javobi:\n{message.text}")
            else:
                await message.answer("❌ Foydalanuvchi ID topilmadi. Xatolik yuz berdi.")
        except ValueError:
            await message.answer("❌ Foydalanuvchi ID topilmadi. Xatolik yuz berdi.")
# Admin panel
@dp.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Siz admin emassiz!")
        return
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📊 Statistika")],
            [types.KeyboardButton(text="📢 Reklama yuborish")],
            [types.KeyboardButton(text="➕ Yangi test qo'shish")],
        ],
        resize_keyboard=True
    )
    await message.answer("Admin panelga xush kelibsiz!", reply_markup=keyboard)

# Admin: Statistika
@dp.message(lambda message: message.text == "📊 Statistika" and message.from_user.id in ADMIN_IDS)
async def show_statistics(message: types.Message):
    total_users = len(user_data)
    await message.answer(f"📊 Bot foydalanuvchilari soni: {total_users}")

# Admin: Reklama yuborish
# 📢 Admin "Reklama yuborish" tugmasini bossachi
@dp.message(lambda message: message.text == "📢 Reklama yuborish" and message.from_user.id in ADMIN_IDS)
async def ask_for_advertisement(message: Message):
    await message.answer("✍️ Reklama uchun matn, rasm, video yoki fayl yuboring.")

# 📢 Admin xabar, rasm, video yoki fayl yuborsa
@dp.message(lambda message: message.from_user.id in ADMIN_IDS)
async def send_advertisement(message: Message):
    if not user_data:
        await message.answer("⚠️ Hozircha hech qanday foydalanuvchi yo‘q!")
        return

    success, failed = 0, 0

    for user_id in user_data:
        try:
            if message.text:
                await bot.send_message(user_id, message.text)
            elif message.photo:
                await bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption)
            elif message.video:
                await bot.send_video(user_id, message.video.file_id, caption=message.caption)
            elif message.document:
                await bot.send_document(user_id, message.document.file_id, caption=message.caption)
            success += 1
        except Exception as e:
            print(f"❌ Xabar yuborilmadi (User ID: {user_id}): {e}")
            failed += 1

    await message.answer(f"✅ Reklama {success} ta foydalanuvchiga yuborildi!\n❌ Xatoliklar: {failed}")
# 🎯 Foydalanuvchilarni avtomatik ro‘yxatga olish
@dp.message(lambda message: message.from_user.id not in ADMIN_IDS)
async def register_user(message: Message):
    user_data.add(message.from_user.id)
# Admin: Yangi test qo'shish
@dp.message(lambda message: message.text == "➕ Yangi test qo'shish" and message.from_user.id in ADMIN_IDS)
async def add_new_test(message: types.Message):

    await message.answer("Yangi test qo'shish uchun quyidagi formatda xabar yuboring:\n\n"
                         "Fan nomi: Savol matni\n"
                         "A) Variant 1\n"
                         "B) Variant 2\n"
                         "C) Variant 3\n"
                         "To'g'ri javob: A")

@dp.message(lambda msg: msg.from_user.id in ADMIN_IDS)
async def process_new_test(msg: types.Message):
    try:
        # Xabarni bo'lib olish
        lines = msg.text.split("\n")

        if len(lines) < 5:
            raise ValueError("To'liq formatda kiritilmagan.")

        # Fan nomi va savolni ajratib olish
        subject_part = lines[0].split(": ", 1)
        if len(subject_part) < 2:
            raise ValueError("Fan nomi noto‘g‘ri formatda.")

        subject = subject_part[0].strip()
        question = subject_part[1].strip()

        # Variantlarni olish
        options = []
        for i in range(1, 4):  # A, B, C variantlari
            if len(lines[i]) < 4 or lines[i][1] != ")":
                raise ValueError("Variantlar noto‘g‘ri formatda.")
            options.append(lines[i][3:].strip())

        # To‘g‘ri javobni olish
        correct_part = lines[4].split(": ", 1)
        if len(correct_part) < 2:
            raise ValueError("To'g'ri javob noto‘g‘ri formatda.")
        
        correct_option = correct_part[1].strip().upper()
        if correct_option not in ["A", "B", "C"]:
            raise ValueError("To'g'ri javob faqat A, B yoki C bo‘lishi kerak.")

        correct_index = ord(correct_option) - ord("A")  # Indeksni aniqlash (0, 1, 2)

        # Testni saqlash
        if subject not in quizzes:
            quizzes[subject] = []
        quizzes[subject].append({
            "question": question,
            "options": options,
            "correct": correct_index
        })

        await msg.answer("✅ Yangi test muvaffaqiyatli qo'shildi!")
    
    except ValueError as e:
        await msg.answer(f"❌ Xatolik: {e}")
    except Exception as e:
        await msg.answer(f"❌ Kutilmagan xatolik: {e}")

        

# Botni ishga tushirish
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
