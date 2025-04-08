import asyncio
import random
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from aiogram import types, F
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import asyncio
from aiogram import Router, F, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()
dp = Dispatcher()
dp.include_router(router)

# BotFather tomonidan berilgan token
TOKEN = "7267797063:AAFNqt3UXzIY77jTMv85p08Cp57K9WPD4sA"  # Bu yerga haqiqiy tokenni qo'ying
ADMIN_IDS = [7871012050]  # Admin IDlari

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Test savollari
quizzes = {
    "state_verbs": [
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
  "preposition_verbs1":[
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
"preposition_verbs2": [
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
    "preposition_verbs3":[
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
    "preposition_verbs4": [
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

"preposition_verbs5": [
    {
        "question": "Hujum",
        "options": ["Attack on", "Attack at", "Attack to", "Attack for"],
        "correct": 0
    },
    {
        "question": "Qatnashmoq",
        "options": ["Attend to", "Attend for", "Attend at", "Attend with"],
        "correct": 0
    },
    {
        "question": "Be/boxabar bo'lmoq",
        "options": ["(Un) aware of", "(Un) aware for", "(Un) aware at", "(Un) aware with"],
        "correct": 0
    },
    {
        "question": "Borasida yomon",
        "options": ["Bad at", "Bad in", "Bad for", "Bad to"],
        "correct": 0
    },
    {
        "question": "Yomon munosabatda bo’lmoq",
        "options": ["Bad to", "Bad at", "Bad for", "Bad with"],
        "correct": 0
    },
    {
        "question": "Asoslanmoq",
        "options": ["Base on", "Base for", "Base at", "Base with"],
        "correct": 0
    },
    {
        "question": "Asos",
        "options": ["Basis for", "Basis of", "Basis at", "Basis in"],
        "correct": 0
    },
    {
        "question": "Yalinmoq",
        "options": ["Beg for", "Beg to", "Beg at", "Beg with"],
        "correct": 0
    },
    {
        "question": "Boshlamoq",
        "options": ["Begin with", "Begin to", "Begin at", "Begin for"],
        "correct": 0
    },
    {
        "question": "Ishonmoq",
        "options": ["Believe in", "Believe on", "Believe to", "Believe for"],
        "correct": 0
    }
],
"preposition_verbs6": [
    {
        "question": "Foyda",
        "options": ["Benefit from", "Benefit to", "Benefit by", "Benefit at"],
        "correct": 0
    },
    {
        "question": "Pul tikmoq",
        "options": ["Bet on", "Bet with", "Bet at", "Bet for"],
        "correct": 0
    },
    {
        "question": "Ehtiyot bo’lmoq",
        "options": ["Beware of", "Beware at", "Beware for", "Beware with"],
        "correct": 0
    },
    {
        "question": "Ayblamoq (biror kishiga)",
        "options": ["(Put the) blame on smb", "Blame smb for smth", "Blame smth on smb", "All of the above"],
        "correct": 3
    },
    {
        "question": "Ayblamoq (biror narsaga)",
        "options": ["Blame smb for smth", "Blame smth on smb", "(Put the) blame on smb", "Blame smb for"],
        "correct": 1
    },
    {
        "question": "Maxtanmoq",
        "options": ["Boast about/of", "Boast at", "Boast for", "Boast with"],
        "correct": 0
    },
    {
        "question": "Zerikkan",
        "options": ["Bored with/of", "Bored from", "Bored by", "Bored at"],
        "correct": 0
    },
    {
        "question": "Qarzga olmoq",
        "options": ["Borrow smth from smb", "Borrow smth to smb", "Borrow from smb for smth", "Borrow with smb"],
        "correct": 0
    },
    {
        "question": "Borasida a’lo",
        "options": ["Brilliant at", "Brilliant in", "Brilliant for", "Brilliant with"],
        "correct": 0
    }
]
,
"preposition_verbs7": [
    {
        "question": "Urib olmoq",
        "options": ["Bump into", "Bump at", "Bump with", "Bump on"],
        "correct": 0
    },
    {
        "question": "... bilan band",
        "options": ["Busy with", "Busy for", "Busy about", "Busy on"],
        "correct": 0
    },
    {
        "question": "To‘xtab o’tmoq (poyezd v.h.z.larga nisbatan)",
        "options": ["Call at", "Call for", "Call with", "Call on"],
        "correct": 0
    },
    {
        "question": "Talab qilmoq",
        "options": ["Call for", "Call on", "Call at", "Call to"],
        "correct": 0
    },
    {
        "question": "Hamkorlikda ishlamoq",
        "options": ["Campaign against/for", "Campaign with", "Campaign on", "Campaign to"],
        "correct": 0
    },
    {
        "question": "...ga layoqatli",
        "options": ["Capable of", "Capable for", "Capable in", "Capable with"],
        "correct": 0
    },
    {
        "question": "Qayg’urmoq",
        "options": ["Care about", "Care for", "Care of", "Care with"],
        "correct": 0
    },
    {
        "question": "Yoqtirmoq",
        "options": ["Care for smb", "Care about smb", "Care for smth", "Care on smb"],
        "correct": 0
    },
    {
        "question": "G’amxo’rlik qilmoq",
        "options": ["(Take) care of", "Care for", "Care about", "Care with"],
        "correct": 0
    },
    {
        "question": "Qilishni xohlamoq",
        "options": ["Care for smth", "Care about smth", "Care with smth", "Care of smth"],
        "correct": 0
    }
]
,

"preposition_verbs8": [
    {
        "question": "Ehtiyotkor",
        "options": ["Careful of", "Careful about", "Careful with", "Careful for"],
        "correct": 0
    },
    {
        "question": "E’tiborsiz",
        "options": ["Careless about", "Careless of", "Careless with", "Careless in"],
        "correct": 0
    },
    {
        "question": "Sabab",
        "options": ["Cause of", "Cause for", "Cause at", "Cause with"],
        "correct": 0
    },
    {
        "question": "Ishonchli",
        "options": ["Certain of", "Certain about", "Certain in", "Certain for"],
        "correct": 0
    },
    {
        "question": "...ga o'zgarmoq",
        "options": ["Change into", "Change for", "Change to", "Change in"],
        "correct": 0
    },
    {
        "question": "Fazilatli",
        "options": ["Characteristic of", "Characteristic for", "Characteristic with", "Characteristic about"],
        "correct": 0
    },
    {
        "question": "To'latmoq",
        "options": ["Charge for", "Charge to", "Charge at", "Charge with"],
        "correct": 0
    },
    {
        "question": "Ayblamoq",
        "options": ["Charge smb with", "Charge smb for", "Charge for smb", "Charge with smb"],
        "correct": 0
    },
    {
        "question": "Chek",
        "options": ["Cheque for", "Cheque to", "Cheque at", "Cheque from"],
        "correct": 0
    },
    {
        "question": "Tanlov",
        "options": ["Choice between/of", "Choice for", "Choice at", "Choice with"],
        "correct": 0
    }
],

"preposition_verbs9": [
    {
        "question": "...da aqlli",
        "options": ["Clever at", "Clever in", "Clever with", "Clever for"],
        "correct": 0
    },
    {
        "question": "...ga yaqin",
        "options": ["Close to", "Close with", "Close at", "Close in"],
        "correct": 0
    },
    {
        "question": "Hamkorlikda ishlamoq",
        "options": ["Collaborate with", "Collaborate for", "Collaborate on", "Collaborate at"],
        "correct": 0
    },
    {
        "question": "To‘qnashmoq",
        "options": ["Collide with", "Collide on", "Collide for", "Collide at"],
        "correct": 0
    },
    {
        "question": "Fikr bildirmoq",
        "options": ["Comment on", "Comment about", "Comment for", "Comment with"],
        "correct": 0
    },
    {
        "question": "Aloqa qilmoq",
        "options": ["Communicate with", "Communicate to", "Communicate for", "Communicate at"],
        "correct": 0
    },
    {
        "question": "Taqqoslamoq",
        "options": ["Compare with/to", "Compare to", "Compare with", "Compare on"],
        "correct": 0
    },
    {
        "question": "Taqqoslash",
        "options": ["Comparison between", "Comparison of", "Comparison to", "Comparison with"],
        "correct": 0
    },
    {
        "question": "Shikoyat qilmoq/nolimoq",
        "options": ["Complain of", "Complain about", "Complain for", "Complain with"],
        "correct": 0
    },
    {
        "question": "Norozilik bildirmoq",
        "options": ["Complain to smb about smth", "Complain about smth to smb", "Complain of smb", "Complain for smb"],
        "correct": 0
    }
],
"preposition_verbs10": [
    {
        "question": "Xushomad qilmoq/maqtamoq",
        "options": ["Compliment smb on", "Compliment smb for", "Compliment smb with", "Compliment smb to"],
        "correct": 0
    },
    {
        "question": "Bo’ysunmoq",
        "options": ["Comply with", "Comply to", "Comply for", "Comply at"],
        "correct": 0
    },
    {
        "question": "Yashirmoq",
        "options": ["Conceal smth from smb", "Conceal smth for smb", "Conceal smb from smth", "Conceal smb with smth"],
        "correct": 0
    },
    {
        "question": "Diqqatni jamlamoq",
        "options": ["Concentrate on", "Concentrate in", "Concentrate for", "Concentrate at"],
        "correct": 0
    },
    {
        "question": "Ishonch",
        "options": ["(Have) confidence in smb", "(Have) confidence on smb", "(Have) confidence for smb", "(Have) confidence with smb"],
        "correct": 0
    },
    {
        "question": "Ikkilanmoq",
        "options": ["Confusion over", "Confusion about", "Confusion with", "Confusion for"],
        "correct": 0
    },
    {
        "question": "Tabriklamoq",
        "options": ["Congratulate smb on smth", "Congratulate smb for smth", "Congratulate smb about smth", "Congratulate smb with smth"],
        "correct": 0
    },
    {
        "question": "Aloqa",
        "options": ["Connection between", "Connection for", "Connection to", "Connection at"],
        "correct": 0
    },
    {
        "question": "...bilan aloqadorlikda",
        "options": ["In connection with", "In connection to", "In connection for", "In connection on"],
        "correct": 0
    },
    {
        "question": "...sezadigan",
        "options": ["Conscious of", "Conscious about", "Conscious for", "Conscious in"],
        "correct": 0
    }
],




"irregular_verbs1": [
    {
        "question": "Bo‘lmoq",
        "options": ["be - was/were - been", "beat - beat - beaten", "become - became - become", "begin - began - begun"],
        "correct": 0
    },
    {
        "question": "Urmoq, yengmoq",
        "options": ["become - became - become", "beat - beat - beaten", "begin - began - begun", "bend - bent - bent"],
        "correct": 1
    },
    {
        "question": "Bo‘lib qolmoq",
        "options": ["bet - bet - bet", "become - became - become", "begin - began - begun", "bite - bit - bitten"],
        "correct": 1
    },
    {
        "question": "Boshlamoq",
        "options": ["begin - began - begun", "bet - bet - bet", "bend - bent - bent", "bite - bit - bitten"],
        "correct": 0
    },
    {
        "question": "Egilmoq",
        "options": ["break - broke - broken", "bend - bent - bent", "bet - bet - bet", "blow - blew - blown"],
        "correct": 1
    },
    {
        "question": "Tikish (pul tikmoq)",
        "options": ["bite - bit - bitten", "bet - bet - bet", "break - broke - broken", "bring - brought - brought"],
        "correct": 1
    },
    {
        "question": "Tishlamoq",
        "options": ["blow - blew - blown", "bite - bit - bitten", "bring - brought - brought", "build - built - built"],
        "correct": 1
    },
    {
        "question": "Puflamoq, esmoq",
        "options": ["break - broke - broken", "blow - blew - blown", "broadcast - broadcast - broadcast", "burst - burst - burst"],
        "correct": 1
    },
    {
        "question": "Sindirmoq",
        "options": ["break - broke - broken", "bring - brought - brought", "broadcast - broadcast - broadcast", "burst - burst - burst"],
        "correct": 0
    },
    {
        "question": "Olib kelmoq",
        "options": ["build - built - built", "buy - bought - bought", "bring - brought - brought", "broadcast - broadcast - broadcast"],
        "correct": 2
    },
    {
        "question": "E‘lon qilmoq",
        "options": ["burst - burst - burst", "buy - bought - bought", "catch - caught - caught", "broadcast - broadcast - broadcast"],
        "correct": 3
    },
    {
        "question": "Qurmoq",
        "options": ["build - built - built", "burst - burst - burst", "catch - caught - caught", "choose - chose - chosen"],
        "correct": 0
    },
    {
        "question": "Portlamoq",
        "options": ["catch - caught - caught", "choose - chose - chosen", "burst - burst - burst", "come - came - come"],
        "correct": 2
    },
    {
        "question": "Sotib olmoq",
        "options": ["buy - bought - bought", "cost - cost - cost", "creep - crept - crept", "cut - cut - cut"],
        "correct": 0
    },
    {
        "question": "Ushlamoq, tutib olmoq",
        "options": ["cost - cost - cost", "creep - crept - crept", "catch - caught - caught", "cut - cut - cut"],
        "correct": 2
    },
    {
        "question": "Tanlamoq",
        "options": ["choose - chose - chosen", "come - came - come", "cost - cost - cost", "creep - crept - crept"],
        "correct": 0
    },
    {
        "question": "Kelmoq",
        "options": ["cost - cost - cost", "creep - crept - crept", "come - came - come", "cut - cut - cut"],
        "correct": 2
    },
    {
        "question": "Narx turmoq",
        "options": ["creep - crept - crept", "cost - cost - cost", "cut - cut - cut", "deal - dealt - dealt"],
        "correct": 1
    },
    {
        "question": "Uzoq yurmoq, sekin harakatlanmoq",
        "options": ["creep - crept - crept", "deal - dealt - dealt", "dig - dug - dug", "do - did - done"],
        "correct": 0
    },
    {
        "question": "Kesmoq",
        "options": ["cut - cut - cut", "deal - dealt - dealt", "dig - dug - dug", "do - did - done"],
        "correct": 0
    }
]
,
    "irregular_verbs2": [
    {
        "question": "Bitim tuzmoq",
        "options": ["deal - dealt - dealt", "dig - dug - dug", "do - did - done", "draw - drew - drawn"],
        "correct": 0
    },
    {
        "question": "Qazimoq",
        "options": ["dig - dug - dug", "do - did - done", "draw - drew - drawn", "dream - dreamt - dreamt"],
        "correct": 0
    },
    {
        "question": "Qilmoq",
        "options": ["do - did - done", "draw - drew - drawn", "dream - dreamt - dreamt", "drink - drank - drunk"],
        "correct": 0
    },
    {
        "question": "Chizmoq",
        "options": ["draw - drew - drawn", "dream - dreamt - dreamt", "drink - drank - drunk", "drive - drove - driven"],
        "correct": 0
    },
    {
        "question": "Orzu qilmoq",
        "options": ["dream - dreamt - dreamt", "drink - drank - drunk", "drive - drove - driven", "eat - ate - eaten"],
        "correct": 0
    },
    {
        "question": "Ichmoq",
        "options": ["drink - drank - drunk", "drive - drove - driven", "eat - ate - eaten", "fall - fell - fallen"],
        "correct": 0
    },
    {
        "question": "Haydamoq",
        "options": ["drive - drove - driven", "eat - ate - eaten", "fall - fell - fallen", "feed - fed - fed"],
        "correct": 0
    },
    {
        "question": "Yemoq",
        "options": ["eat - ate - eaten", "fall - fell - fallen", "feed - fed - fed", "feel - felt - felt"],
        "correct": 0
    },
    {
        "question": "Yiqilmoq",
        "options": ["fall - fell - fallen", "feed - fed - fed", "feel - felt - felt", "fight - fought - fought"],
        "correct": 0
    },
    {
        "question": "Boqmoq, ovqatlantirmoq",
        "options": ["feed - fed - fed", "feel - felt - felt", "fight - fought - fought", "find - found - found"],
        "correct": 0
    },
    {
        "question": "His qilmoq",
        "options": ["feel - felt - felt", "fight - fought - fought", "find - found - found", "fly - flew - flown"],
        "correct": 0
    },
    {
        "question": "Ulashmoq, jang qilmoq",
        "options": ["fight - fought - fought", "find - found - found", "fly - flew - flown", "forget - forgot - forgotten"],
        "correct": 0
    },
    {
        "question": "Topmoq",
        "options": ["find - found - found", "fly - flew - flown", "forget - forgot - forgotten", "forgive - forgave - forgiven"],
        "correct": 0
    },
    {
        "question": "Uchmoq",
        "options": ["fly - flew - flown", "forget - forgot - forgotten", "forgive - forgave - forgiven", "freeze - froze - frozen"],
        "correct": 0
    },
    {
        "question": "Unutmoq",
        "options": ["forget - forgot - forgotten", "forgive - forgave - forgiven", "freeze - froze - frozen", "get - got - gotten"],
        "correct": 0
    },
    {
        "question": "Kechirmoq",
        "options": ["forgive - forgave - forgiven", "freeze - froze - frozen", "get - got - gotten", "give - gave - given"],
        "correct": 0
    },
    {
        "question": "Muzlamoq",
        "options": ["freeze - froze - frozen", "get - got - gotten", "give - gave - given", "go - went - gone"],
        "correct": 0
    },
    {
        "question": "Olmoq, yetmoq",
        "options": ["get - got - gotten", "give - gave - given", "go - went - gone", "grow - grew - grown"],
        "correct": 0
    },
    {
        "question": "Bermoq",
        "options": ["give - gave - given", "go - went - gone", "grow - grew - grown", "hang - hung - hung"],
        "correct": 0
    },
    {
        "question": "Ketmoq, bormoq",
        "options": ["go - went - gone", "grow - grew - grown", "hang - hung - hung", "hear - heard - heard"],
        "correct": 0
    }
]
,
"irregular_verbs3": [
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
,
"irregular_verbs4": [
    {
        "question": "Qilmoq, yasamoq",
        "options": ["make – made – made", "mean – meant – meant", "meet – met – met", "pay – paid – paid"],
        "correct": 0
    },
    {
        "question": "Uchrashmoq",
        "options": ["put – put – put", "meet – met – met", "read – read – read", "ride – rode – ridden"],
        "correct": 1
    },
    {
        "question": "To‘lamoq",
        "options": ["run – ran – run", "pay – paid – paid", "read – read – read", "ride – rode – ridden"],
        "correct": 1
    },
    {
        "question": "O‘qimoq",
        "options": ["read – read – read", "run – ran – run", "see – saw – seen", "sell – sold – sold"],
        "correct": 0
    },
    {
        "question": "Minmoq",
        "options": ["ride – rode – ridden", "say – said – said", "see – saw – seen", "sell – sold – sold"],
        "correct": 0
    },
    {
        "question": "Yugurmoq",
        "options": ["run – ran – run", "say – said – said", "see – saw – seen", "seek – sought – sought"],
        "correct": 0
    },
    {
        "question": "Aytmoq",
        "options": ["sell – sold – sold", "send – sent – sent", "say – said – said", "set – set – set"],
        "correct": 2
    },
    {
        "question": "Ko‘rmoq",
        "options": ["sell – sold – sold", "see – saw – seen", "send – sent – sent", "set – set – set"],
        "correct": 1
    },
    {
        "question": "Izlamoq",
        "options": ["send – sent – sent", "seek – sought – sought", "set – set – set", "shake – shook – shaken"],
        "correct": 1
    },
    {
        "question": "Sotmoq",
        "options": ["sell – sold – sold", "send – sent – sent", "set – set – set", "shake – shook – shaken"],
        "correct": 0
    },
    {
        "question": "Yubormoq",
        "options": ["send – sent – sent", "set – set – set", "shake – shook – shaken", "shine – shone – shone"],
        "correct": 0
    },
    {
        "question": "O‘rnatmoq",
        "options": ["set – set – set", "shake – shook – shaken", "shine – shone – shone", "shoot – shot – shot"],
        "correct": 0
    },
    {
        "question": "Silkitmoq",
        "options": ["shake – shook – shaken", "shine – shone – shone", "shoot – shot – shot", "show – showed – shown"],
        "correct": 0
    },
    {
        "question": "Yaltiramoq",
        "options": ["shine – shone – shone", "shoot – shot – shot", "show – showed – shown", "shut – shut – shut"],
        "correct": 0
    },
    {
        "question": "O‘q otmoq",
        "options": ["shoot – shot – shot", "show – showed – shown", "shut – shut – shut", "sing – sang – sung"],
        "correct": 0
    },
    {
        "question": "Ko‘rsatmoq",
        "options": ["show – showed – shown", "shut – shut – shut", "sing – sang – sung", "sit – sat – sat"],
        "correct": 0
    },
    {
        "question": "Yopmoq",
        "options": ["shut – shut – shut", "sing – sang – sung", "sit – sat – sat", "sleep – slept – slept"],
        "correct": 0
    },
    {
        "question": "Kuylamoq",
        "options": ["sing – sang – sung", "sit – sat – sat", "sleep – slept – slept", "slide – slid – slid"],
        "correct": 0
    },
    {
        "question": "O‘tirib olmoq",
        "options": ["sit – sat – sat", "sleep – slept – slept", "slide – slid – slid", "speak – spoke – spoken"],
        "correct": 0
    },
    {
        "question": "Uxlamoq",
        "options": ["sleep – slept – slept", "slide – slid – slid", "speak – spoke – spoken", "spend – spent – spent"],
        "correct": 0
    }
]
,
"irregular_verbs5": [
    {
        "question": "Turmoq",
        "options": ["stand – stood – stood", "steal – stole – stolen", "stick – stuck – stuck", "sting – stung – stung"],
        "correct": 0
    },
    {
        "question": "O‘g‘irlamoq",
        "options": ["steal – stole – stolen", "stick – stuck – stuck", "sting – stung – stung", "stink – stank – stunk"],
        "correct": 0
    },
    {
        "question": "Yopishtirmoq, tiqilmoq",
        "options": ["stick – stuck – stuck", "sting – stung – stung", "stink – stank – stunk", "strike – struck – struck"],
        "correct": 0
    },
    {
        "question": "Chaqmoq (ari, chayon)",
        "options": ["sting – stung – stung", "stink – stank – stunk", "strike – struck – struck", "swear – swore – sworn"],
        "correct": 0
    },
    {
        "question": "Sasimoq, hid yomon bo‘lmoq",
        "options": ["stink – stank – stunk", "strike – struck – struck", "swear – swore – sworn", "sweep – swept – swept"],
        "correct": 0
    },
    {
        "question": "Urmoq, zarba bermoq",
        "options": ["strike – struck – struck", "swear – swore – sworn", "sweep – swept – swept", "swim – swam – swum"],
        "correct": 0
    },
    {
        "question": "Qasam ichmoq",
        "options": ["swear – swore – sworn", "sweep – swept – swept", "swim – swam – swum", "swing – swung – swung"],
        "correct": 0
    },
    {
        "question": "Supurmoq",
        "options": ["sweep – swept – swept", "swim – swam – swum", "swing – swung – swung", "take – took – taken"],
        "correct": 0
    },
    {
        "question": "Suzmoq",
        "options": ["swim – swam – swum", "swing – swung – swung", "take – took – taken", "teach – taught – taught"],
        "correct": 0
    },
    {
        "question": "Tegirmoq, silkitmoq",
        "options": ["swing – swung – swung", "take – took – taken", "teach – taught – taught", "tear – tore – torn"],
        "correct": 0
    },
    {
        "question": "Olmoq",
        "options": ["take – took – taken", "teach – taught – taught", "tear – tore – torn", "tell – told – told"],
        "correct": 0
    },
    {
        "question": "O‘rgatmoq",
        "options": ["teach – taught – taught", "tear – tore – torn", "tell – told – told", "think – thought – thought"],
        "correct": 0
    },
    {
        "question": "Yirtmoq",
        "options": ["tear – tore – torn", "tell – told – told", "think – thought – thought", "throw – threw – thrown"],
        "correct": 0
    },
    {
        "question": "Aytmoq, gapirmoq",
        "options": ["tell – told – told", "think – thought – thought", "throw – threw – thrown", "understand – understood – understood"],
        "correct": 0
    },
    {
        "question": "O‘ylamoq",
        "options": ["think – thought – thought", "throw – threw – thrown", "understand – understood – understood", "wake – woke – woken"],
        "correct": 0
    },
    {
        "question": "Otmoq (narsa)",
        "options": ["throw – threw – thrown", "understand – understood – understood", "wake – woke – woken", "wear – wore – worn"],
        "correct": 0
    },
    {
        "question": "Tushunmoq",
        "options": ["understand – understood – understood", "wake – woke – woken", "wear – wore – worn", "weep – wept – wept"],
        "correct": 0
    },
    {
        "question": "Uyg‘otmoq",
        "options": ["wake – woke – woken", "wear – wore – worn", "weep – wept – wept", "win – won – won"],
        "correct": 0
    },
    {
        "question": "Kiyinmoq",
        "options": ["wear – wore – worn", "weep – wept – wept", "win – won – won", "write – wrote – written"],
        "correct": 0
    },
    {
        "question": "Yig‘lamoq",
        "options": ["weep – wept – wept", "win – won – won", "write – wrote – written", "stand – stood – stood"],
        "correct": 0
    },
    {
        "question": "Yutmoq (g‘alaba)",
        "options": ["win – won – won", "write – wrote – written", "stand – stood – stood", "steal – stole – stolen"],
        "correct": 0
    }
]
    ,
    "irregular_verbs6": [
    {
        "question": "Yozmoq",
        "options": ["write – wrote – written", "arise – arose – arisen", "awake – awoke – awoken", "bear – bore – borne"],
        "correct": 0
    },
    {
        "question": "Ko'tarilmoq, paydo bo'lmoq",
        "options": ["arise – arose – arisen", "awake – awoke – awoken", "bear – bore – borne", "befall – befell – befallen"],
        "correct": 0
    },
    {
        "question": "Uygonmoq",
        "options": ["awake – awoke – awoken", "bear – bore – borne", "befall – befell – befallen", "bid – bid/bade – bid/bidden"],
        "correct": 0
    },
    {
        "question": "Ko'tarmoq, chidamoq",
        "options": ["bear – bore – borne", "befall – befell – befallen", "bid – bid/bade – bid/bidden", "bind – bound – bound"],
        "correct": 0
    },
    {
        "question": "Sodir bo'lmoq, yuz bermoq",
        "options": ["befall – befell – befallen", "bid – bid/bade – bid/bidden", "bind – bound – bound", "bleed – bled – bled"],
        "correct": 0
    },
    {
        "question": "Taklif qilmoq, buyurmoq",
        "options": ["bid – bid/bade – bid/bidden", "bind – bound – bound", "bleed – bled – bled", "breed – bred – bred"],
        "correct": 0
    },
    {
        "question": "Bog'lamoq",
        "options": ["bind – bound – bound", "bleed – bled – bled", "breed – bred – bred", "cling – clung – clung"],
        "correct": 0
    },
    {
        "question": "Qonamoq",
        "options": ["bleed – bled – bled", "breed – bred – bred", "cling – clung – clung", "dive – dove/dived – dived"],
        "correct": 0
    },
    {
        "question": "Ko'paytirmoq, boqmoq",
        "options": ["breed – bred – bred", "cling – clung – clung", "dive – dove/dived – dived", "draw – drew – drawn"],
        "correct": 0
    },
    {
        "question": "Yopishmoq, mahkam ushlamoq",
        "options": ["cling – clung – clung", "dive – dove/dived – dived", "draw – drew – drawn", "dream – dreamt/dreamed – dreamt/dreamed"],
        "correct": 0
    },
    {
        "question": "Sho'ng'imoq",
        "options": ["dive – dove/dived – dived", "draw – drew – drawn", "dream – dreamt/dreamed – dreamt/dreamed", "feed – fed – fed"],
        "correct": 0
    },
    {
        "question": "Chizmoq, tortmoq",
        "options": ["draw – drew – drawn", "dream – dreamt/dreamed – dreamt/dreamed", "feed – fed – fed", "flee – fled – fled"],
        "correct": 0
    },
    {
        "question": "Tush ko'rmoq",
        "options": ["dream – dreamt/dreamed – dreamt/dreamed", "feed – fed – fed", "flee – fled – fled", "fling – flung – flung"],
        "correct": 0
    },
    {
        "question": "Boqmoq, ovqat bermoq",
        "options": ["feed – fed – fed", "flee – fled – fled", "fling – flung – flung", "grind – ground – ground"],
        "correct": 0
    },
    {
        "question": "Qochmoq",
        "options": ["flee – fled – fled", "fling – flung – flung", "grind – ground – ground", "hear – heard – heard"],
        "correct": 0
    },
    {
        "question": "Otmoq, uloqtirmoq",
        "options": ["fling – flung – flung", "grind – ground – ground", "hear – heard – heard", "lead – led – led"],
        "correct": 0
    },
    {
        "question": "Maydamoq, yanchmoq",
        "options": ["grind – ground – ground", "hear – heard – heard", "lead – led – led", "lend – lent – lent"],
        "correct": 0
    },
    {
        "question": "Eshitmoq",
        "options": ["hear – heard – heard", "lead – led – led", "lend – lent – lent", "write – wrote – written"],
        "correct": 0
    },
    {
        "question": "Rahnamolik qilmoq, boshlmoq",
        "options": ["lead – led – led", "lend – lent – lent", "write – wrote – written", "arise – arose – arisen"],
        "correct": 0
    },
    {
        "question": "Qarzga bermoq",
        "options": ["lend – lent – lent", "write – wrote – written", "arise – arose – arisen", "awake – awoke – awoken"],
        "correct": 0
    }
],

  "irregular_verbs_all": [
    {
      "question": "Bo'lmoq",
      "options": ["be – was/were – been", "beat – beat – beaten", "become – became – become", "begin – began – begun"],
      "correct": 0
    },
    {
      "question": "Urilmoq",
      "options": ["beat – beat – beaten", "become – became – become", "begin – began – begun", "bend – bent – bent"],
      "correct": 0
    },
    {
      "question": "Bo'lmoq (o'zgarish)",
      "options": ["become – became – become", "begin – began – begun", "bend – bent – bent", "bet – bet – bet"],
      "correct": 0
    },
    {
      "question": "Boshlanmoq",
      "options": ["begin – began – begun", "bend – bent – bent", "bet – bet – bet", "bite – bit – bitten"],
      "correct": 0
    },
    {
      "question": "Egilmoq",
      "options": ["bend – bent – bent", "bet – bet – bet", "bite – bit – bitten", "blow – blew – blown"],
      "correct": 0
    },
    {
      "question": "Tishlamoq",
      "options": ["bite – bit – bitten", "blow – blew – blown", "break – broke – broken", "bring – brought – brought"],
      "correct": 0
    },
    {
      "question": "Puflamoq",
      "options": ["blow – blew – blown", "break – broke – broken", "bring – brought – brought", "build – built – built"],
      "correct": 0
    },
    {
      "question": "Sindirmoq",
      "options": ["break – broke – broken", "bring – brought – brought", "build – built – built", "burn – burned/burnt – burned/burnt"],
      "correct": 0
    },
    {
      "question": "Olib kelmoq",
      "options": ["bring – brought – brought", "build – built – built", "burn – burned/burnt – burned/burnt", "buy – bought – bought"],
      "correct": 0
    },
    {
      "question": "Qurmoq",
      "options": ["build – built – built", "burn – burned/burnt – burned/burnt", "buy – bought – bought", "catch – caught – caught"],
      "correct": 0
    },
    {
      "question": "Yonmoq",
      "options": ["burn – burned/burnt – burned/burnt", "buy – bought – bought", "catch – caught – caught", "choose – chose – chosen"],
      "correct": 0
    },
    {
      "question": "Sotib olmoq",
      "options": ["buy – bought – bought", "catch – caught – caught", "choose – chose – chosen", "come – came – come"],
      "correct": 0
    },
    {
      "question": "Tutmoq",
      "options": ["catch – caught – caught", "choose – chose – chosen", "come – came – come", "cost – cost – cost"],
      "correct": 0
    },
    {
      "question": "Tanlamoq",
      "options": ["choose – chose – chosen", "come – came – come", "cost – cost – cost", "cut – cut – cut"],
      "correct": 0
    },
    {
      "question": "Kelmoq",
      "options": ["come – came – come", "cost – cost – cost", "cut – cut – cut", "dig – dug – dug"],
      "correct": 0
    },
    {
      "question": "Narx turmoq",
      "options": ["cost – cost – cost", "cut – cut – cut", "dig – dug – dug", "do – did – done"],
      "correct": 0
    },
    {
      "question": "Kesmoq",
      "options": ["cut – cut – cut", "dig – dug – dug", "do – did – done", "draw – drew – drawn"],
      "correct": 0
    },
    {
      "question": "Qazimoq",
      "options": ["dig – dug – dug", "do – did – done", "draw – drew – drawn", "drink – drank – drunk"],
      "correct": 0
    },
    {
      "question": "Qilmoq",
      "options": ["do – did – done", "draw – drew – drawn", "drink – drank – drunk", "drive – drove – driven"],
      "correct": 0
    },
    {
      "question": "Chizmoq",
      "options": ["draw – drew – drawn", "drink – drank – drunk", "drive – drove – driven", "eat – ate – eaten"],
      "correct": 0
    },
    {
      "question": "Ichmoq",
      "options": ["drink – drank – drunk", "drive – drove – driven", "eat – ate – eaten", "fall – fell – fallen"],
      "correct": 0
    },
    {
      "question": "Haydamoq",
      "options": ["drive – drove – driven", "eat – ate – eaten", "fall – fell – fallen", "feed – fed – fed"],
      "correct": 0
    },
    {
      "question": "Yemoq",
      "options": ["eat – ate – eaten", "fall – fell – fallen", "feed – fed – fed", "feel – felt – felt"],
      "correct": 0
    },
    {
      "question": "Yiqilmoq",
      "options": ["fall – fell – fallen", "feed – fed – fed", "feel – felt – felt", "fight – fought – fought"],
      "correct": 0
    },
    {
      "question": "Boqmoq",
      "options": ["feed – fed – fed", "feel – felt – felt", "fight – fought – fought", "find – found – found"],
      "correct": 0
    },
    {
      "question": "Hiss qilmoq",
      "options": ["feel – felt – felt", "fight – fought – fought", "find – found – found", "fly – flew – flown"],
      "correct": 0
    },
    {
      "question": "Jang qilmoq",
      "options": ["fight – fought – fought", "find – found – found", "fly – flew – flown", "forget – forgot – forgotten"],
      "correct": 0
    },
    {
      "question": "Topmoq",
      "options": ["find – found – found", "fly – flew – flown", "forget – forgot – forgotten", "forgive – forgave – forgiven"],
      "correct": 0
    },
    {
      "question": "Uchmoq",
      "options": ["fly – flew – flown", "forget – forgot – forgotten", "forgive – forgave – forgiven", "freeze – froze – frozen"],
      "correct": 0
    },
    {
      "question": "Unutmoq",
      "options": ["forget – forgot – forgotten", "forgive – forgave – forgiven", "freeze – froze – frozen", "get – got – gotten"],
      "correct": 0
    },
    {
      "question": "Kechirmoq",
      "options": ["forgive – forgave – forgiven", "freeze – froze – frozen", "get – got – gotten", "give – gave – given"],
      "correct": 0
    },
    {
      "question": "Muzlamoq",
      "options": ["freeze – froze – frozen", "get – got – gotten", "give – gave – given", "go – went – gone"],
      "correct": 0
    },
    {
      "question": "Olishmoq",
      "options": ["get – got – gotten", "give – gave – given", "go – went – gone", "grow – grew – grown"],
      "correct": 0
    },
    {
      "question": "Bermoq",
      "options": ["give – gave – given", "go – went – gone", "grow – grew – grown", "hang – hung – hung"],
      "correct": 0
    },
    {
      "question": "Ketmoq",
      "options": ["go – went – gone", "grow – grew – grown", "hang – hung – hung", "have – had – had"],
      "correct": 0
    },
    {
      "question": "O'smoq",
      "options": ["grow – grew – grown", "hang – hung – hung", "have – had – had", "hear – heard – heard"],
      "correct": 0
    },
    {
      "question": "Osilmoq",
      "options": ["hang – hung – hung", "have – had – had", "hear – heard – heard", "hide – hid – hidden"],
      "correct": 0
    },
    {
      "question": "Egallamoq",
      "options": ["have – had – had", "hear – heard – heard", "hide – hid – hidden", "hit – hit – hit"],
      "correct": 0
    },
    {
      "question": "Eshitmoq",
      "options": ["hear – heard – heard", "hide – hid – hidden", "hit – hit – hit", "hold – held – held"],
      "correct": 0
    },
    {
      "question": "Yashirmoq",
      "options": ["hide – hid – hidden", "hit – hit – hit", "hold – held – held", "hurt – hurt – hurt"],
      "correct": 0
    },
    {
      "question": "Urilmoq",
      "options": ["hit – hit – hit", "hold – held – held", "hurt – hurt – hurt", "keep – kept – kept"],
      "correct": 0
    },
    {
      "question": "Uslab turmoq",
      "options": ["hold – held – held", "hurt – hurt – hurt", "keep – kept – kept", "know – knew – known"],
      "correct": 0
    },
    {
      "question": "Alam qilmoq",
      "options": ["hurt – hurt – hurt", "keep – kept – kept", "know – knew – known", "lay – laid – laid"],
      "correct": 0
    },
    {
      "question": "Saqlab turmoq",
      "options": ["keep – kept – kept", "know – knew – known", "lay – laid – laid", "lead – led – led"],
      "correct": 0
    },
    {
      "question": "Bilmoq",
      "options": ["know – knew – known", "lay – laid – laid", "lead – led – led", "leave – left – left"],
      "correct": 0
    },
    {
      "question": "Qo'yishmoq",
      "options": ["lay – laid – laid", "lead – led – led", "leave – left – left", "lend – lent – lent"],
      "correct": 0
    },
    {
      "question": "Boshqarmoq",
      "options": ["lead – led – led", "leave – left – left", "lend – lent – lent", "let – let – let"],
      "correct": 0
    },
    {
      "question": "Ketishmoq",
      "options": ["leave – left – left", "lend – lent – lent", "let – let – let", "lie – lay – lain"],
      "correct": 0
    },
    {
      "question": "Qarzga bermoq",
      "options": ["lend – lent – lent", "let – let – let", "lie – lay – lain", "lose – lost – lost"],
      "correct": 0
    },
    {
      "question": "Ruxsat bermoq",
      "options": ["let – let – let", "lie – lay – lain", "lose – lost – lost", "make – made – made"],
      "correct": 0
    },
    {
      "question": "Yotishmoq",
      "options": ["lie – lay – lain", "lose – lost – lost", "make – made – made", "mean – meant – meant"],
      "correct": 0
    },
    {
      "question": "Yo'qotmoq",
      "options": ["lose – lost – lost", "make – made – made", "mean – meant – meant", "meet – met – met"],
      "correct": 0
    },
    {
      "question": "Qilmoq, yasamoq",
      "options": ["make – made – made", "mean – meant – meant", "meet – met – met", "pay – paid – paid"],
      "correct": 0
    },
    {
      "question": "Anglatmoq",
      "options": ["mean – meant – meant", "meet – met – met", "pay – paid – paid", "put – put – put"],
      "correct": 0
    },
    {
      "question": "Uchrashmoq",
      "options": ["meet – met – met", "pay – paid – paid", "put – put – put", "read – read – read"],
      "correct": 0
    },
    {
      "question": "To'lamoq",
      "options": ["pay – paid – paid", "put – put – put", "read – read – read", "ride – rode – ridden"],
      "correct": 0
    },
    {
      "question": "Qo'yishmoq",
      "options": ["put – put – put", "read – read – read", "ride – rode – ridden", "ring – rang – rung"],
      "correct": 0
    },
    {
      "question": "O'qimoq",
      "options": ["read – read – read", "ride – rode – ridden", "ring – rang – rung", "rise – rose – risen"],
      "correct": 0
    },
    {
      "question": "Minmoq",
      "options": ["ride – rode – ridden", "ring – rang – rung", "rise – rose – risen", "run – ran – run"],
      "correct": 0
    },
    {
      "question": "Qo'ng'iroq qilmoq",
      "options": ["ring – rang – rung", "rise – rose – risen", "run – ran – run", "say – said – said"],
      "correct": 0
    },
    {
      "question": "Ko'tarilmoq",
      "options": ["rise – rose – risen", "run – ran – run", "say – said – said", "see – saw – seen"],
      "correct": 0
    },
    {
      "question": "Yugurmoq",
      "options": ["run – ran – run", "say – said – said", "see – saw – seen", "seek – sought – sought"],
      "correct": 0
    },
    {
      "question": "Aytmoq",
      "options": ["say – said – said", "see – saw – seen", "seek – sought – sought", "sell – sold – sold"],
      "correct": 0
    },
    {
      "question": "Ko'rmoq",
      "options": ["see – saw – seen", "seek – sought – sought", "sell – sold – sold", "send – sent – sent"],
      "correct": 0
    },
    {
      "question": "Izlamoq",
      "options": ["seek – sought – sought", "sell – sold – sold", "send – sent – sent", "set – set – set"],
      "correct": 0
    },
    {
      "question": "Sotmoq",
      "options": ["sell – sold – sold", "send – sent – sent", "set – set – set", "shake – shook – shaken"],
      "correct": 0
    },
    {
      "question": "Yubormoq",
      "options": ["send – sent – sent", "set – set – set", "shake – shook – shaken", "shine – shone – shone"],
      "correct": 0
    },
    {
      "question": "O'rnatmoq",
      "options": ["set – set – set", "shake – shook – shaken", "shine – shone – shone", "shoot – shot – shot"],
      "correct": 0
    },
    {
      "question": "Silkitmoq",
      "options": ["shake – shook – shaken", "shine – shone – shone", "shoot – shot – shot", "show – showed – shown"],
      "correct": 0
    },
    {
      "question": "Yaltiramoq",
      "options": ["shine – shone – shone", "shoot – shot – shot", "show – showed – shown", "shut – shut – shut"],
      "correct": 0
    },
    {
      "question": "O'q otmoq",
      "options": ["shoot – shot – shot", "show – showed – shown", "shut – shut – shut", "sing – sang – sung"],
      "correct": 0
    },
    {
      "question": "Ko'rsatmoq",
      "options": ["show – showed – shown", "shut – shut – shut", "sing – sang – sung", "sit – sat – sat"],
      "correct": 0
    },
    {
      "question": "Yopmoq",
      "options": ["shut – shut – shut", "sing – sang – sung", "sit – sat – sat", "sleep – slept – slept"],
      "correct": 0
    },
    {
      "question": "Kuylamoq",
      "options": ["sing – sang – sung", "sit – sat – sat", "sleep – slept – slept", "slide – slid – slid"],
      "correct": 0
    },
    {
      "question": "O'tirib olmoq",
      "options": ["sit – sat – sat", "sleep – slept – slept", "slide – slid – slid", "speak – spoke – spoken"],
      "correct": 0
    },
    {
      "question": "Uxlamoq",
      "options": ["sleep – slept – slept", "slide – slid – slid", "speak – spoke – spoken", "spend – spent – spent"],
      "correct": 0
    },
    {
      "question": "Sirpanmoq",
      "options": ["slide – slid – slid", "speak – spoke – spoken", "spend – spent – spent", "spit – spat – spat"],
      "correct": 0
    },
    {
      "question": "Gapirmoq",
      "options": ["speak – spoke – spoken", "spend – spent – spent", "spit – spat – spat", "split – split – split"],
      "correct": 0
    },
    {
      "question": "Sarflamoq",
      "options": ["spend – spent – spent", "spit – spat – spat", "split – split – split", "spread – spread – spread"],
      "correct": 0
    },
    {
      "question": "Tupurmoq",
      "options": ["spit – spat – spat", "split – split – split", "spread – spread – spread", "stand – stood – stood"],
      "correct": 0
    },
    {
      "question": "Bo'lmoq (yoriq)",
      "options": ["split – split – split", "spread – spread – spread", "stand – stood – stood", "steal – stole – stolen"],
      "correct": 0
    },
    {
      "question": "Yoymoq",
      "options": ["spread – spread – spread", "stand – stood – stood", "steal – stole – stolen", "stick – stuck – stuck"],
      "correct": 0
    },
    {
      "question": "Turmoq",
      "options": ["stand – stood – stood", "steal – stole – stolen", "stick – stuck – stuck", "sting – stung – stung"],
      "correct": 0
    },
    {
      "question": "O'g'irlamoq",
      "options": ["steal – stole – stolen", "stick – stuck – stuck", "sting – stung – stung", "stink – stank – stunk"],
      "correct": 0
    },
    {
      "question": "Yopishtirmoq",
      "options": ["stick – stuck – stuck", "sting – stung – stung", "stink – stank – stunk", "strike – struck – struck"],
      "correct": 0
    },
    {
      "question": "Chaqmoq (ari)",
      "options": ["sting – stung – stung", "stink – stank – stunk", "strike – struck – struck", "swear – swore – sworn"],
      "correct": 0
    },
    {
      "question": "Sasimoq",
      "options": ["stink – stank – stunk", "strike – struck – struck", "swear – swore – sworn", "sweep – swept – swept"],
      "correct": 0
    },
    {
      "question": "Urmoq",
      "options": ["strike – struck – struck", "swear – swore – sworn", "sweep – swept – swept", "swim – swam – swum"],
      "correct": 0
    },
    {
      "question": "Qasam ichmoq",
      "options": ["swear – swore – sworn", "sweep – swept – swept", "swim – swam – swum", "swing – swung – swung"],
      "correct": 0
    },
    {
      "question": "Supurmoq",
      "options": ["sweep – swept – swept", "swim – swam – swum", "swing – swung – swung", "take – took – taken"],
      "correct": 0
    },
    {
      "question": "Suzmoq",
      "options": ["swim – swam – swum", "swing – swung – swung", "take – took – taken", "teach – taught – taught"],
      "correct": 0
    },
    {
      "question": "Tegirmoq",
      "options": ["swing – swung – swung", "take – took – taken", "teach – taught – taught", "tear – tore – torn"],
      "correct": 0
    },
    {
      "question": "Olishmoq",
      "options": ["take – took – taken", "teach – taught – taught", "tear – tore – torn", "tell – told – told"],
      "correct": 0
    },
    {
      "question": "O'rgatmoq",
      "options": ["teach – taught – taught", "tear – tore – torn", "tell – told – told", "think – thought – thought"],
      "correct": 0
    },
    {
      "question": "Yirtmoq",
      "options": ["tear – tore – torn", "tell – told – told", "think – thought – thought", "throw – threw – thrown"],
      "correct": 0
    },
    {
      "question": "Aytmoq",
      "options": ["tell – told – told", "think – thought – thought", "throw – threw – thrown", "understand – understood – understood"],
      "correct": 0
    },
    {
      "question": "O'ylamoq",
      "options": ["think – thought – thought", "throw – threw – thrown", "understand – understood – understood", "wake – woke – woken"],
      "correct": 0
    },
    {
      "question": "Otmoq",
      "options": ["throw – threw – thrown", "understand – understood – understood", "wake – woke – woken", "wear – wore – worn"],
      "correct": 0
    },
    {
      "question": "Tushunmoq",
      "options": ["understand – understood – understood", "wake – woke – woken", "wear – wore – worn", "weep – wept – wept"],
      "correct": 0
    },
    {
      "question": "Uyg'otmoq",
      "options": ["wake – woke – woken", "wear – wore – worn", "weep – wept – wept", "win – won – won"],
      "correct": 0
    },
    {
      "question": "Kiyinmoq",
      "options": ["wear – wore – worn", "weep – wept – wept", "win – won – won", "write – wrote – written"],
      "correct": 0
    },
    {
      "question": "Yig'lamoq",
      "options": ["weep – wept – wept", "win – won – won", "write – wrote – written", "be – was/were – been"],
      "correct": 0
    },
    {
      "question": "Yutmoq",
      "options": ["win – won – won", "write – wrote – written", "be – was/were – been", "beat – beat – beaten"],
      "correct": 0
    },
    {
      "question": "Yozmoq",
      "options": ["write – wrote – written", "be – was/were – been", "beat – beat – beaten", "become – became – become"],
      "correct": 0
    }
  ]
,
 

  "present_simple": [
    {
      "question": "Gap qismlarini raqamlar tartibida joylashtiring: \"1=She\", \"2=works\", \"3=in a hospital\"",
      "numbered_options": {
        "1": "She",
        "2": "works",
        "3": "in a hospital"
      },
      "options": ["1,2,3", "3,2,1", "2,1,3"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Subject + Verb + Place"
    },
    {
      "question": "Gap qismlarini tartiblang: \"1=They\", \"2=play\", \"3=football\", \"4=every weekend\"",
      "numbered_options": {
        "1": "They",
        "2": "play",
        "3": "football",
        "4": "every weekend"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Subject + Verb + Object + Time"
    },
    {
      "question": "To'g'ri tartibni tanlang: \"1=The sun\", \"2=rises\", \"3=in the east\"",
      "numbered_options": {
        "1": "The sun",
        "2": "rises",
        "3": "in the east"
      },
      "options": ["1,2,3", "3,1,2", "2,3,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Universal truths"
    },
    {
      "question": "Gap tuzing: \"1=We\", \"2=don't\", \"3=eat\", \"4=meat\"",
      "numbered_options": {
        "1": "We",
        "2": "don't",
        "3": "eat",
        "4": "meat"
      },
      "options": ["1,2,3,4", "4,2,3,1", "2,1,3,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Negative form"
    },
    {
      "question": "Tartiblang: \"1=My teacher\", \"2=speaks\", \"3=English\", \"4=very well\"",
      "numbered_options": {
        "1": "My teacher",
        "2": "speaks",
        "3": "English",
        "4": "very well"
      },
      "options": ["1,2,3,4", "4,2,3,1", "3,1,2,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Subject + Verb + Object + Manner"
    },
    {
      "question": "Gap qismlarini joylashtiring: \"1=Children\", \"2=like\", \"3=ice cream\"",
      "numbered_options": {
        "1": "Children",
        "2": "like",
        "3": "ice cream"
      },
      "options": ["1,2,3", "3,2,1", "2,1,3"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Subject + Verb + Object"
    },
    {
      "question": "To'g'ri tartib: \"1=He\", \"2=goes\", \"3=to school\", \"4=by bus\"",
      "numbered_options": {
        "1": "He",
        "2": "goes",
        "3": "to school",
        "4": "by bus"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Subject + Verb + Place + Transport"
    },
    {
      "question": "Gap tuzing: \"1=I\", \"2=always\", \"3=do\", \"4=my homework\"",
      "numbered_options": {
        "1": "I",
        "2": "always",
        "3": "do",
        "4": "my homework"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Adverb position"
    },
    {
      "question": "Tartiblang: \"1=The train\", \"2=arrives\", \"3=at 9 AM\"",
      "numbered_options": {
        "1": "The train",
        "2": "arrives",
        "3": "at 9 AM"
      },
      "options": ["1,2,3", "3,2,1", "2,1,3"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Timetable events"
    },
    {
      "question": "Gap qismlarini joylashtiring: \"1=You\", \"2=need\", \"3=a visa\", \"4=to travel\"",
      "numbered_options": {
        "1": "You",
        "2": "need",
        "3": "a visa",
        "4": "to travel"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,4,3"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Subject + Verb + Object + Infinitive"
    },

    {
      "question": "Gap tuzing: \"1=She\", \"2=rarely\", \"3=watches\", \"4=TV\", \"5=in the evening\"",
      "numbered_options": {
        "1": "She",
        "2": "rarely",
        "3": "watches",
        "4": "TV",
        "5": "in the evening"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Frequency adverbs"
    },
    {
      "question": "Tartiblang: \"1=Does\", \"2=your brother\", \"3=work\", \"4=in Tashkent\"",
      "numbered_options": {
        "1": "Does",
        "2": "your brother",
        "3": "work",
        "4": "in Tashkent"
      },
      "options": ["1,2,3,4", "2,1,3,4", "4,3,2,1"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Yes/No questions"
    },
    {
      "question": "Gap qismlarini joylashtiring: \"1=What\", \"2=do\", \"3=you\", \"4=do\", \"5=on weekends\"",
      "numbered_options": {
        "1": "What",
        "2": "do",
        "3": "you",
        "4": "do",
        "5": "on weekends"
      },
      "options": ["1,2,3,4,5", "3,2,1,4,5", "5,4,3,2,1"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Wh- questions"
    },
    {
      "question": "To'g'ri tartib: \"1=My parents\", \"2=don't\", \"3=speak\", \"4=French\"",
      "numbered_options": {
        "1": "My parents",
        "2": "don't",
        "3": "speak",
        "4": "French"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Negative form (plural)"
    },
    {
      "question": "Gap tuzing: \"1=How often\", \"2=do\", \"3=you\", \"4=visit\", \"5=your grandparents\"",
      "numbered_options": {
        "1": "How often",
        "2": "do",
        "3": "you",
        "4": "visit",
        "5": "your grandparents"
      },
      "options": ["1,2,3,4,5", "3,2,1,4,5", "5,4,3,2,1"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Frequency questions"
    },
    {
      "question": "Tartiblang: \"1=The meeting\", \"2=starts\", \"3=at 3 PM\", \"4=sharp\"",
      "numbered_options": {
        "1": "The meeting",
        "2": "starts",
        "3": "at 3 PM",
        "4": "sharp"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Scheduled events"
    },
    {
      "question": "Gap qismlarini joylashtiring: \"1=Why\", \"2=does\", \"3=he\", \"4=need\", \"5=a new phone\"",
      "numbered_options": {
        "1": "Why",
        "2": "does",
        "3": "he",
        "4": "need",
        "5": "a new phone"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "3,2,1,4,5"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Reason questions"
    },
    {
      "question": "To'g'ri tartib: \"1=This shop\", \"2=doesn't\", \"3=sell\", \"4=electronics\"",
      "numbered_options": {
        "1": "This shop",
        "2": "doesn't",
        "3": "sell",
        "4": "electronics"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Negative (3rd person)"
    },
    {
      "question": "Gap tuzing: \"1=Where\", \"2=do\", \"3=your friends\", \"4=live\"",
      "numbered_options": {
        "1": "Where",
        "2": "do",
        "3": "your friends",
        "4": "live"
      },
      "options": ["1,2,3,4", "3,2,1,4", "4,3,2,1"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Place questions"
    },
    {
      "question": "Tartiblang: \"1=The bus\", \"2=doesn't\", \"3=stop\", \"4=here\", \"5=after midnight\"",
      "numbered_options": {
        "1": "The bus",
        "2": "doesn't",
        "3": "stop",
        "4": "here",
        "5": "after midnight"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Negative + time limitation"
    },

    {
      "question": "Gap tuzing: \"1=By the time\", \"2=we arrive\", \"3=the movie\", \"4=will have\", \"5=already started\"",
      "numbered_options": {
        "1": "By the time",
        "2": "we arrive",
        "3": "the movie",
        "4": "will have",
        "5": "already started"
      },
      "options": ["1,2,3,4,5", "3,4,5,1,2", "2,1,3,4,5"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Future perfect"
    },
    {
      "question": "Tartiblang: \"1=Had\", \"2=you\", \"3=ever\", \"4=visited\", \"5=Samarkand\", \"6=before 2020\"",
      "numbered_options": {
        "1": "Had",
        "2": "you",
        "3": "ever",
        "4": "visited",
        "5": "Samarkand",
        "6": "before 2020"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Past perfect question"
    },
    {
      "question": "Gap qismlarini joylashtiring: \"1=The report\", \"2=is being\", \"3=prepared\", \"4=by the team\", \"5=right now\"",
      "numbered_options": {
        "1": "The report",
        "2": "is being",
        "3": "prepared",
        "4": "by the team",
        "5": "right now"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Present continuous passive"
    },
    {
      "question": "To'g'ri tartib: \"1=Not only\", \"2=does she\", \"3=speak\", \"4=English\", \"5=but also\", \"6=French\"",
      "numbered_options": {
        "1": "Not only",
        "2": "does she",
        "3": "speak",
        "4": "English",
        "5": "but also",
        "6": "French"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Inversion with not only"
    },
    {
      "question": "Gap tuzing: \"1=Were\", \"2=you\", \"3=to visit\", \"4=Uzbekistan\", \"5=what\", \"6=would you\", \"7=see first\"",
      "numbered_options": {
        "1": "Were",
        "2": "you",
        "3": "to visit",
        "4": "Uzbekistan",
        "5": "what",
        "6": "would you",
        "7": "see first"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "5,6,7,1,2,3,4"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Were + infinitive conditional"
    },
    {
      "question": "Tartiblang: \"1=Hardly\", \"2=had\", \"3=I\", \"4=arrived\", \"5=when\", \"6=the phone\", \"7=rang\"",
      "numbered_options": {
        "1": "Hardly",
        "2": "had",
        "3": "I",
        "4": "arrived",
        "5": "when",
        "6": "the phone",
        "7": "rang"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "3,2,1,4,5,6,7"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Inversion with hardly"
    },
    {
      "question": "Gap qismlarini joylashtiring: \"1=Such\", \"2=was\", \"3=the noise\", \"4=that\", \"5=we\", \"6=couldn't\", \"7=sleep\"",
      "numbered_options": {
        "1": "Such",
        "2": "was",
        "3": "the noise",
        "4": "that",
        "5": "we",
        "6": "couldn't",
        "7": "sleep"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "3,2,1,4,5,6,7"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Such...that structure"
    },
    {
      "question": "To'g'ri tartib: \"1=No sooner\", \"2=had\", \"3=she\", \"4=left\", \"5=than\", \"6=it\", \"7=started\", \"8=raining\"",
      "numbered_options": {
        "1": "No sooner",
        "2": "had",
        "3": "she",
        "4": "left",
        "5": "than",
        "6": "it",
        "7": "started",
        "8": "raining"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "3,2,1,4,5,6,7,8"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "No sooner...than"
    },
    {
      "question": "Gap tuzing: \"1=Only\", \"2=when\", \"3=the teacher\", \"4=explained\", \"5=the rule\", \"6=did I\", \"7=understand\", \"8=it\"",
      "numbered_options": {
        "1": "Only",
        "2": "when",
        "3": "the teacher",
        "4": "explained",
        "5": "the rule",
        "6": "did I",
        "7": "understand",
        "8": "it"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "3,4,5,1,2,6,7,8"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Inversion with only"
    },
    {
      "question": "Tartiblang: \"1=Under no circumstances\", \"2=should\", \"3=you\", \"4=open\", \"5=this door\", \"6=during\", \"7=an emergency\"",
      "numbered_options": {
        "1": "Under no circumstances",
        "2": "should",
        "3": "you",
        "4": "open",
        "5": "this door",
        "6": "during",
        "7": "an emergency"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "3,2,1,4,5,6,7"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Negative adverbial inversion"
    }
  ],
  "metadata": {
    "total_questions": 30,
    "levels": {
      "easy": 10,
      "normal": 10,
      "hard": 10
    },
    "grammar_points_covered": [
      "Present Simple",
      "Present Continuous",
      "Present Perfect",
      "Past Perfect",
      "Future Perfect",
      "Passive Voice",
      "Conditionals",
      "Inversion",
      "Question Forms"
    ],
    "recommended_time": "20-30 minutes"
  }

 


,
 "present_continuous": [
    {
      "question": "Gap qismlarini tartiblang (emphatic form): \"1=I\", \"2=AM\", \"3=TELLING\", \"4=you\", \"5=the truth\"",
      "numbered_options": {
        "1": "I",
        "2": "AM",
        "3": "TELLING",
        "4": "you",
        "5": "the truth"
      },
      "options": ["1,2,3,4,5", "1,3,2,4,5", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Emphatic present continuous",
      "hint": "Stress on auxiliary verb for emphasis"
    },
    {
      "question": "Tartiblang (double action): \"1=While\", \"2=she\", \"3=is cooking\", \"4=dinner\", \"5=her husband\", \"6=is watching\", \"7=TV\"",
      "numbered_options": {
        "1": "While",
        "2": "she",
        "3": "is cooking",
        "4": "dinner",
        "5": "her husband",
        "6": "is watching",
        "7": "TV"
      },
      "options": ["1,2,3,4,5,6,7", "5,6,7,1,2,3,4", "1,5,6,7,2,3,4"],
      "correct": 0,
      "grammar_point": "Parallel actions",
      "hint": "Two simultaneous actions with while"
    },
    {
      "question": "Gap tuzing (changing meaning verb): \"1=He\", \"2=is being\", \"3=very\", \"4=careful\", \"5=with\", \"6=that antique\"",
      "numbered_options": {
        "1": "He",
        "2": "is being",
        "3": "very",
        "4": "careful",
        "5": "with",
        "6": "that antique"
      },
      "options": ["1,2,3,4,5,6", "1,3,4,5,6,2", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Stative verb with continuous",
      "hint": "'Be' in continuous shows temporary behavior"
    },
    {
      "question": "Joylashtiring (future arrangement): \"1=This\", \"2=time\", \"3=next week\", \"4=we\", \"5='re flying\", \"6=to\", \"7=Paris\"",
      "numbered_options": {
        "1": "This",
        "2": "time",
        "3": "next week",
        "4": "we",
        "5": "'re flying",
        "6": "to",
        "7": "Paris"
      },
      "options": ["1,2,3,4,5,6,7", "4,5,6,7,1,2,3", "3,1,2,4,5,6,7"],
      "correct": 0,
      "grammar_point": "Fixed future arrangements",
      "hint": "Present continuous for scheduled future events"
    },
    {
      "question": "Tartiblang (complaint): \"1=That child\", \"2=is constantly\", \"3=interrupting\", \"4=the\", \"5=teacher\"",
      "numbered_options": {
        "1": "That child",
        "2": "is constantly",
        "3": "interrupting",
        "4": "the",
        "5": "teacher"
      },
      "options": ["1,2,3,4,5", "1,3,2,4,5", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Annoying habits",
      "hint": "Adverbs of frequency + continuous for irritation"
    },
    {
      "question": "Gap tuzing (passive): \"1=A new bridge\", \"2=is being\", \"3=built\", \"4=across\", \"5=the river\"",
      "numbered_options": {
        "1": "A new bridge",
        "2": "is being",
        "3": "built",
        "4": "across",
        "5": "the river"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Present continuous passive",
      "hint": "Object + is being + past participle"
    },
    {
      "question": "Joylashtiring (negative question): \"1=Why\", \"2=isn't\", \"3=the\", \"4=computer\", \"5=working\", \"6=properly\"",
      "numbered_options": {
        "1": "Why",
        "2": "isn't",
        "3": "the",
        "4": "computer",
        "5": "working",
        "6": "properly"
      },
      "options": ["1,2,3,4,5,6", "3,4,5,6,1,2", "2,3,4,5,1,6"],
      "correct": 0,
      "grammar_point": "Negative questions",
      "hint": "Wh- word + isn't + subject + -ing form"
    },
    {
      "question": "Tartiblang (state verb exception): \"1=I\", \"2='m\", \"3=seeing\", \"4=the\", \"5=doctor\", \"6=tomorrow\"",
      "numbered_options": {
        "1": "I",
        "2": "'m",
        "3": "seeing",
        "4": "the",
        "5": "doctor",
        "6": "tomorrow"
      },
      "options": ["1,2,3,4,5,6", "4,5,1,2,3,6", "6,5,4,3,2,1"],
      "correct": 0,
      "grammar_point": "State verbs in continuous",
      "hint": "'See' can be continuous for planned meetings"
    },
    {
      "question": "Gap tuzing (question tag): \"1=You\", \"2='re\", \"3=not\", \"4=listening\", \"5=to\", \"6=me\", \"7=are you\"",
      "numbered_options": {
        "1": "You",
        "2": "'re",
        "3": "not",
        "4": "listening",
        "5": "to",
        "6": "me",
        "7": "are you"
      },
      "options": ["1,2,3,4,5,6,7", "1,2,4,5,6,3,7", "7,6,5,4,3,2,1"],
      "correct": 0,
      "grammar_point": "Question tags",
      "hint": "Negative statement + positive tag"
    },
    {
      "question": "Joylashtiring (mixed tenses): \"1=While\", \"2=we\", \"3='re discussing\", \"4=this\", \"5=the situation\", \"6=is getting\", \"7=worse\"",
      "numbered_options": {
        "1": "While",
        "2": "we",
        "3": "'re discussing",
        "4": "this",
        "5": "the situation",
        "6": "is getting",
        "7": "worse"
      },
      "options": ["1,2,3,4,5,6,7", "5,6,7,1,2,3,4", "2,3,4,1,5,6,7"],
      "correct": 0,
      "grammar_point": "Background action + development",
      "hint": "Continuous for both parallel and changing situations"
    }
  ],
  "metadata": {
    "difficulty_features": {
      "complex_structures": ["Passive voice", "Question tags", "Negative questions"],
      "special_cases": ["State verbs", "Emphatic forms", "Future meaning"],
      "sentence_length": "7-8 parts",
      "cognitive_load": "High (requires analyzing multiple grammar points)"
    },
    "scoring": {
      "points_per_question": 3,
      "bonus_points": {
        "explain_grammar": "+1",
        "identify_exception": "+1"
      }
    }
  }
,

 "present_perfect": [
    {
      "question": "Tartiblang: \"1=I\", \"2=have\", \"3=visited\", \"4=France\", \"5=before\"",
      "numbered_options": {
        "1": "I",
        "2": "have",
        "3": "visited",
        "4": "France",
        "5": "before"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "3,4,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=has\", \"3=finished\", \"4=her homework\"",
      "numbered_options": {
        "1": "She",
        "2": "has",
        "3": "finished",
        "4": "her homework"
      },
      "options": ["1,2,3,4", "2,1,4,3", "3,4,1,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=have\", \"3=never\", \"4=seen\", \"5=a lion\"",
      "numbered_options": {
        "1": "They",
        "2": "have",
        "3": "never",
        "4": "seen",
        "5": "a lion"
      },
      "options": ["1,2,3,4,5", "4,3,2,1,5", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=He\", \"2=has\", \"3=already\", \"4=eaten\", \"5=lunch\"",
      "numbered_options": {
        "1": "He",
        "2": "has",
        "3": "already",
        "4": "eaten",
        "5": "lunch"
      },
      "options": ["1,2,3,4,5", "2,1,4,3,5", "3,5,2,1,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=have\", \"3=completed\", \"4=the project\"",
      "numbered_options": {
        "1": "We",
        "2": "have",
        "3": "completed",
        "4": "the project"
      },
      "options": ["1,2,3,4", "2,1,4,3", "3,4,1,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=You\", \"2=have\", \"3=visited\", \"4=London\", \"5=twice\"",
      "numbered_options": {
        "1": "You",
        "2": "have",
        "3": "visited",
        "4": "London",
        "5": "twice"
      },
      "options": ["1,2,3,4,5", "2,3,1,5,4", "3,4,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=have\", \"3=worked\", \"4=here\", \"5=for a year\"",
      "numbered_options": {
        "1": "They",
        "2": "have",
        "3": "worked",
        "4": "here",
        "5": "for a year"
      },
      "options": ["1,2,3,4,5", "2,1,4,3,5", "4,3,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=has\", \"3=traveled\", \"4=to Asia\"",
      "numbered_options": {
        "1": "She",
        "2": "has",
        "3": "traveled",
        "4": "to Asia"
      },
      "options": ["1,2,3,4", "2,3,1,4", "3,4,1,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=have\", \"3=seen\", \"4=that movie\"",
      "numbered_options": {
        "1": "We",
        "2": "have",
        "3": "seen",
        "4": "that movie"
      },
      "options": ["1,2,3,4", "2,1,4,3", "3,4,1,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=have\", \"3=started\", \"4=my own business\"",
      "numbered_options": {
        "1": "I",
        "2": "have",
        "3": "started",
        "4": "my own business"
      },
      "options": ["1,2,3,4", "2,3,1,4", "3,4,1,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect"
    }
  ],
   "present_perfect_cont": [
    {
      "question": "Tartiblang: \"1=I\", \"2=have\", \"3=been\", \"4=studying\", \"5=English\"",
      "numbered_options": {
        "1": "I",
        "2": "have",
        "3": "been",
        "4": "studying",
        "5": "English"
      },
      "options": ["1,2,3,4,5", "2,1,3,5,4", "3,4,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=has\", \"3=been\", \"4=working\", \"5=here\"",
      "numbered_options": {
        "1": "She",
        "2": "has",
        "3": "been",
        "4": "working",
        "5": "here"
      },
      "options": ["1,2,3,4,5", "3,4,1,2,5", "2,1,4,3,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=have\", \"3=been\", \"4=waiting\", \"5=for you\"",
      "numbered_options": {
        "1": "They",
        "2": "have",
        "3": "been",
        "4": "waiting",
        "5": "for you"
      },
      "options": ["1,2,3,4,5", "3,5,2,1,4", "4,1,2,3,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=He\", \"2=has\", \"3=been\", \"4=running\", \"5=a marathon\"",
      "numbered_options": {
        "1": "He",
        "2": "has",
        "3": "been",
        "4": "running",
        "5": "a marathon"
      },
      "options": ["1,2,3,4,5", "2,1,4,3,5", "4,3,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=have\", \"3=been\", \"4=working\", \"5=together\"",
      "numbered_options": {
        "1": "We",
        "2": "have",
        "3": "been",
        "4": "working",
        "5": "together"
      },
      "options": ["1,2,3,4,5", "2,1,4,3,5", "3,5,1,4,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=You\", \"2=have\", \"3=been\", \"4=playing\", \"5=soccer\"",
      "numbered_options": {
        "1": "You",
        "2": "have",
        "3": "been",
        "4": "playing",
        "5": "soccer"
      },
      "options": ["1,2,3,4,5", "3,1,4,2,5", "2,5,1,3,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=have\", \"3=been\", \"4=learning\", \"5=Spanish\"",
      "numbered_options": {
        "1": "They",
        "2": "have",
        "3": "been",
        "4": "learning",
        "5": "Spanish"
      },
      "options": ["1,2,3,4,5", "2,1,5,4,3", "3,4,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=has\", \"3=been\", \"4=reading\", \"5=a book\"",
      "numbered_options": {
        "1": "She",
        "2": "has",
        "3": "been",
        "4": "reading",
        "5": "a book"
      },
      "options": ["1,2,3,4,5", "2,1,4,3,5", "3,5,1,2,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=have\", \"3=been\", \"4=watching\", \"5=TV\"",
      "numbered_options": {
        "1": "I",
        "2": "have",
        "3": "been",
        "4": "watching",
        "5": "TV"
      },
      "options": ["1,2,3,4,5", "2,1,4,3,5", "3,4,1,2,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=have\", \"3=been\", \"4=discussing\", \"5=the project\"",
      "numbered_options": {
        "1": "We",
        "2": "have",
        "3": "been",
        "4": "discussing",
        "5": "the project"
      },
      "options": ["1,2,3,4,5", "2,4,1,3,5", "3,1,2,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Present Perfect Continuous"
    }
  ],



  "present_continuous": [
    {
      "question": "Gap tuzing (holiday plans): \"1=We\", \"2=are visiting\", \"3=our\", \"4=grandparents\", \"5=this weekend\"",
      "numbered_options": {
        "1": "We", "2": "are visiting", "3": "our", "4": "grandparents", "5": "this weekend"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Future arrangements",
      "hint": "Present continuous for scheduled plans"
    },
    {
      "question": "Tartiblang (current activity): \"1=Right now\", \"2=the students\", \"3=are preparing\", \"4=for\", \"5=their exams\"",
      "numbered_options": {
        "1": "Right now", "2": "the students", "3": "are preparing", "4": "for", "5": "their exams"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,1,4,5"],
      "correct": 0,
      "grammar_point": "Current actions",
      "hint": "Time marker 'right now' indicates ongoing activity"
    },
    {
      "question": "Gap tuzing (passive): \"1=A new law\", \"2=is being\", \"3=discussed\", \"4=in\", \"5=parliament\", \"6=this week\"",
      "numbered_options": {
        "1": "A new law", "2": "is being", "3": "discussed", "4": "in", "5": "parliament", "6": "this week"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Present continuous passive",
      "hint": "Object + is being + past participle"
    },
    {
      "question": "Joylashtiring (double action): \"1=While\", \"2=I\", \"3=am cooking\", \"4=dinner\", \"5=my husband\", \"6=is setting\", \"7=the table\"",
      "numbered_options": {
        "1": "While", "2": "I", "3": "am cooking", "4": "dinner", "5": "my husband", "6": "is setting", "7": "the table"
      },
      "options": ["1,2,3,4,5,6,7", "5,6,7,1,2,3,4", "2,3,4,1,5,6,7"],
      "correct": 0,
      "grammar_point": "Simultaneous actions",
      "hint": "'While' shows two parallel ongoing actions"
    },
    {
      "question": "Tartiblang (emphatic negative): \"1=I\", \"2=AM NOT\", \"3=EXAGGERATING\", \"4=when\", \"5=I say\", \"6=this\", \"7=is critical\"",
      "numbered_options": {
        "1": "I", "2": "AM NOT", "3": "EXAGGERATING", "4": "when", "5": "I say", "6": "this", "7": "is critical"
      },
      "options": ["1,2,3,4,5,6,7", "4,5,6,7,1,2,3", "2,1,3,4,5,6,7"],
      "correct": 0,
      "grammar_point": "Emphatic negation",
      "hint": "Capitalized auxiliary shows strong emphasis"
    },
    {
      "question": "Gap tuzing (mixed tenses): \"1=As\", \"2=we\", \"3=are speaking\", \"4=the situation\", \"5=is becoming\", \"6=more\", \"7=complicated\"",
      "numbered_options": {
        "1": "As", "2": "we", "3": "are speaking", "4": "the situation", "5": "is becoming", "6": "more", "7": "complicated"
      },
      "options": ["1,2,3,4,5,6,7", "4,5,6,7,1,2,3", "2,3,1,4,5,6,7"],
      "correct": 0,
      "grammar_point": "Background + development",
      "hint": "Continuous for both ongoing action and changing state"
    }
  ],

   "present_perfect": [
       {
      "question": "Gap tuzing (experience): \"1=I\", \"2=have visited\", \"3=Paris\", \"4=twice\"",
      "numbered_options": {
        "1": "I", "2": "have visited", "3": "Paris", "4": "twice"
      },
      "options": ["1,2,3,4", "3,2,1,4", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Life experiences",
      "hint": "Subject + have + past participle"
    },
    {
      "question": "Tartiblang (recent action): \"1=She\", \"2=has just\", \"3=finished\", \"4=her homework\"",
      "numbered_options": {
        "1": "She", "2": "has just", "3": "finished", "4": "her homework"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Recent actions",
      "hint": "'just' indicates very recent completion"
    },
    {
      "question": "Gap tuzing (unfinished time): \"1=We\", \"2=have had\", \"3=three meetings\", \"4=this week\"",
      "numbered_options": {
        "1": "We", "2": "have had", "3": "three meetings", "4": "this week"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Unfinished time periods",
      "hint": "This week is still continuing"
    },
    {
      "question": "Tartiblang (result): \"1=He\", \"2=has lost\", \"3=his\", \"4=passport\"",
      "numbered_options": {
        "1": "He", "2": "has lost", "3": "his", "4": "passport"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Present results",
      "hint": "The loss affects the present situation"
    },
    {
      "question": "Gap tuzing (never): \"1=I\", \"2=have never\", \"3=tried\", \"4=sushi\"",
      "numbered_options": {
        "1": "I", "2": "have never", "3": "tried", "4": "sushi"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Negative experiences",
      "hint": "'never' goes between auxiliary and main verb"
    },
    {
      "question": "Gap tuzing (duration): \"1=They\", \"2=have lived\", \"3=here\", \"4=since\", \"5=2010\"",
      "numbered_options": {
        "1": "They", "2": "have lived", "3": "here", "4": "since", "5": "2010"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Duration from past to present",
      "hint": "'since' for starting point in the past"
    },
    {
      "question": "Tartiblang (yet): \"1=Have\", \"2=you\", \"3=finished\", \"4=the report\", \"5=yet\"",
      "numbered_options": {
        "1": "Have", "2": "you", "3": "finished", "4": "the report", "5": "yet"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Questions with 'yet'",
      "hint": "'yet' typically comes at the end in questions"
    },
    {
      "question": "Gap tuzing (already): \"1=She\", \"2=has already\", \"3=seen\", \"4=that movie\"",
      "numbered_options": {
        "1": "She", "2": "has already", "3": "seen", "4": "that movie"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "'already' position",
      "hint": "'already' goes between auxiliary and main verb"
    },
    {
      "question": "Tartiblang (recent change): \"1=The prices\", \"2=have\", \"3=gone up\", \"4=significantly\"",
      "numbered_options": {
        "1": "The prices", "2": "have", "3": "gone up", "4": "significantly"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Recent changes",
      "hint": "Present perfect for changes happening recently"
    },
    {
      "question": "Gap tuzing (how long): \"1=How long\", \"2=have\", \"3=you\", \"4=known\", \"5=your best friend\"",
      "numbered_options": {
        "1": "How long", "2": "have", "3": "you", "4": "known", "5": "your best friend"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Duration questions",
      "hint": "'How long' questions often use present perfect"
    },
    {
      "question": "Gap tuzing (passive): \"1=This book\", \"2=has been\", \"3=translated\", \"4=into\", \"5=30 languages\"",
      "numbered_options": {
        "1": "This book", "2": "has been", "3": "translated", "4": "into", "5": "30 languages"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Present perfect passive",
      "hint": "Object + has been + past participle"
    },
    {
      "question": "Tartiblang (emphasis): \"1=I\", \"2=HAVE\", \"3=told\", \"4=you\", \"5=this\", \"6=many times\"",
      "numbered_options": {
        "1": "I", "2": "HAVE", "3": "told", "4": "you", "5": "this", "6": "many times"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Emphatic present perfect",
      "hint": "Capitalized auxiliary shows strong emphasis"
    },
    {
      "question": "Gap tuzing (first time): \"1=This is\", \"2=the first time\", \"3=I\", \"4=have ever\", \"5=flown\", \"6=in a helicopter\"",
      "numbered_options": {
        "1": "This is", "2": "the first time", "3": "I", "4": "have ever", "5": "flown", "6": "in a helicopter"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "'First time' expressions",
      "hint": "Present perfect after 'This is the first time'"
    },
    {
      "question": "Tartiblang (mixed tenses): \"1=Although\", \"2=she\", \"3=has lived\", \"4=here\", \"5=for years\", \"6=she\", \"7=doesn't know\", \"8=the city well\"",
      "numbered_options": {
        "1": "Although", "2": "she", "3": "has lived", "4": "here", "5": "for years", "6": "she", "7": "doesn't know", "8": "the city well"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,5,1,6,7,8"],
      "correct": 0,
      "grammar_point": "Contrast with present perfect",
      "hint": "Present perfect for duration vs. present simple for current state"
    },
    {
      "question": "Gap tuzing (complex): \"1=Not only\", \"2=has\", \"3=he\", \"4=completed\", \"5=the project\", \"6=but he\", \"7=has also\", \"8=exceeded\", \"9=our expectations\"",
      "numbered_options": {
        "1": "Not only", "2": "has", "3": "he", "4": "completed", "5": "the project", "6": "but he", "7": "has also", "8": "exceeded", "9": "our expectations"
      },
      "options": ["1,2,3,4,5,6,7,8,9", "9,8,7,6,5,4,3,2,1", "2,3,4,5,1,6,7,8,9"],
      "correct": 0,
      "grammar_point": "Inversion with present perfect",
      "hint": "Inversion after 'Not only' (auxiliary before subject)"
    }
  ],

  "present_perfect_cont": [
    {
      "question": "Gap tuzing (duration): \"1=I\", \"2=have been working\", \"3=on this\", \"4=project\", \"5=all day\"",
      "numbered_options": {
        "1": "I", "2": "have been working", "3": "on this", "4": "project", "5": "all day"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Duration emphasis",
      "hint": "Subject + have been + verb-ing"
    },
    {
      "question": "Tartiblang (recent activity): \"1=Her eyes\", \"2=are red\", \"3=she\", \"4=has been\", \"5=crying\"",
      "numbered_options": {
        "1": "Her eyes", "2": "are red", "3": "she", "4": "has been", "5": "crying"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "3,4,5,1,2"],
      "correct": 2,
      "grammar_point": "Recent activity evidence",
      "hint": "Present result shows recent continuous activity"
    },
    {
      "question": "Gap tuzing (temporary): \"1=We\", \"2=have been staying\", \"3=at a hotel\", \"4=while\", \"5=our house\", \"6=is being renovated\"",
      "numbered_options": {
        "1": "We", "2": "have been staying", "3": "at a hotel", "4": "while", "5": "our house", "6": "is being renovated"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Temporary situations",
      "hint": "Continuous form for temporary arrangements"
    },
    {
      "question": "Tartiblang (how long): \"1=How long\", \"2=have\", \"3=you\", \"4=been waiting\", \"5=here\"",
      "numbered_options": {
        "1": "How long", "2": "have", "3": "you", "4": "been waiting", "5": "here"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Duration questions",
      "hint": "Present perfect continuous for 'how long' questions"
    },
    {
      "question": "Gap tuzing (recent focus): \"1=The ground\", \"2=is wet\", \"3=it\", \"4=has been\", \"5=raining\"",
      "numbered_options": {
        "1": "The ground", "2": "is wet", "3": "it", "4": "has been", "5": "raining"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "3,4,5,1,2"],
      "correct": 2,
      "grammar_point": "Recent activity evidence",
      "hint": "Present result shows recent continuous action"
    },

    {
      "question": "Gap tuzing (annoyance): \"1=He\", \"2=has been\", \"3=using\", \"4=my computer\", \"5=without\", \"6=asking\"",
      "numbered_options": {
        "1": "He", "2": "has been", "3": "using", "4": "my computer", "5": "without", "6": "asking"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Repeated annoying actions",
      "hint": "Present perfect continuous for repeated irritating actions"
    },
    {
      "question": "Tartiblang (focus on action): \"1=The scientists\", \"2=have been analyzing\", \"3=the data\", \"4=for\", \"5=months\"",
      "numbered_options": {
        "1": "The scientists", "2": "have been analyzing", "3": "the data", "4": "for", "5": "months"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Ongoing activity focus",
      "hint": "Emphasizes the continuous nature of the activity"
    },
    {
      "question": "Gap tuzing (recent completion): \"1=I\", \"2=have been\", \"3=cleaning\", \"4=the house\", \"5=all morning\"",
      "numbered_options": {
        "1": "I", "2": "have been", "3": "cleaning", "4": "the house", "5": "all morning"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Recently stopped activity",
      "hint": "Activity may have just finished or may continue"
    },
    {
      "question": "Tartiblang (temporary habit): \"1=Lately\", \"2=she\", \"3=has been\", \"4=working\", \"5=late\", \"6=every day\"",
      "numbered_options": {
        "1": "Lately", "2": "she", "3": "has been", "4": "working", "5": "late", "6": "every day"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,3,4,5,6,1"],
      "correct": 0,
      "grammar_point": "Temporary habits",
      "hint": "'Lately' indicates recent temporary pattern"
    },
    {
      "question": "Gap tuzing (result focus): \"1=Her hands\", \"2=are dirty\", \"3=because\", \"4=she\", \"5=has been\", \"6=gardening\"",
      "numbered_options": {
        "1": "Her hands", "2": "are dirty", "3": "because", "4": "she", "5": "has been", "6": "gardening"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "4,5,6,3,1,2"],
      "correct": 0,
      "grammar_point": "Visible results",
      "hint": "Present result of a recent continuous action"
    },
    {
      "question": "Gap tuzing (passive): \"1=This theory\", \"2=has been\", \"3=being\", \"4=debated\", \"5=for decades\"",
      "numbered_options": {
        "1": "This theory", "2": "has been", "3": "being", "4": "debated", "5": "for decades"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Present perfect continuous passive",
      "hint": "Object + has been + being + past participle"
    },
    {
      "question": "Tartiblang (mixed tenses): \"1=Although\", \"2=he\", \"3=has been\", \"4=studying\", \"5=English\", \"6=for years\", \"7=he\", \"8=still\", \"9=makes\", \"10=basic mistakes\"",
      "numbered_options": {
        "1": "Although", "2": "he", "3": "has been", "4": "studying", "5": "English", "6": "for years", "7": "he", "8": "still", "9": "makes", "10": "basic mistakes"
      },
      "options": ["1,2,3,4,5,6,7,8,9,10", "10,9,8,7,6,5,4,3,2,1", "2,3,4,5,6,1,7,8,9,10"],
      "correct": 0,
      "grammar_point": "Contrast with present simple",
      "hint": "Continuous duration vs. present state/ability"
    },
    {
      "question": "Gap tuzing (emphasis): \"1=I\", \"2=HAVE been\", \"3=trying\", \"4=to call\", \"5=you\", \"6=all day\"",
      "numbered_options": {
        "1": "I", "2": "HAVE been", "3": "trying", "4": "to call", "5": "you", "6": "all day"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Emphatic form",
      "hint": "Capitalized auxiliary shows frustration/emphasis"
    },
    {
      "question": "Tartiblang (complex duration): \"1=Ever since\", \"2=she\", \"3=got\", \"4=promoted\", \"5=she\", \"6=has been\", \"7=working\", \"8=longer hours\"",
      "numbered_options": {
        "1": "Ever since", "2": "she", "3": "got", "4": "promoted", "5": "she", "6": "has been", "7": "working", "8": "longer hours"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,1,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Duration from past point",
      "hint": "'Ever since' marks the starting point"
    },
    {
      "question": "Gap tuzing (interrupted): \"1=We\", \"2=have been\", \"3=discussing\", \"4=the contract\", \"5=but\", \"6=we\", \"7=haven't\", \"8=reached\", \"9=an agreement\", \"10=yet\"",
      "numbered_options": {
        "1": "We", "2": "have been", "3": "discussing", "4": "the contract", "5": "but", "6": "we", "7": "haven't", "8": "reached", "9": "an agreement", "10": "yet"
      },
      "options": ["1,2,3,4,5,6,7,8,9,10", "10,9,8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8,9,10"],
      "correct": 0,
      "grammar_point": "Interrupted activity",
      "hint": "Continuous action that hasn't achieved its goal yet"
    }
  ],

  "past_simple": [
    {
      "question": "Gap tuzing (regular): \"1=She\", \"2=worked\", \"3=in London\", \"4=last year\"",
      "numbered_options": {
        "1": "She", "2": "worked", "3": "in London", "4": "last year"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Completed actions",
      "hint": "Subject + past simple verb"
    },
    {
      "question": "Tartiblang (irregular): \"1=They\", \"2=went\", \"3=to Paris\", \"4=on holiday\"",
      "numbered_options": {
        "1": "They", "2": "went", "3": "to Paris", "4": "on holiday"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Past events",
      "hint": "Irregular past form of 'go'"
    },
    {
      "question": "Gap tuzing (negative): \"1=I\", \"2=did not\", \"3=see\", \"4=him\", \"5=yesterday\"",
      "numbered_options": {
        "1": "I", "2": "did not", "3": "see", "4": "him", "5": "yesterday"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Negative form",
      "hint": "Did + not + base verb"
    },
    {
      "question": "Tartiblang (question): \"1=Did\", \"2=you\", \"3=watch\", \"4=the news\", \"5=last night\"",
      "numbered_options": {
        "1": "Did", "2": "you", "3": "watch", "4": "the news", "5": "last night"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Yes/no questions",
      "hint": "Did + subject + base verb"
    },
    {
      "question": "Gap tuzing (time marker): \"1=We\", \"2=met\", \"3=in 2010\", \"4=at university\"",
      "numbered_options": {
        "1": "We", "2": "met", "3": "in 2010", "4": "at university"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Specific past time",
      "hint": "Past simple with definite time marker"
    },
    {
      "question": "Gap tuzing (sequence): \"1=First\", \"2=she\", \"3=finished\", \"4=her degree\", \"5=then\", \"6=she\", \"7=got\", \"8=a job\"",
      "numbered_options": {
        "1": "First", "2": "she", "3": "finished", "4": "her degree", "5": "then", "6": "she", "7": "got", "8": "a job"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,1,6,7,8,5"],
      "correct": 0,
      "grammar_point": "Sequenced actions",
      "hint": "Past simple for consecutive completed actions"
    },
    {
      "question": "Tartiblang (WH question): \"1=Why\", \"2=did\", \"3=you\", \"4=leave\", \"5=early\", \"6=yesterday\"",
      "numbered_options": {
        "1": "Why", "2": "did", "3": "you", "4": "leave", "5": "early", "6": "yesterday"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,3,4,5,6,1"],
      "correct": 0,
      "grammar_point": "WH questions",
      "hint": "WH word + did + subject + base verb"
    },
    {
      "question": "Gap tuzing (habit): \"1=When\", \"2=I\", \"3=was\", \"4=young\", \"5=I\", \"6=played\", \"7=tennis\", \"8=every weekend\"",
      "numbered_options": {
        "1": "When", "2": "I", "3": "was", "4": "young", "5": "I", "6": "played", "7": "tennis", "8": "every weekend"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,1,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Past habits",
      "hint": "Past simple for habits that no longer continue"
    },
    {
      "question": "Tartiblang (storytelling): \"1=Suddenly\", \"2=the lights\", \"3=went\", \"4=out\", \"5=and\", \"6=we\", \"7=heard\", \"8=a strange noise\"",
      "numbered_options": {
        "1": "Suddenly", "2": "the lights", "3": "went", "4": "out", "5": "and", "6": "we", "7": "heard", "8": "a strange noise"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,1,6,7,8,5"],
      "correct": 0,
      "grammar_point": "Narrative past",
      "hint": "Past simple for events in a story"
    },
    {
      "question": "Gap tuzing (state): \"1=They\", \"2=lived\", \"3=in Rome\", \"4=for\", \"5=ten years\", \"6=before moving\"",
      "numbered_options": {
        "1": "They", "2": "lived", "3": "in Rome", "4": "for", "5": "ten years", "6": "before moving"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Past states",
      "hint": "Past simple for situations that lasted in the past"
    },
    {
      "question": "Gap tuzing (passive): \"1=The letter\", \"2=was\", \"3=sent\", \"4=last week\"",
      "numbered_options": {
        "1": "The letter", "2": "was", "3": "sent", "4": "last week"
      },
      "options": ["1,2,3,4", "4,3,2,1", "2,1,3,4"],
      "correct": 0,
      "grammar_point": "Past passive",
      "hint": "Object + was/were + past participle"
    },
    {
      "question": "Tartiblang (unreal present): \"1=I\", \"2=wish\", \"3=I\", \"4=knew\", \"5=the answer\"",
      "numbered_options": {
        "1": "I", "2": "wish", "3": "I", "4": "knew", "5": "the answer"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Unreal present",
      "hint": "Past simple after 'wish' for present meaning"
    },
    {
      "question": "Gap tuzing (second conditional): \"1=If\", \"2=you\", \"3=studied\", \"4=more\", \"5=you\", \"6=would pass\", \"7=the exam\"",
      "numbered_options": {
        "1": "If", "2": "you", "3": "studied", "4": "more", "5": "you", "6": "would pass", "7": "the exam"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,3,4,1,5,6,7"],
      "correct": 0,
      "grammar_point": "Second conditional",
      "hint": "If + past simple, would + base verb"
    },
    {
      "question": "Tartiblang (time clause): \"1=After\", \"2=she\", \"3=graduated\", \"4=she\", \"5=traveled\", \"6=around Asia\", \"7=for a year\"",
      "numbered_options": {
        "1": "After", "2": "she", "3": "graduated", "4": "she", "5": "traveled", "6": "around Asia", "7": "for a year"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,3,1,4,5,6,7"],
      "correct": 0,
      "grammar_point": "Time clauses",
      "hint": "After + past simple, past simple"
    },
    {
      "question": "Gap tuzing (indirect speech): \"1=She\", \"2=said\", \"3=that\", \"4=she\", \"5=loved\", \"6=the concert\"",
      "numbered_options": {
        "1": "She", "2": "said", "3": "that", "4": "she", "5": "loved", "6": "the concert"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Reported speech",
      "hint": "Past simple often used in reported speech"
    }
  ],
  "past_continuous": [
    {
      "question": "Gap tuzing (ongoing action): \"1=At 8 PM\", \"2=yesterday\", \"3=I\", \"4=was watching\", \"5=TV\"",
      "numbered_options": {
        "1": "At 8 PM", "2": "yesterday", "3": "I", "4": "was watching", "5": "TV"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "3,4,5,1,2"],
      "correct": 0,
      "grammar_point": "Specific time interruption",
      "hint": "Was/were + verb-ing for ongoing past actions"
    },
    {
      "question": "Tartiblang (parallel actions): \"1=While\", \"2=I\", \"3=was cooking\", \"4=my husband\", \"5=was setting\", \"6=the table\"",
      "numbered_options": {
        "1": "While", "2": "I", "3": "was cooking", "4": "my husband", "5": "was setting", "6": "the table"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,3,1,4,5,6"],
      "correct": 0,
      "grammar_point": "Simultaneous actions",
      "hint": "Two ongoing actions connected with 'while'"
    },
    {
      "question": "Gap tuzing (interrupted action): \"1=When\", \"2=you\", \"3=called\", \"4=I\", \"5=was taking\", \"6=a shower\"",
      "numbered_options": {
        "1": "When", "2": "you", "3": "called", "4": "I", "5": "was taking", "6": "a shower"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "4,5,6,1,2,3"],
      "correct": 0,
      "grammar_point": "Interrupted actions",
      "hint": "Past simple interrupts past continuous"
    },
    {
      "question": "Tartiblang (background description): \"1=The sun\", \"2=was shining\", \"3=and\", \"4=the birds\", \"5=were singing\"",
      "numbered_options": {
        "1": "The sun", "2": "was shining", "3": "and", "4": "the birds", "5": "were singing"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,5,4"],
      "correct": 0,
      "grammar_point": "Scene setting",
      "hint": "Past continuous for background description"
    },
    {
      "question": "Gap tuzing (temporary situation): \"1=In 2010\", \"2=I\", \"3=was living\", \"4=in\", \"5=Madrid\"",
      "numbered_options": {
        "1": "In 2010", "2": "I", "3": "was living", "4": "in", "5": "Madrid"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,3,4,5,1"],
      "correct": 0,
      "grammar_point": "Temporary past situations",
      "hint": "Past continuous for temporary living situations"
    },
    {
      "question": "Gap tuzing (polite inquiry): \"1=I\", \"2=was wondering\", \"3=if\", \"4=you\", \"5=could\", \"6=help me\"",
      "numbered_options": {
        "1": "I", "2": "was wondering", "3": "if", "4": "you", "5": "could", "6": "help me"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Polite questions",
      "hint": "Past continuous makes requests more polite"
    },
    {
      "question": "Tartiblang (irritation): \"1=He\", \"2=was always\", \"3=complaining\", \"4=about\", \"5=his job\"",
      "numbered_options": {
        "1": "He", "2": "was always", "3": "complaining", "4": "about", "5": "his job"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "grammar_point": "Repeated annoying actions",
      "hint": "Always + past continuous shows irritation"
    },
    {
      "question": "Gap tuzing (changing states): \"1=It\", \"2=was getting\", \"3=darker\", \"4=so\", \"5=we\", \"6=decided\", \"7=to leave\"",
      "numbered_options": {
        "1": "It", "2": "was getting", "3": "darker", "4": "so", "5": "we", "6": "decided", "7": "to leave"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,1,3,4,5,6,7"],
      "correct": 0,
      "grammar_point": "Changing situations",
      "hint": "Past continuous for gradual changes"
    },
    {
      "question": "Tartiblang (passive): \"1=The documents\", \"2=were being\", \"3=prepared\", \"4=when\", \"5=the power\", \"6=went out\"",
      "numbered_options": {
        "1": "The documents", "2": "were being", "3": "prepared", "4": "when", "5": "the power", "6": "went out"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Past continuous passive",
      "hint": "Was/were being + past participle"
    },
    {
      "question": "Gap tuzing (emphatic): \"1=I\", \"2=WAS\", \"3=NOT\", \"4=sleeping\", \"5=during\", \"6=the lecture\"",
      "numbered_options": {
        "1": "I", "2": "WAS", "3": "NOT", "4": "sleeping", "5": "during", "6": "the lecture"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Emphatic negation",
      "hint": "Capitalized auxiliary shows strong denial"
    },
    {
      "question": "Gap tuzing (mixed tenses): \"1=While\", \"2=we\", \"3=were discussing\", \"4=the budget\", \"5=the director\", \"6=interrupted\", \"7=us\", \"8=with urgent news\"",
      "numbered_options": {
        "1": "While", "2": "we", "3": "were discussing", "4": "the budget", "5": "the director", "6": "interrupted", "7": "us", "8": "with urgent news"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,1,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Background interruption",
      "hint": "Long background action interrupted by sudden event"
    },
    {
      "question": "Tartiblang (narrative): \"1=As\", \"2=the crowd\", \"3=was cheering\", \"4=the runner\", \"5=was approaching\", \"6=the finish line\", \"7=when\", \"8=he\", \"9=tripped\"",
      "numbered_options": {
        "1": "As", "2": "the crowd", "3": "was cheering", "4": "the runner", "5": "was approaching", "6": "the finish line", "7": "when", "8": "he", "9": "tripped"
      },
      "options": ["1,2,3,4,5,6,7,8,9", "9,8,7,6,5,4,3,2,1", "2,3,1,4,5,6,7,8,9"],
      "correct": 0,
      "grammar_point": "Complex narrative",
      "hint": "Two parallel actions building tension"
    },
    {
      "question": "Gap tuzing (speculation): \"1=He\", \"2=must have been\", \"3=joking\", \"4=when\", \"5=he\", \"6=said\", \"7=that\"",
      "numbered_options": {
        "1": "He", "2": "must have been", "3": "joking", "4": "when", "5": "he", "6": "said", "7": "that"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,1,3,4,5,6,7"],
      "correct": 0,
      "grammar_point": "Past deduction",
      "hint": "Must + have been + verb-ing for past speculation"
    },
    {
      "question": "Tartiblang (time clause): \"1=Just as\", \"2=I\", \"3=was leaving\", \"4=the house\", \"5=the phone\", \"6=rang\"",
      "numbered_options": {
        "1": "Just as", "2": "I", "3": "was leaving", "4": "the house", "5": "the phone", "6": "rang"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,3,4,1,5,6"],
      "correct": 0,
      "grammar_point": "Precise interruption",
      "hint": "'Just as' emphasizes exact moment of interruption"
    },
    {
      "question": "Gap tuzing (contrast): \"1=Whereas\", \"2=most students\", \"3=were studying\", \"4=for exams\", \"5=he\", \"6=was spending\", \"7=all his time\", \"8=playing games\"",
      "numbered_options": {
        "1": "Whereas", "2": "most students", "3": "were studying", "4": "for exams", "5": "he", "6": "was spending", "7": "all his time", "8": "playing games"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,1,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Contrasting actions",
      "hint": "Parallel actions showing contrast with 'whereas'"
    }
  ],

 "past_perfect": [
    {
      "question": "Gap tuzing (sequence): \"1=When\", \"2=we\", \"3=arrived\", \"4=the movie\", \"5=had already\", \"6=started\"",
      "numbered_options": {
        "1": "When", "2": "we", "3": "arrived", "4": "the movie", "5": "had already", "6": "started"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "4,5,6,1,2,3"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Past-before-past",
      "hint": "Had + past participle for earlier past action"
    },
    {
      "question": "Tartiblang (regret): \"1=I\", \"2=wish\", \"3=I\", \"4=had studied\", \"5=harder\"",
      "numbered_options": {
        "1": "I", "2": "wish", "3": "I", "4": "had studied", "5": "harder"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Unreal past",
      "hint": "Wish + had + past participle for regrets"
    },
    {
      "question": "Gap tuzing (cause-effect): \"1=She\", \"2=was tired\", \"3=because\", \"4=she\", \"5=hadn't slept\", \"6=well\"",
      "numbered_options": {
        "1": "She", "2": "was tired", "3": "because", "4": "she", "5": "hadn't slept", "6": "well"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "4,5,6,3,1,2"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Past reasons",
      "hint": "Past perfect explains cause of past state"
    },
    {
      "question": "Tartiblang (reported speech): \"1=He\", \"2=said\", \"3=that\", \"4=he\", \"5=had never\", \"6=seen\", \"7=such\", \"8=a beautiful sunset\"",
      "numbered_options": {
        "1": "He", "2": "said", "3": "that", "4": "he", "5": "had never", "6": "seen", "7": "such", "8": "a beautiful sunset"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Reported speech",
      "hint": "Present perfect becomes past perfect in reports"
    },
    {
      "question": "Gap tuzing (time expression): \"1=By\", \"2=the time\", \"3=we\", \"4=got there\", \"5=they\", \"6=had left\"",
      "numbered_options": {
        "1": "By", "2": "the time", "3": "we", "4": "got there", "5": "they", "6": "had left"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "5,6,1,2,3,4"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Completion before past point",
      "hint": "'By the time' often used with past perfect"
    },
    {
      "question": "Gap tuzing (third conditional): \"1=If\", \"2=you\", \"3=had told\", \"4=me earlier\", \"5=I\", \"6=would have\", \"7=helped\"",
      "numbered_options": {
        "1": "If", "2": "you", "3": "had told", "4": "me earlier", "5": "I", "6": "would have", "7": "helped"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,3,4,1,5,6,7"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Third conditional",
      "hint": "If + past perfect, would have + past participle"
    },
    {
      "question": "Tartiblang (double past): \"1=After\", \"2=she\", \"3=had finished\", \"4=her work\", \"5=she\", \"6=went\", \"7=for a walk\"",
      "numbered_options": {
        "1": "After", "2": "she", "3": "had finished", "4": "her work", "5": "she", "6": "went", "7": "for a walk"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,3,4,1,5,6,7"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Sequence of past events",
      "hint": "'After' makes the sequence clear"
    },
    {
      "question": "Gap tuzing (passive): \"1=The documents\", \"2=had been\", \"3=signed\", \"4=before\", \"5=the meeting\", \"6=started\"",
      "numbered_options": {
        "1": "The documents", "2": "had been", "3": "signed", "4": "before", "5": "the meeting", "6": "started"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Past perfect passive",
      "hint": "Had been + past participle"
    },
    {
      "question": "Tartiblang (unreal past): \"1=If only\", \"2=I\", \"3=had known\", \"4=the truth\", \"5=earlier\"",
      "numbered_options": {
        "1": "If only", "2": "I", "3": "had known", "4": "the truth", "5": "earlier"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,3,4,5,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Regrets",
      "hint": "'If only' expresses strong regret about past"
    },
    {
      "question": "Gap tuzing (negative): \"1=They\", \"2=hadn't\", \"3=met\", \"4=before\", \"5=the party\"",
      "numbered_options": {
        "1": "They", "2": "hadn't", "3": "met", "4": "before", "5": "the party"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Negative past perfect",
      "hint": "Had not + past participle"
    },
    {
      "question": "Gap tuzing (mixed tenses): \"1=By\", \"2=the time\", \"3=he\", \"4=realized\", \"5=his mistake\", \"6=the damage\", \"7=had already\", \"8=been done\"",
      "numbered_options": {
        "1": "By", "2": "the time", "3": "he", "4": "realized", "5": "his mistake", "6": "the damage", "7": "had already", "8": "been done"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Complex sequencing",
      "hint": "Past simple and past perfect passive combination"
    },
    {
      "question": "Tartiblang (inversion): \"1=Hardly\", \"2=had\", \"3=we\", \"4=left\", \"5=the house\", \"6=when\", \"7=the phone\", \"8=rang\"",
      "numbered_options": {
        "1": "Hardly", "2": "had", "3": "we", "4": "left", "5": "the house", "6": "when", "7": "the phone", "8": "rang"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,5,1,6,7,8"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Inversion with adverbs",
      "hint": "Hardly had subject past participle"
    },
    {
      "question": "Gap tuzing (speculation): \"1=She\", \"2=must have\", \"3=forgotten\", \"4=about\", \"5=the meeting\", \"6=because\", \"7=she\", \"8=hadn't mentioned\", \"9=it all day\"",
      "numbered_options": {
        "1": "She", "2": "must have", "3": "forgotten", "4": "about", "5": "the meeting", "6": "because", "7": "she", "8": "hadn't mentioned", "9": "it all day"
      },
      "options": ["1,2,3,4,5,6,7,8,9", "9,8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8,9"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Past deduction",
      "hint": "Must have + past participle for logical conclusions"
    },
    {
      "question": "Tartiblang (literary): \"1=Scarcely\", \"2=had\", \"3=the ceremony\", \"4=ended\", \"5=when\", \"6=the protests\", \"7=began\"",
      "numbered_options": {
        "1": "Scarcely", "2": "had", "3": "the ceremony", "4": "ended", "5": "when", "6": "the protests", "7": "began"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "2,3,4,1,5,6,7"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Literary inversion",
      "hint": "Scarcely + had + subject + past participle"
    },
    {
      "question": "Gap tuzing (time clauses): \"1=No sooner\", \"2=had\", \"3=the judge\", \"4=pronounced\", \"5=the sentence\", \"6=than\", \"7=the defendant\", \"8=appealed\"",
      "numbered_options": {
        "1": "No sooner", "2": "had", "3": "the judge", "4": "pronounced", "5": "the sentence", "6": "than", "7": "the defendant", "8": "appealed"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,3,4,5,1,6,7,8"],
      "correct": 0,
      "level": "hard",
      "grammar_point": "Fixed expressions",
      "hint": "No sooner + had + subject + past participle + than"
    }
  ],

  "past_perfect_cont": [
    {
      "question": "Gap tuzing (duration): \"1=Her eyes\", \"2=were red\", \"3=because\", \"4=she\", \"5=had been\", \"6=crying\"",
      "numbered_options": {
        "1": "Her eyes", "2": "were red", "3": "because", "4": "she", "5": "had been", "6": "crying"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "4,5,6,3,1,2"],
      "correct": 0,
      "grammar_point": "Past cause-effect",
      "hint": "Had been + verb-ing for ongoing past actions"
    },
    {
      "question": "Tartiblang (long action): \"1=They\", \"2=had been\", \"3=working\", \"4=on\", \"5=the project\", \"6=for months\"",
      "numbered_options": {
        "1": "They", "2": "had been", "3": "working", "4": "on", "5": "the project", "6": "for months"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Duration before past",
      "hint": "Emphasizes duration before another past event"
    },
    {
      "question": "Gap tuzing (tiredness): \"1=I\", \"2=was exhausted\", \"3=because\", \"4=I\", \"5=had been\", \"6=running\"",
      "numbered_options": {
        "1": "I", "2": "was exhausted", "3": "because", "4": "I", "5": "had been", "6": "running"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "4,5,6,3,1,2"],
      "correct": 0,
      "grammar_point": "Result of past action",
      "hint": "Continuous action led to past state"
    },
    {
      "question": "Tartiblang (recent activity): \"1=The ground\", \"2=was wet\", \"3=it\", \"4=had been\", \"5=raining\"",
      "numbered_options": {
        "1": "The ground", "2": "was wet", "3": "it", "4": "had been", "5": "raining"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "3,4,5,1,2"],
      "correct": 2,
      "grammar_point": "Recent past evidence",
      "hint": "Visible result of recent continuous action"
    },
    {
      "question": "Gap tuzing (interrupted): \"1=She\", \"2=had been\", \"3=reading\", \"4=when\", \"5=the phone\", \"6=rang\"",
      "numbered_options": {
        "1": "She", "2": "had been", "3": "reading", "4": "when", "5": "the phone", "6": "rang"
      },
      "options": ["1,2,3,4,5,6", "6,5,4,3,2,1", "2,1,3,4,5,6"],
      "correct": 0,
      "grammar_point": "Interrupted action",
      "hint": "Long action interrupted by shorter one"
    },
    {
      "question": "Gap tuzing (passive): \"1=The car\", \"2=had been\", \"3=being\", \"4=repaired\", \"5=for hours\", \"6=before\", \"7=it\", \"8=was ready\"",
      "numbered_options": {
        "1": "The car", "2": "had been", "3": "being", "4": "repaired", "5": "for hours", "6": "before", "7": "it", "8": "was ready"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Past perfect continuous passive",
      "hint": "Had been being + past participle (rare)"
    },
    {
      "question": "Tartiblang (emphasis): \"1=He\", \"2=HAD been\", \"3=working\", \"4=there\", \"5=for decades\", \"6=before\", \"7=they\", \"8=fired him\"",
      "numbered_options": {
        "1": "He", "2": "HAD been", "3": "working", "4": "there", "5": "for decades", "6": "before", "7": "they", "8": "fired him"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Emphatic duration",
      "hint": "Capitalized auxiliary emphasizes unfairness"
    },
    {
      "question": "Gap tuzing (mixed tenses): \"1=Although\", \"2=she\", \"3=had been\", \"4=studying\", \"5=English\", \"6=for years\", \"7=she\", \"8=still\", \"9=struggled\", \"10=with pronunciation\"",
      "numbered_options": {
        "1": "Although", "2": "she", "3": "had been", "4": "studying", "5": "English", "6": "for years", "7": "she", "8": "still", "9": "struggled", "10": "with pronunciation"
      },
      "options": ["1,2,3,4,5,6,7,8,9,10", "10,9,8,7,6,5,4,3,2,1", "2,3,4,5,6,1,7,8,9,10"],
      "correct": 0,
      "grammar_point": "Unexpected result",
      "hint": "Long preparation didn't lead to expected outcome"
    },
    {
      "question": "Tartiblang (negative): \"1=They\", \"2=hadn't been\", \"3=living\", \"4=there\", \"5=long\", \"6=when\", \"7=the problems\", \"8=started\"",
      "numbered_options": {
        "1": "They", "2": "hadn't been", "3": "living", "4": "there", "5": "long", "6": "when", "7": "the problems", "8": "started"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "2,1,3,4,5,6,7,8"],
      "correct": 0,
      "grammar_point": "Negative duration",
      "hint": "Had not been + verb-ing for lack of duration"
    },
    {
      "question": "Gap tuzing (temporary): \"1=Before\", \"2=moving\", \"3=to Paris\", \"4=we\", \"5=had been\", \"6=renting\", \"7=an apartment\", \"8=in Lyon\"",
      "numbered_options": {
        "1": "Before", "2": "moving", "3": "to Paris", "4": "we", "5": "had been", "6": "renting", "7": "an apartment", "8": "in Lyon"
      },
      "options": ["1,2,3,4,5,6,7,8", "8,7,6,5,4,3,2,1", "4,5,6,7,8,1,2,3"],
      "correct": 0,
      "grammar_point": "Temporary past situations",
      "hint": "Temporary living situation before main past event"
    },
    {
      "question": "Gap tuzing (speculation): \"1=His hands\", \"2=were dirty\", \"3=he\", \"4=must have been\", \"5=working\", \"6=in\", \"7=the garden\"",
      "numbered_options": {
        "1": "His hands", "2": "were dirty", "3": "he", "4": "must have been", "5": "working", "6": "in", "7": "the garden"
      },
      "options": ["1,2,3,4,5,6,7", "7,6,5,4,3,2,1", "3,4,5,6,7,1,2"],
      "correct": 0,
      "grammar_point": "Past deduction",
      "hint": "Must have been + verb-ing for ongoing past deduction"
    },
    {
      "question": "Tartiblang (literary): \"1=For\", \"2=how many years\", \"3=had\", \"4=the ancient tree\", \"5=been\", \"6=growing\", \"7=there\", \"8=before\", \"9=the storm\", \"10=felled it\"",
      "numbered_options": {
        "1": "For", "2": "how many years", "3": "had", "4": "the ancient tree", "5": "been", "6": "growing", "7": "there", "8": "before", "9": "the storm", "10": "felled it"
      },
      "options": ["1,2,3,4,5,6,7,8,9,10", "10,9,8,7,6,5,4,3,2,1", "3,4,5,6,7,1,2,8,9,10"],
      "correct": 0,
      "grammar_point": "Literary duration",
      "hint": "Emphasizes long duration before dramatic event"
    },
  ],
  "future_simple_tests" : [
    {
        "question": "So'zlarni tartiblang: \"1=They\", \"2=will\", \"3=arrive\", \"4=tomorrow\"",
        "numbered_options": {
            "1": "They",
            "2": "will",
            "3": "arrive",
            "4": "tomorrow"
        },
        "options": [
            "1,2,3,4",
            "4,1,2,3",
            "1,3,2,4"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=I\", \"2=will\", \"3=call\", \"4=you\", \"5=later\"",
        "numbered_options": {
            "1": "I",
            "2": "will",
            "3": "call",
            "4": "you",
            "5": "later"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=She\", \"2=will\", \"3=not\", \"4=attend\", \"5=the meeting\"",
        "numbered_options": {
            "1": "She",
            "2": "will",
            "3": "not",
            "4": "attend",
            "5": "the meeting"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=Will\", \"2=you\", \"3=help\", \"4=me\", \"5=with this task?\"",
        "numbered_options": {
            "1": "Will",
            "2": "you",
            "3": "help",
            "4": "me",
            "5": "with this task?"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "2,1,3,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=By next year\", \"2=they\", \"3=will\", \"4=have\", \"5=a new house\"",
        "numbered_options": {
            "1": "By next year",
            "2": "they",
            "3": "will",
            "4": "have",
            "5": "a new house"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "medium",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=He\", \"2=will\", \"3=probably\", \"4=be\", \"5=late\"",
        "numbered_options": {
            "1": "He",
            "2": "will",
            "3": "probably",
            "4": "be",
            "5": "late"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "medium",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=I\", \"2=think\", \"3=it\", \"4=will\", \"5=rain\", \"6=tomorrow\"",
        "numbered_options": {
            "1": "I",
            "2": "think",
            "3": "it",
            "4": "will",
            "5": "rain",
            "6": "tomorrow"
        },
        "options": [
            "1,2,3,4,5,6",
            "6,1,2,3,4,5",
            "1,3,2,4,5,6"
        ],
        "correct": 0,
        "level": "medium",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=She\", \"2=will\", \"3=be\", \"4=20\", \"5=next month\"",
        "numbered_options": {
            "1": "She",
            "2": "will",
            "3": "be",
            "4": "20",
            "5": "next month"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
     {
        "question": "So'zlarni tartiblang: \"1=They\", \"2=will\", \"3=arrive\", \"4=tomorrow\"",
        "numbered_options": {
            "1": "They",
            "2": "will",
            "3": "arrive",
            "4": "tomorrow"
        },
        "options": [
            "1,2,3,4",
            "4,1,2,3",
            "1,3,2,4"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=I\", \"2=will\", \"3=call\", \"4=you\", \"5=later\"",
        "numbered_options": {
            "1": "I",
            "2": "will",
            "3": "call",
            "4": "you",
            "5": "later"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=She\", \"2=will\", \"3=not\", \"4=attend\", \"5=the meeting\"",
        "numbered_options": {
            "1": "She",
            "2": "will",
            "3": "not",
            "4": "attend",
            "5": "the meeting"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=Will\", \"2=you\", \"3=help\", \"4=me\", \"5=with this task?\"",
        "numbered_options": {
            "1": "Will",
            "2": "you",
            "3": "help",
            "4": "me",
            "5": "with this task?"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "2,1,3,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=By next year\", \"2=they\", \"3=will\", \"4=have\", \"5=a new house\"",
        "numbered_options": {
            "1": "By next year",
            "2": "they",
            "3": "will",
            "4": "have",
            "5": "a new house"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "medium",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=He\", \"2=will\", \"3=probably\", \"4=be\", \"5=late\"",
        "numbered_options": {
            "1": "He",
            "2": "will",
            "3": "probably",
            "4": "be",
            "5": "late"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "medium",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=I\", \"2=think\", \"3=it\", \"4=will\", \"5=rain\", \"6=tomorrow\"",
        "numbered_options": {
            "1": "I",
            "2": "think",
            "3": "it",
            "4": "will",
            "5": "rain",
            "6": "tomorrow"
        },
        "options": [
            "1,2,3,4,5,6",
            "6,1,2,3,4,5",
            "1,3,2,4,5,6"
        ],
        "correct": 0,
        "level": "medium",
        "grammar_point": "future_simple"
    },
    {
        "question": "So'zlarni tartiblang: \"1=She\", \"2=will\", \"3=be\", \"4=20\", \"5=next month\"",
        "numbered_options": {
            "1": "She",
            "2": "will",
            "3": "be",
            "4": "20",
            "5": "next month"
        },
        "options": [
            "1,2,3,4,5",
            "5,1,2,3,4",
            "1,3,2,4,5"
        ],
        "correct": 0,
        "level": "easy",
        "grammar_point": "future_simple"
    },
      {
    "question": "So'zlarni tartiblang: \"1=They\", \"2=will\", \"3=arrive\", \"4=tomorrow\"",
    "numbered_options": {
      "1": "They",
      "2": "will",
      "3": "arrive",
      "4": "tomorrow"
    },
    "options": [
      "1,2,3,4",
      "4,1,2,3",
      "1,3,2,4"
    ],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_simple"
  },
  {
    "question": "So'zlarni tartiblang: \"1=I\", \"2=will\", \"3=call\", \"4=you\", \"5=later\"",
    "numbered_options": {
      "1": "I",
      "2": "will",
      "3": "call",
      "4": "you",
      "5": "later"
    },
    "options": [
      "1,2,3,4,5",
      "5,1,2,3,4",
      "1,3,2,4,5"
    ],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_simple"
  }
],
"future_continuous": [
    {
      "question": "Tartiblang: \"1=This time\", \"2=tomorrow\", \"3=I\", \"4=will be\", \"5=driving\", \"6=to work\"",
      "numbered_options": {
        "1": "This time",
        "2": "tomorrow",
        "3": "I",
        "4": "will be",
        "5": "driving",
        "6": "to work"
      },
      "options": ["1,2,3,4,5,6", "3,4,5,6,1,2", "1,3,4,2,5,6"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous",
      "hint": "Future continuous: will be + V-ing"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=will be\", \"3=having\", \"4=dinner\", \"5=at 8 PM\"",
      "numbered_options": {
        "1": "We",
        "2": "will be",
        "3": "having",
        "4": "dinner",
        "5": "at 8 PM"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Scheduled future action",
      "hint": "Use future continuous for actions in progress at a specific time"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will be\", \"3=waiting\", \"4=for us\", \"5=when we arrive\"",
      "numbered_options": {
        "1": "They",
        "2": "will be",
        "3": "waiting",
        "4": "for us",
        "5": "when we arrive"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "5,1,2,3,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "Future ongoing",
      "hint": "Describe what will be happening at a moment in future"
    },
    {
      "question": "Tartiblang: \"1=At this time\", \"2=next year\", \"3=he\", \"4=will be\", \"5=living\", \"6=in Canada\"",
      "numbered_options": {
        "1": "At this time",
        "2": "next year",
        "3": "he",
        "4": "will be",
        "5": "living",
        "6": "in Canada"
      },
      "options": ["1,2,3,4,5,6", "3,4,5,6,1,2", "1,3,4,2,5,6"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Future progress",
      "hint": "Will be + verb-ing for future events in progress"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=won't be\", \"3=attending\", \"4=the meeting\", \"5=tomorrow\"",
      "numbered_options": {
        "1": "I",
        "2": "won't be",
        "3": "attending",
        "4": "the meeting",
        "5": "tomorrow"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "1,3,2,4,5"],
      "correct": 0,
      "level": "normal",
      "grammar_point": "Negative future continuous",
      "hint": "Won’t be + verb-ing = negative future continuous"
    },
 {
      "question": "Tartiblang: \"1=She\", \"2=will be\", \"3=studying\", \"4=at\", \"5=7 PM\"",
      "numbered_options": {
        "1": "She",
        "2": "will be",
        "3": "studying",
        "4": "at",
        "5": "7 PM"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous",
      "hint": "Will be + verb-ing for action in progress in future"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will\", \"3=be\", \"4=traveling\", \"5=to Italy\"",
      "numbered_options": {
        "1": "They",
        "2": "will",
        "3": "be",
        "4": "traveling",
        "5": "to Italy"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "5,4,3,2,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous",
      "hint": "Future Continuous = will be + V-ing"
    },
    {
      "question": "Gap tuzing: \"1=I\", \"2=will be\", \"3=waiting\", \"4=for you\", \"5=outside the station\"",
      "numbered_options": {
        "1": "I",
        "2": "will be",
        "3": "waiting",
        "4": "for you",
        "5": "outside the station"
      },
      "options": ["1,2,3,4,5", "4,3,2,1,5", "1,3,2,5,4"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Use 'will be' + V-ing for action at a future time"
    },
    {
      "question": "Tartiblang: \"1=At this time tomorrow\", \"2=he\", \"3=will be\", \"4=driving\", \"5=to the airport\"",
      "numbered_options": {
        "1": "At this time tomorrow",
        "2": "he",
        "3": "will be",
        "4": "driving",
        "5": "to the airport"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,3,4,5,1"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "An action in progress at a specific time in the future"
    },
    {
      "question": "Gap tuzing: \"1=We\", \"2=won't\", \"3=be\", \"4=attending\", \"5=the meeting\"",
      "numbered_options": {
        "1": "We",
        "2": "won't",
        "3": "be",
        "4": "attending",
        "5": "the meeting"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous_negative",
      "hint": "Negative: won't be + verb-ing"
    },
    {
      "question": "Tartiblang: \"1=Will\", \"2=you\", \"3=be\", \"4=working\", \"5=late tonight?\"",
      "numbered_options": {
        "1": "Will",
        "2": "you",
        "3": "be",
        "4": "working",
        "5": "late tonight?"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "5,4,3,2,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous_question",
      "hint": "Future Continuous Question = Will + subject + be + V-ing?"
    },
    {
      "question": "Tartiblang: \"1=By 9 PM\", \"2=they\", \"3=will be\", \"4=watching\", \"5=a movie\"",
      "numbered_options": {
        "1": "By 9 PM",
        "2": "they",
        "3": "will be",
        "4": "watching",
        "5": "a movie"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,3,4,5,1"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Future time expression often begins the sentence"
    },
    {
      "question": "Gap tuzing: \"1=I\", \"2=will\", \"3=not\", \"4=be\", \"5=using\", \"6=the computer\"",
      "numbered_options": {
        "1": "I",
        "2": "will",
        "3": "not",
        "4": "be",
        "5": "using",
        "6": "the computer"
      },
      "options": ["1,2,3,4,5,6", "2,3,4,5,6,1", "1,3,2,4,5,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous_negative",
      "hint": "Negative Future Continuous = will not be + verb-ing"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=will be\", \"3=studying\", \"4=at\", \"5=7 PM\"",
      "numbered_options": {
        "1": "She",
        "2": "will be",
        "3": "studying",
        "4": "at",
        "5": "7 PM"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous",
      "hint": "Will be + verb-ing for action in progress in future"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will\", \"3=be\", \"4=traveling\", \"5=to Italy\"",
      "numbered_options": {
        "1": "They",
        "2": "will",
        "3": "be",
        "4": "traveling",
        "5": "to Italy"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "5,4,3,2,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous",
      "hint": "Future Continuous = will be + V-ing"
    },
    {
      "question": "Gap tuzing: \"1=I\", \"2=will be\", \"3=waiting\", \"4=for you\", \"5=outside the station\"",
      "numbered_options": {
        "1": "I",
        "2": "will be",
        "3": "waiting",
        "4": "for you",
        "5": "outside the station"
      },
      "options": ["1,2,3,4,5", "4,3,2,1,5", "1,3,2,5,4"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Use 'will be' + V-ing for action at a future time"
    },
    {
      "question": "Tartiblang: \"1=At this time tomorrow\", \"2=he\", \"3=will be\", \"4=driving\", \"5=to the airport\"",
      "numbered_options": {
        "1": "At this time tomorrow",
        "2": "he",
        "3": "will be",
        "4": "driving",
        "5": "to the airport"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,3,4,5,1"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "An action in progress at a specific time in the future"
    },
    {
      "question": "Gap tuzing: \"1=We\", \"2=won't\", \"3=be\", \"4=attending\", \"5=the meeting\"",
      "numbered_options": {
        "1": "We",
        "2": "won't",
        "3": "be",
        "4": "attending",
        "5": "the meeting"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous_negative",
      "hint": "Negative: won't be + verb-ing"
    },
    {
      "question": "Tartiblang: \"1=Will\", \"2=you\", \"3=be\", \"4=working\", \"5=late tonight?\"",
      "numbered_options": {
        "1": "Will",
        "2": "you",
        "3": "be",
        "4": "working",
        "5": "late tonight?"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "5,4,3,2,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous_question",
      "hint": "Future Continuous Question = Will + subject + be + V-ing?"
    },
    {
      "question": "Tartiblang: \"1=By 9 PM\", \"2=they\", \"3=will be\", \"4=watching\", \"5=a movie\"",
      "numbered_options": {
        "1": "By 9 PM",
        "2": "they",
        "3": "will be",
        "4": "watching",
        "5": "a movie"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,3,4,5,1"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Future time expression often begins the sentence"
    },
    {
      "question": "Gap tuzing: \"1=I\", \"2=will\", \"3=not\", \"4=be\", \"5=using\", \"6=the computer\"",
      "numbered_options": {
        "1": "I",
        "2": "will",
        "3": "not",
        "4": "be",
        "5": "using",
        "6": "the computer"
      },
      "options": ["1,2,3,4,5,6", "2,3,4,5,6,1", "1,3,2,4,5,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous_negative",
      "hint": "Negative Future Continuous = will not be + verb-ing"
    },
    {
      "question": "Tartiblang: \"1=Tomorrow\", \"2=at noon\", \"3=I\", \"4=will be\", \"5=meeting\", \"6=my boss\"",
      "numbered_options": {
        "1": "Tomorrow",
        "2": "at noon",
        "3": "I",
        "4": "will be",
        "5": "meeting",
        "6": "my boss"
      },
      "options": ["1,2,3,4,5,6", "3,4,5,6,1,2", "1,3,4,5,2,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Time expression can come at the beginning"
    },
    {
      "question": "Gap tuzing: \"1=Will\", \"2=they\", \"3=be\", \"4=playing\", \"5=football\", \"6=on Sunday?\"",
      "numbered_options": {
        "1": "Will",
        "2": "they",
        "3": "be",
        "4": "playing",
        "5": "football",
        "6": "on Sunday?"
      },
      "options": ["1,2,3,4,5,6", "2,1,3,4,5,6", "6,5,4,3,2,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous_question",
      "hint": "Yes/No question in future continuous = Will + subject + be + V-ing?"
    },
    {
      "question": "Tartiblang: \"1=You\", \"2=will\", \"3=be\", \"4=using\", \"5=this app\", \"6=every day\"",
      "numbered_options": {
        "1": "You",
        "2": "will",
        "3": "be",
        "4": "using",
        "5": "this app",
        "6": "every day"
      },
      "options": ["1,2,3,4,5,6", "2,1,3,4,5,6", "1,3,2,4,5,6"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_continuous",
      "hint": "Will be + V-ing"
    },
    {
      "question": "Tartiblang: \"1=Next week\", \"2=he\", \"3=will be\", \"4=working\", \"5=remotely\"",
      "numbered_options": {
        "1": "Next week",
        "2": "he",
        "3": "will be",
        "4": "working",
        "5": "remotely"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Subject + will be + verb-ing"
    },
    {
      "question": "Gap tuzing: \"1=By this time next week\", \"2=we\", \"3=will be\", \"4=relaxing\", \"5=on the beach\"",
      "numbered_options": {
        "1": "By this time next week",
        "2": "we",
        "3": "will be",
        "4": "relaxing",
        "5": "on the beach"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "Future continuous for planned actions"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=will\", \"3=still\", \"4=be\", \"5=sleeping\", \"6=at 6 AM\"",
      "numbered_options": {
        "1": "I",
        "2": "will",
        "3": "still",
        "4": "be",
        "5": "sleeping",
        "6": "at 6 AM"
      },
      "options": ["1,2,3,4,5,6", "2,1,3,4,5,6", "1,2,4,3,5,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous",
      "hint": "'Still' comes before 'be'"
    },
    {
      "question": "Gap tuzing: \"1=We\", \"2=won’t\", \"3=be\", \"4=having\", \"5=a meeting\", \"6=on Friday\"",
      "numbered_options": {
        "1": "We",
        "2": "won’t",
        "3": "be",
        "4": "having",
        "5": "a meeting",
        "6": "on Friday"
      },
      "options": ["1,2,3,4,5,6", "2,1,3,4,5,6", "1,3,2,4,5,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_continuous_negative",
      "hint": "Negative form = won’t be + V-ing"
    }
    ],
    "future_perfect": [
    {
      "question": "Tartiblang: \"1=By next year\", \"2=they\", \"3=will have\", \"4=completed\", \"5=the project\"",
      "numbered_options": {
        "1": "By next year",
        "2": "they",
        "3": "will have",
        "4": "completed",
        "5": "the project"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Will have + past participle before a future time"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=will have\", \"3=left\", \"4=before\", \"5=we arrive\"",
      "numbered_options": {
        "1": "She",
        "2": "will have",
        "3": "left",
        "4": "before",
        "5": "we arrive"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Used to show earlier future action"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=finished\", \"4=the work\", \"5=by Monday\"",
      "numbered_options": {
        "1": "They",
        "2": "will have",
        "3": "finished",
        "4": "the work",
        "5": "by Monday"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "'By + time' indicates deadline"
    },
    {
      "question": "Tartiblang: \"1=By 2026\", \"2=he\", \"3=will have\", \"4=written\", \"5=ten books\"",
      "numbered_options": {
        "1": "By 2026",
        "2": "he",
        "3": "will have",
        "4": "written",
        "5": "ten books"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Future perfect expresses achievement by a future point"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=will have\", \"3=traveled\", \"4=to three countries\", \"5=by July\"",
      "numbered_options": {
        "1": "We",
        "2": "will have",
        "3": "traveled",
        "4": "to three countries",
        "5": "by July"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Use 'by' + future time to indicate deadline"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=will not have\", \"3=finished\", \"4=her homework\", \"5=by then\"",
      "numbered_options": {
        "1": "She",
        "2": "will not have",
        "3": "finished",
        "4": "her homework",
        "5": "by then"
      },
      "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "negative_future_perfect",
      "hint": "Negative: will not have + past participle"
    },
    {
      "question": "Tartiblang: \"1=By midnight\", \"2=they\", \"3=will have\", \"4=gone\", \"5=to bed\"",
      "numbered_options": {
        "1": "By midnight",
        "2": "they",
        "3": "will have",
        "4": "gone",
        "5": "to bed"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Perfect action finished before a future deadline"
    },
    {
      "question": "Tartiblang: \"1=He\", \"2=will have\", \"3=earned\", \"4=his degree\", \"5=by June\"",
      "numbered_options": {
        "1": "He",
        "2": "will have",
        "3": "earned",
        "4": "his degree",
        "5": "by June"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "By + date + will have + verb 3"
    },
    {
      "question": "Tartiblang: \"1=You\", \"2=will have\", \"3=learned\", \"4=a lot\", \"5=by the end of the course\"",
      "numbered_options": {
        "1": "You",
        "2": "will have",
        "3": "learned",
        "4": "a lot",
        "5": "by the end of the course"
      },
      "options": ["1,2,3,4,5", "5,4,3,2,1", "2,1,3,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Future perfect for result by course end"
    },
    {
      "question": "Tartiblang: \"1=Will\", \"2=you\", \"3=have\", \"4=completed\", \"5=the report\", \"6=by tomorrow?\"",
      "numbered_options": {
        "1": "Will",
        "2": "you",
        "3": "have",
        "4": "completed",
        "5": "the report",
        "6": "by tomorrow?"
      },
      "options": ["1,2,3,4,5,6", "2,1,3,4,5,6", "1,3,2,4,5,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect_question",
      "hint": "Question: Will + subject + have + past participle"
    },
     {
    "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=built\", \"4=the house\", \"5=by summer\"",
    "numbered_options": {
      "1": "They",
      "2": "will have",
      "3": "built",
      "4": "the house",
      "5": "by summer"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect",
    "hint": "They will have + past participle + time marker"
  },
  {
    "question": "Tartiblang: \"1=He\", \"2=won't have\", \"3=finished\", \"4=his shift\", \"5=by 8 o'clock\"",
    "numbered_options": {
      "1": "He",
      "2": "won't have",
      "3": "finished",
      "4": "his shift",
      "5": "by 8 o'clock"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "negative_future_perfect",
    "hint": "Won’t have + past participle = negative form"
  },
  {
    "question": "Tartiblang: \"1=Will\", \"2=she\", \"3=have\", \"4=arrived\", \"5=by the time we leave?\"",
    "numbered_options": {
      "1": "Will",
      "2": "she",
      "3": "have",
      "4": "arrived",
      "5": "by the time we leave?"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect_question",
    "hint": "Question format: Will + subject + have + past participle"
  },
  {
    "question": "Tartiblang: \"1=We\", \"2=will have\", \"3=used\", \"4=all the paper\", \"5=before the event starts\"",
    "numbered_options": {
      "1": "We",
      "2": "will have",
      "3": "used",
      "4": "all the paper",
      "5": "before the event starts"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect",
    "hint": "Before + event = future deadline"
  },
  {
    "question": "Tartiblang: \"1=By next Friday\", \"2=I\", \"3=will have\", \"4=read\", \"5=the whole book\"",
    "numbered_options": {
      "1": "By next Friday",
      "2": "I",
      "3": "will have",
      "4": "read",
      "5": "the whole book"
    },
    "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "By + future time = deadline"
  }
  ],





   "future_perfect": [
  {
    "question": "Tartiblang: \"1=I\", \"2=will have\", \"3=finished\", \"4=my work\", \"5=by 5 pm\"",
    "numbered_options": {
      "1": "I",
      "2": "will have",
      "3": "finished",
      "4": "my work",
      "5": "by 5 pm"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "Subject + will have + past participle + time"
  },
  {
    "question": "Tartiblang: \"1=She\", \"2=will have\", \"3=left\", \"4=the office\", \"5=before you arrive\"",
    "numbered_options": {
      "1": "She",
      "2": "will have",
      "3": "left",
      "4": "the office",
      "5": "before you arrive"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect",
    "hint": "Before + event = deadline in future"
  },
  {
    "question": "Tartiblang: \"1=They\", \"2=won't have\", \"3=completed\", \"4=the project\", \"5=by next week\"",
    "numbered_options": {
      "1": "They",
      "2": "won't have",
      "3": "completed",
      "4": "the project",
      "5": "by next week"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "negative_future_perfect",
    "hint": "Negative: won't have + past participle"
  },
  {
    "question": "Tartiblang: \"1=Will\", \"2=you\", \"3=have\", \"4=written\", \"5=the report by Monday?\"",
    "numbered_options": {
      "1": "Will",
      "2": "you",
      "3": "have",
      "4": "written",
      "5": "the report by Monday?"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "3,2,1,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "question_future_perfect",
    "hint": "Question: Will + subject + have + V3"
  },
  {
    "question": "Tartiblang: \"1=By 2026\", \"2=they\", \"3=will have\", \"4=launched\", \"5=the new product\"",
    "numbered_options": {
      "1": "By 2026",
      "2": "they",
      "3": "will have",
      "4": "launched",
      "5": "the new product"
    },
    "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "Future deadline: By + year"
  },
  {
    "question": "Tartiblang: \"1=We\", \"2=will have\", \"3=eaten\", \"4=dinner\", \"5=before 9\"",
    "numbered_options": {
      "1": "We",
      "2": "will have",
      "3": "eaten",
      "4": "dinner",
      "5": "before 9"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "Standard future perfect sentence"
  },
  {
    "question": "Tartiblang: \"1=He\", \"2=won't have\", \"3=returned\", \"4=home\", \"5=by night\"",
    "numbered_options": {
      "1": "He",
      "2": "won't have",
      "3": "returned",
      "4": "home",
      "5": "by night"
    },
    "options": ["1,2,3,4,5", "1,3,2,4,5", "2,1,3,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "negative_future_perfect",
    "hint": "Won’t have + V3"
  },
  {
    "question": "Tartiblang: \"1=By the time you arrive\", \"2=I\", \"3=will have\", \"4=finished\", \"5=cooking\"",
    "numbered_options": {
      "1": "By the time you arrive",
      "2": "I",
      "3": "will have",
      "4": "finished",
      "5": "cooking"
    },
    "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect",
    "hint": "Time clause at beginning"
  },
  {
    "question": "Tartiblang: \"1=The guests\", \"2=will have\", \"3=left\", \"4=before midnight\", \"5=probably\"",
    "numbered_options": {
      "1": "The guests",
      "2": "will have",
      "3": "left",
      "4": "before midnight",
      "5": "probably"
    },
    "options": ["1,5,2,3,4", "1,2,3,4,5", "5,1,2,3,4"],
    "correct": 0,
    "level": "hard",
    "grammar_point": "future_perfect_with_adverb",
    "hint": "Adverb goes before 'will'"
  },
  {
    "question": "Tartiblang: \"1=You\", \"2=will have\", \"3=read\", \"4=all the chapters\", \"5=by the test\"",
    "numbered_options": {
      "1": "You",
      "2": "will have",
      "3": "read",
      "4": "all the chapters",
      "5": "by the test"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "Will have + past participle + by..."
  },
  {
    "question": "Tartiblang: \"1=She\", \"2=will not have\", \"3=met\", \"4=him\", \"5=until the party\"",
    "numbered_options": {
      "1": "She",
      "2": "will not have",
      "3": "met",
      "4": "him",
      "5": "until the party"
    },
    "options": ["1,2,3,4,5", "1,3,2,4,5", "2,1,3,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "negative_future_perfect",
    "hint": "Until = similar to by in negative"
  },
  {
    "question": "Tartiblang: \"1=Will\", \"2=they\", \"3=have\", \"4=completed\", \"5=everything on time?\"",
    "numbered_options": {
      "1": "Will",
      "2": "they",
      "3": "have",
      "4": "completed",
      "5": "everything on time?"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "3,2,1,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect_question",
    "hint": "Will + they + have + V3"
  },
  {
    "question": "Tartiblang: \"1=By this time next year\", \"2=I\", \"3=will have\", \"4=graduated\", \"5=from university\"",
    "numbered_options": {
      "1": "By this time next year",
      "2": "I",
      "3": "will have",
      "4": "graduated",
      "5": "from university"
    },
    "options": ["1,2,3,4,5", "2,3,4,5,1", "3,2,4,5,1"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "By + future time → future perfect"
  },
  {
    "question": "Tartiblang: \"1=We\", \"2=will have\", \"3=visited\", \"4=three cities\", \"5=by next weekend\"",
    "numbered_options": {
      "1": "We",
      "2": "will have",
      "3": "visited",
      "4": "three cities",
      "5": "by next weekend"
    },
    "options": ["1,2,3,4,5", "1,3,2,4,5", "2,1,3,4,5"],
    "correct": 0,
    "level": "easy",
    "grammar_point": "future_perfect",
    "hint": "Standard future perfect sentence"
  },
  {
    "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=built\", \"4=the house\", \"5=by summer\"",
    "numbered_options": {
      "1": "They",
      "2": "will have",
      "3": "built",
      "4": "the house",
      "5": "by summer"
    },
    "options": ["1,2,3,4,5", "2,1,3,4,5", "1,3,2,4,5"],
    "correct": 0,
    "level": "medium",
    "grammar_point": "future_perfect",
    "hint": "They will have + past participle + time marker"
  }
],




"future_perfect_cont":
 [
    {
      "question": "Tartiblang: \"1=By this time\", \"2=next year\", \"3=they\", \"4=will have\", \"5=completed\", \"6=the project\"",
      "numbered_options": {
        "1": "By this time",
        "2": "next year",
        "3": "they",
        "4": "will have",
        "5": "completed",
        "6": "the project"
      },
      "options": ["1,2,3,4,5,6", "3,4,5,6,1,2", "1,2,4,3,5,6"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "By [time], subject + will have + V3"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=will have\", \"3=left\", \"4=before\", \"5=you\", \"6=arrive\"",
      "numbered_options": {
        "1": "She",
        "2": "will have",
        "3": "left",
        "4": "before",
        "5": "you",
        "6": "arrive"
      },
      "options": ["1,2,3,4,5,6", "4,5,6,1,2,3", "2,1,3,4,5,6"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Future perfect before another future action"
    },
    {
      "question": "Tartiblang: \"1=By 2025\", \"2=scientists\", \"3=will have\", \"4=discovered\", \"5=a cure\"",
      "numbered_options": {
        "1": "By 2025",
        "2": "scientists",
        "3": "will have",
        "4": "discovered",
        "5": "a cure"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "1,3,2,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "By [year], subject + will have + V3"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=will have\", \"3=written\", \"4=five reports\", \"5=by tomorrow\"",
      "numbered_options": {
        "1": "I",
        "2": "will have",
        "3": "written",
        "4": "five reports",
        "5": "by tomorrow"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Future result by a deadline"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=arrived\", \"4=by the time\", \"5=we\", \"6=get there\"",
      "numbered_options": {
        "1": "They",
        "2": "will have",
        "3": "arrived",
        "4": "by the time",
        "5": "we",
        "6": "get there"
      },
      "options": ["1,2,3,4,5,6", "4,5,6,1,2,3", "1,3,2,5,6,4"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "By the time + present simple, future perfect"
    },
    {
      "question": "Tartiblang: \"1=He\", \"2=will have\", \"3=read\", \"4=all the books\", \"5=by summer\"",
      "numbered_options": {
        "1": "He",
        "2": "will have",
        "3": "read",
        "4": "all the books",
        "5": "by summer"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "1,3,2,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Focus on completed action before a time"
    },
     {
      "question": "Tartiblang: \"1=By this time\", \"2=next year\", \"3=they\", \"4=will have\", \"5=completed\", \"6=the project\"",
      "numbered_options": {
        "1": "By this time",
        "2": "next year",
        "3": "they",
        "4": "will have",
        "5": "completed",
        "6": "the project"
      },
      "options": ["1,2,3,4,5,6", "3,4,5,6,1,2", "1,2,4,3,5,6"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "By [time], subject + will have + V3"
    },
    {
      "question": "Tartiblang: \"1=She\", \"2=will have\", \"3=left\", \"4=before\", \"5=you\", \"6=arrive\"",
      "numbered_options": {
        "1": "She",
        "2": "will have",
        "3": "left",
        "4": "before",
        "5": "you",
        "6": "arrive"
      },
      "options": ["1,2,3,4,5,6", "4,5,6,1,2,3", "2,1,3,4,5,6"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Future perfect before another future action"
    },
    {
      "question": "Tartiblang: \"1=By 2025\", \"2=scientists\", \"3=will have\", \"4=discovered\", \"5=a cure\"",
      "numbered_options": {
        "1": "By 2025",
        "2": "scientists",
        "3": "will have",
        "4": "discovered",
        "5": "a cure"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "1,3,2,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "By [year], subject + will have + V3"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=will have\", \"3=written\", \"4=five reports\", \"5=by tomorrow\"",
      "numbered_options": {
        "1": "I",
        "2": "will have",
        "3": "written",
        "4": "five reports",
        "5": "by tomorrow"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "1,3,2,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Future result by a deadline"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=arrived\", \"4=by the time\", \"5=we\", \"6=get there\"",
      "numbered_options": {
        "1": "They",
        "2": "will have",
        "3": "arrived",
        "4": "by the time",
        "5": "we",
        "6": "get there"
      },
      "options": ["1,2,3,4,5,6", "4,5,6,1,2,3", "1,3,2,5,6,4"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "By the time + present simple, future perfect"
    },
    {
      "question": "Tartiblang: \"1=He\", \"2=will have\", \"3=read\", \"4=all the books\", \"5=by summer\"",
      "numbered_options": {
        "1": "He",
        "2": "will have",
        "3": "read",
        "4": "all the books",
        "5": "by summer"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "1,3,2,4,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Focus on completed action before a time"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=will have\", \"3=finished\", \"4=my work\", \"5=by the time\", \"6=you arrive\"",
      "numbered_options": {
        "1": "I",
        "2": "will have",
        "3": "finished",
        "4": "my work",
        "5": "by the time",
        "6": "you arrive"
      },
      "options": ["1,2,3,4,5,6", "5,6,1,2,3,4", "1,3,2,4,5,6"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Future perfect for completed action before another future event"
    },
    {
      "question": "Tartiblang: \"1=By next week\", \"2=I\", \"3=will have\", \"4=completed\", \"5=my assignment\"",
      "numbered_options": {
        "1": "By next week",
        "2": "I",
        "3": "will have",
        "4": "completed",
        "5": "my assignment"
      },
      "options": ["1,2,3,4,5", "2,3,4,5,1", "1,2,4,3,5"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Will have + V3 for completed future actions"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=gone\", \"4=before\", \"5=we\", \"6=arrive\"",
      "numbered_options": {
        "1": "They",
        "2": "will have",
        "3": "gone",
        "4": "before",
        "5": "we",
        "6": "arrive"
      },
      "options": ["1,2,3,4,5,6", "5,6,1,2,3,4", "4,5,6,1,2,3"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Event will be completed before another future event"
    },
    {
      "question": "Tartiblang: \"1=They\", \"2=will have\", \"3=completed\", \"4=the project\", \"5=by next month\"",
      "numbered_options": {
        "1": "They",
        "2": "will have",
        "3": "completed",
        "4": "the project",
        "5": "by next month"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "1,3,2,5,4"],
      "correct": 0,
      "level": "easy",
      "grammar_point": "future_perfect",
      "hint": "Future perfect used to describe actions finished in the future"
    },
    {
      "question": "Tartiblang: \"1=He\", \"2=will have\", \"3=visited\", \"4=several countries\", \"5=by the time he is 30\"",
      "numbered_options": {
        "1": "He",
        "2": "will have",
        "3": "visited",
        "4": "several countries",
        "5": "by the time he is 30"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "1,5,2,3,4"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "An action completed in the future before a certain age"
    },
    {
      "question": "Tartiblang: \"1=I\", \"2=will have\", \"3=spoken\", \"4=to the teacher\", \"5=by the end of class\"",
      "numbered_options": {
        "1": "I",
        "2": "will have",
        "3": "spoken",
        "4": "to the teacher",
        "5": "by the end of class"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "2,3,1,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Subject + will have + V3 (completed action)"
    },
    {
      "question": "Tartiblang: \"1=We\", \"2=will have\", \"3=completed\", \"4=all assignments\", \"5=by tomorrow\"",
      "numbered_options": {
        "1": "We",
        "2": "will have",
        "3": "completed",
        "4": "all assignments",
        "5": "by tomorrow"
      },
      "options": ["1,2,3,4,5", "5,1,2,3,4", "2,1,3,4,5"],
      "correct": 0,
      "level": "medium",
      "grammar_point": "future_perfect",
      "hint": "Action completed by a certain future time"
    }
  ]
}

# Foydalanuvchi ma'lumotlari
user_data = {}
ratings = {}
ADMIN_IDS = [7871012050]  # Admin ID larini qo'shing

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧠❤️👀 State Verbs"), KeyboardButton(text="📚 English Lessons")],
            [KeyboardButton(text="📜 Preposition Verbs"), KeyboardButton(text="🌟 Irregular Verbs")],
            [KeyboardButton(text="⏳ English Tenses"), KeyboardButton(text="👤 Profil")],
            [KeyboardButton(text="📈 Reyting"), KeyboardButton(text="📞 Adminga murojaat")],
        ],
        resize_keyboard=True
    )
    await message.answer("Quyidagi funksiyalardan birini tanlang:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "⬅️ Ortga")
async def back_to_main_menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
       keyboard=[
            [KeyboardButton(text="🧠❤️👀 State Verbs"),  KeyboardButton(text="📚 English Lessons")],
            [KeyboardButton(text="📜 Preposition Verbs"), KeyboardButton(text="🌟 Irregular Verbs")],
            [KeyboardButton(text="⏳ English Tenses"),    KeyboardButton(text="👤 Profil")],  
            [KeyboardButton(text="📈 Reyting"),           KeyboardButton(text="📞 Adminga murojaat")],
        ],
        resize_keyboard=True
    )

    await message.answer("🔙 *Asosiy menyuga qaytdingiz.*", reply_markup=keyboard, parse_mode="Markdown")


@dp.message(lambda message: message.text == "📜 Preposition Verbs")
async def show_preposition_verbs(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📜 P verb 1"), KeyboardButton(text="📜 P verb 2")],
            [KeyboardButton(text="📜 P verb 3"), KeyboardButton(text="📜 P verb 4")],
            [KeyboardButton(text="📜 P verb 5"), KeyboardButton(text="📜 P verb 6")],
            [KeyboardButton(text="📜 P verb 7"), KeyboardButton(text="📜 P verb 8")],
            [KeyboardButton(text="📜 P verb 9"), KeyboardButton(text="📜 P verb 10")],
            [KeyboardButton(text="♻️ Barcha Preposition Verbs")],
            [KeyboardButton(text="⬅️ Ortga")],
        ],
        resize_keyboard=True
    )

    await message.answer(
        "📜 *Preposition Verbs testlaridan birini tanlang:*\n\n"
        "📌 *Asosiy fe'llar:*\n"
        "1️⃣ P verb 1 - Eng ko'p ishlatiladigan preposition verbs\n"
        "2️⃣ P verb 2 - Ko'proq ishlatiladigan preposition verbs\n\n"
        "📌 *Qo'shimcha fe'llar:*\n"
        "3️⃣ P verb 3 - Qo'shimcha va murakkab preposition verbs\n"
        "4️⃣ P verb 4 - Kam uchraydigan va qiyin preposition verbs\n\n"
        "📌 *Kengaytirilgan to'plamlar:*\n"
        "5️⃣ P verb 5 - Biznes sohasidagi preposition verbs\n"
        "6️⃣ P verb 6 - Tibbiyot sohasidagi preposition verbs\n\n"
        "📌 *Maxsus to'plamlar:*\n"
        "7️⃣ P verb 7 - IT sohasidagi preposition verbs\n"
        "8️⃣ P verb 8 - Huquq sohasidagi preposition verbs\n\n"
        "📌 *Qo'shimcha to'plamlar:*\n"
        "9️⃣ P verb 9 - Turizm sohasidagi preposition verbs\n"
        "🔟 P verb 10 - Ta'lim sohasidagi preposition verbs\n\n"
        "♻️ - *Barcha preposition verbs aralash holda*\n"
        "⬅️ *Ortga qaytish*",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


@dp.message(lambda message: message.text == "🌟 Irregular Verbs")
async def show_irregular_verbs(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌟 I verb 1"), KeyboardButton(text="🌟 I verb 2")],
            [KeyboardButton(text="🌟 I verb 3"), KeyboardButton(text="🌟 I verb 4")],
            [KeyboardButton(text="🌟 I verb 5"), KeyboardButton(text="🌟 I verb 6")],
            [KeyboardButton(text="🌟 I verb All")],
            [KeyboardButton(text="♻️ Barcha Irregular Verbs")],
            [KeyboardButton(text="⬅️ Ortga")],
        ],
        resize_keyboard=True
    )

    await message.answer(
 """
🌟 *Irregular Verbs testlaridan birini tanlang:*\n\n
📌 *Eng ko‘p ishlatiladigan fe’llar:*\n
1️⃣ I verb 1 - 1 dan 20 gacha\n\n
📌 *Qo‘shimcha fe’llar:*\n
2️⃣ I verb 2 - 21 dan 40 gacha\n\n
📌 *Kamroq ishlatiladigan fe’llar:*\n
3️⃣ I verb 3 - 41 dan 60 gacha \n\n
📌 *Noyob fe’llar:*\n
4️⃣ I verb 4 - 61 dan 80 gacha\n\n
5️⃣ I verb 5 - 81 dan 100 gacha\n\n
6️⃣ I verb 6 - 100 dan 120 gacha\n\n
🔄 All I verb ALL - Barcha testlarni takrorlash\n\n
💡 *Eslatma:* Kerakli raqamni tanlang yoki /buyruqni kiriting!
♻️ - *testni takrorlash*\n
⬅️ *Ortga qaytish*
""",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(F.text == "⏳ English Tenses")
async def show_tenses_menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⏳ Present Simple"), KeyboardButton(text="⏳ Present Continuous")],
            [KeyboardButton(text="⏳ Present Perfect"), KeyboardButton(text="⏳ Present Perfect Cont.")],
            [KeyboardButton(text="⏳ Past Simple"), KeyboardButton(text="⏳ Past Continuous")],
            [KeyboardButton(text="⏳ Past Perfect"), KeyboardButton(text="⏳ Past Perfect Cont.")],
            [KeyboardButton(text="⏳ Future Simple"), KeyboardButton(text="⏳ Future Continuous")],
            [KeyboardButton(text="⏳ Future Perfect"), KeyboardButton(text="⏳ Future Perfect Cont.")],
            [KeyboardButton(text="⬅️ Ortga")],
        ],
        resize_keyboard=True
    )
    await message.answer(
        "⏳ English Tenses testlaridan birini tanlang:\n\n"
        "📌 *Present tenses:*\n"
        "1️⃣ Present Simple - Oddiy hozirgi zamon\n"
        "2️⃣ Present Continuous - Davom etayotgan hozirgi zamon\n"
        "3️⃣ Present Perfect - Tugallangan hozirgi zamon\n"
        "4️⃣ Present Perfect Continuous - Tugallangan davomli zamon\n\n"
        "📌 *Past tenses:*\n"
        "5️⃣ Past Simple - Oddiy o'tgan zamon\n"
        "6️⃣ Past Continuous - Davom etgan o'tgan zamon\n"
        "7️⃣ Past Perfect - Tugallangan o'tgan zamon\n"
        "8️⃣ Past Perfect Continuous - Tugallangan davomli o'tgan zamon\n\n"
        "📌 *Future tenses:*\n"
        "9️⃣ Future Simple - Oddiy kelasi zamon\n"
        "🔟 Future Continuous - Davom etadigan kelasi zamon\n"
        "1️⃣1️⃣ Future Perfect - Tugallangan kelasi zamon\n"
        "1️⃣2️⃣ Future Perfect Continuous - Tugallangan davomli kelasi zamon\n\n"
        "♻️ - *Barcha zamonlar aralash*\n"
        "⬅️ *Ortga qaytish*",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


@dp.message(lambda message: message.text == "📚 English Lessons")
async def show_english_lessons(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1️⃣ The Noun"), KeyboardButton(text="2️⃣ Pronouns")],
            [KeyboardButton(text="3️⃣ A lot of/much/many")],
            [KeyboardButton(text="⬅️ Ortga")],
        ],
        resize_keyboard=True
    )

    await message.answer(
        "📚 *Ingliz tili darslaridan birini tanlang:*\n\n"
        "1️⃣ *The Noun* - Otlar va ularning qo'llanilishi\n"
        "2️⃣ *Pronouns* - Olmoshlar (I, you, he, she...)\n"
        "3️⃣ *A lot of/much/many* - Miqdor bildiruvchi so'zlar\n"
        "⬅️ *Asosiy menyuga qaytish*",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "1️⃣ The Noun")
async def show_noun_lesson(message: types.Message):
    await message.answer(
        """
📚 *Ingliz Tili Grammatikasi: Otlar (Nouns)*  

# --------------------------
# 1️⃣ *COUNTABLE vs UNCOUNTABLE NOUNS*
# --------------------------
✅ *Sanaladigan (Countable):*  
   - `a book` → `two books`  
   - `an apple` → `three apples`  

❌ *Sanalmaydigan (Uncountable):*  
   - `water` (✅ some water | ❌ two waters)  
   - `sugar` (✅ much sugar | ❌ five sugars)  

# --------------------------
# 2️⃣ *KO'PLIK QOIDALARI (-s, -es, -ves, -ies)*
# --------------------------
📌 *Oddiy qoida:* -s  
   - `cat → cats`  
   - `car → cars`  

📌 *-s, -ss, -ch, -sh, -x, -o:* -es  
   - `bus → buses`  
   - `tomato → tomatoes`  

📌 *-f/-fe:* -ves  
   - `wolf → wolves`  
   - `knife → knives`  

📌 *-y → -ies* (undosh oldida)  
   - `baby → babies`  
   - `city → cities`  

# --------------------------
# 3️⃣ *NOTO'G'RI KO'PLIKLAR (Irregular Plurals)*
# --------------------------
🔥 *O'zgaradiganlar:*  
   - `man → men`  
   - `woman → women`  

🔥 *O'zgarmaydiganlar:*  
   - `fish → fish`  
   - `deer → deer`  

# --------------------------
# 4️⃣ *SOME & COUNTABLE/UNCOUNTABLE*
# --------------------------
✨ *Sanaladigan (ko'plik):*  
   - `some books`  
   - `some apples`  

✨ *Sanalmaydigan:*  
   - `some water`  
   - `some milk`  

# --------------------------
# 5️⃣ *TO BE FE'LI (is/am/are)*
# --------------------------
💡 *Yakkalik:*  
   - `I am a doctor.`  
   - `She is here.`  

💡 *Ko'plik:*  
   - `We are students.`  
   - `They are happy.`  
        """,
        parse_mode="Markdown"
    )




@dp.message(lambda message: message.text == "2️⃣ Pronouns")
async def show_pronouns_lesson(message: types.Message):
    telegram_text = """
⭐ *Ingliz Tili Grammatikasi: Olmoshlar (Pronouns)*  
_(Python kodiga o'xshab tuzilgan, lekin oddiy matn)_  

# --------------------------
# 1️⃣ *DEMONSTRATIVE PRONOUNS (Ko'rsatish olmoshlari)*
# --------------------------

🔹 *Yaqin narsalar:*  
   - `This` is a book. (Bu kitob.)  
   - `These` are apples. (Bular olma.)  

🔹 *Uzoq narsalar:*  
   - `That` is a car. (U mashina.)  
   - `Those` are trees. (Ular daraxtlar.)  

✅ *Darak:* This is my bag.  
❓ *So'roq:* Is that your car?  
❌ *Inkor:* These are not your books.  

# --------------------------
# 2️⃣ *OBJECTIVE PRONOUNS (Ob'yekt olmoshlari)*
# --------------------------

📌 *Fe'lning ob'yecti* (nima? kim? ni/ga):  
   - She loves `me`.  
   - I see `him`.  
   - Give it to `us`.  

✅ *Darak:* She called me yesterday.  
❓ *So'roq:* Did you see him?  
❌ *Inkor:* They didn't invite us.  

# --------------------------
# 3️⃣ *POSSESSIVE ADJECTIVES (-ning)*
# --------------------------

🔹 *Ot oldidan keladi:*  
   - `My` book  
   - `His` car  
   - `Our` house  

✅ *Darak:* Her dress is beautiful.  
❓ *So'roq:* Is this your phone?  
❌ *Inkor:* Our teacher isn't here.  

# --------------------------
# 4️⃣ *POSSESSIVE PRONOUNS (-niki)*
# --------------------------

🔹 *Ot o'rniga keladi:*  
   - The book is `mine`.  
   - The car is `hers`.  

✅ *Darak:* The red pen is mine.  
❓ *So'roq:* Is this bag yours?  
❌ *Inkor:* Those shoes aren't hers.  

# --------------------------
# 5️⃣ *POSSESSIVE CASE (-ning qo'shmasi)*
# --------------------------

📌 *Qoidalar:*  
   - John's house  
   - The cats' food (ko'plik)  
   - Children's toys (noto'g'ri ko'plik)  

✅ *Darak:* Sam's brother is a doctor.  
❓ *So'roq:* Is this the cat's bowl?  
❌ *Inkor:* This isn't John's laptop.  

📚 *Eslatma:* Har bir turdagi olmoshni to'g'ri ishlatish muhim!
"""
    await message.answer(
        telegram_text,
        parse_mode="Markdown"
    )
@dp.message(lambda message: message.text == 3️⃣ A lot of/much/many)
async def show_quantifiers_lesson(message: types.Message):
    telegram_text = """
⭐ *Ingliz Tili Grammatikasi: Miqdor Olmoshlari (Quantifiers)*  

# --------------------------
# 1️⃣ *A LOT OF / LOTS OF*
# --------------------------

🔹 *Ma'nosi:* "Ko'p" (sanaladigan va sanalmaydigan otlar bilan)  
✅ *Misollar:*  
   - `She has a lot of books.` (Unda ko'p kitob bor)  
   - `There are lots of people here.` (Bu yerda ko'p odam bor)  

# --------------------------
# 2️⃣ *MUCH / HOW MUCH*
# --------------------------

🔹 *Ma'nosi:* "Ko'p" / "Qancha" (sanalmaydigan otlar)  
✅ *Misollar:*  
   - `We don't have much time.` (Bizda ko'p vaqt yo'q)  
   - `How much sugar do you need?` (Qancha shakar kerak?)  

# --------------------------
# 3️⃣ *MANY / HOW MANY*
# --------------------------

🔹 *Ma'nosi:* "Ko'p" / "Qancha" (sanaladigan otlar)  
✅ *Misollar:*  
   - `There aren't many apples left.` (Ko'p olma qolmagan)  
   - `How many students are there?` (Qancha talaba bor?)  

# --------------------------
# 4️⃣ *A LITTLE / LITTLE*
# --------------------------

🔹 *Ma'nosi:* "Bir oz" / "Juda kam" (sanalmaydigan otlar)  
✅ *Misollar:*  
   - `Add a little salt.` (Ozgina tuz qo'shing)  
   - `There's little hope.` (Umid juda kam)  

# --------------------------
# 5️⃣ *A FEW / FEW*
# --------------------------

🔹 *Ma'nosi:* "Bir necha" / "Juda kam" (sanaladigan otlar)  
✅ *Misollar:*  
   - `I have a few friends.` (Menda bir necha do'st bor)  
   - `Few people know this.` (Buni juda kam odam biladi)  

📌 *Farqlar:*
- `A little/A few` → Ijobiy (bir oz, lekin yetarli)
- `Little/Few` → Salbiy (juda kam, deyarli yo'q)
- `Much/Many` → Ko'pincha inkor/savol gaplarda

💡 *Eslatma:*  
- "Much" faqat sanalmaydigan otlar bilan  
- "Many" faqat sanaladigan otlar bilan  
- "A lot of" har ikkala tur bilan ishlatiladi
"""
    await message.answer(
        telegram_text,
        parse_mode="Markdown"
    )



@dp.message(lambda message: message.text == "👤 Profil")
async def show_profile(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        await message.answer("Siz hali test ishlamagansiz! 📌")
        return
    
    user_info = user_data[user_id]
    profile_text = "👤 *Sizning profilingiz:*\n\n"
    for subject, stats in user_info.get("subjects", {}).items():
        profile_text += (
            f"📚 *{subject.capitalize()}*\n"
            f"✅ To'g'ri javoblar: {stats.get('correct', 0)}\n"
            f"❌ Xato javoblar: {stats.get('wrong', 0)}\n"
            f"📊 Jami savollar: {stats.get('total', 0)}\n\n"
        )
    
    profile_text += f"🏆 Umumiy ball: {user_info.get('score', 0)}"
    await message.answer(profile_text, parse_mode="Markdown")

@dp.message(lambda message: message.text == "📈 Reyting")
async def show_ratings(message: types.Message):
    if not ratings:
        await message.answer("📌 Hali hech kim test ishlamagan!")
        return
    
    sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
    result = "🏆 *Top 10 Reyting:*\n\n"
    
    for idx, (user_id, score) in enumerate(sorted_ratings[:10], 1):
        try:
            user = await bot.get_chat(user_id)
            name = user.first_name or user.username or f"Foydalanuvchi {user_id}"
            result += f"{idx}. *{name}* - {score} ball\n"
        except Exception as e:
            print(f"Foydalanuvchi ma'lumotlarini olishda xato: {e}")
            result += f"{idx}. Foydalanuvchi {user_id} - {score} ball\n"
    
    await message.answer(result, parse_mode="Markdown")




@dp.message(lambda message: message.text in [
    "🧠❤️👀 State Verbs", 
    "📜 P verb 1", "📜 P verb 2", "📜 P verb 3", "📜 P verb 4", "📜 P verb 5", "📜 P verb 6", "📜 P verb 7", "📜 P verb 8",  "📜 P verb 9", "📜 P verb 10",
    "🌟 I verb 1", "🌟 I verb 2", "🌟 I verb 3", "🌟 I verb 4", "🌟 I verb 5", "🌟 I verb 6", "🌟 I verb All",
    "⏳ Present Simple", "⏳ Present Continuous", "⏳ Present Perfect", "⏳ Present Perfect Cont.",
    "⏳ Past Simple", "⏳ Past Continuous", "⏳ Past Perfect", "⏳ Past Perfect Cont.",
    "⏳ Future Simple", "⏳ Future Continuous", "⏳ Future Perfect", "⏳ Future Perfect Cont.",
    "♻️ Barcha Preposition Verbs", "♻️ Barcha Irregular Verbs"
])
async def start_quiz(message: types.Message):
    try:
        user_id = message.from_user.id
        subjects_map = {
            "🧠❤️👀 State Verbs": "state_verbs",
            "📜 P verb 1": "preposition_verbs1",
            "📜 P verb 2": "preposition_verbs2",
            "📜 P verb 3": "preposition_verbs3",
            "📜 P verb 4": "preposition_verbs4",
            "📜 P verb 5": "preposition_verbs5",
            "📜 P verb 6": "preposition_verbs6",
            "📜 P verb 7": "preposition_verbs7",
            "📜 P verb 8": "preposition_verbs8",
            "📜 P verb 9": "preposition_verbs9",
            "📜 P verb 10": "preposition_verbs10",
            "🌟 I verb 1": "irregular_verbs1",
            "🌟 I verb 2": "irregular_verbs2",
            "🌟 I verb 3": "irregular_verbs3",
            "🌟 I verb 4": "irregular_verbs4",
            "🌟 I verb 5": "irregular_verbs5",
            "🌟 I verb 6": "irregular_verbs6",
            "🌟 I verb All": "irregular_verbs_all",
            "⏳ Present Simple": "present_simple",
            "⏳ Present Continuous": "present_continuous",
            "⏳ Present Perfect": "present_perfect",
            "⏳ Present Perfect Cont.": "present_perfect_cont",
            "⏳ Past Simple": "past_simple",
            "⏳ Past Continuous": "past_continuous",
            "⏳ Past Perfect": "past_perfect",
            "⏳ Past Perfect Cont.": "past_perfect_cont",
            "⏳ Future Simple": "future_simple",
            "⏳ Future Continuous": "future_continuous",
            "⏳ Future Perfect": "future_perfect",
            "⏳ Future Perfect Cont.": "future_perfect_cont",
            "♻️ Barcha Preposition Verbs": "preposition_verbs_all",
            "♻️ Barcha Irregular Verbs": "irregular_verbs_all"
        }
        
        subject_key = subjects_map.get(message.text)
        if not subject_key:
            await message.answer("❌ Xatolik yuz berdi! Tanlov noto'g'ri.")
            return
        
        
        subject = subjects_map.get(message.text)
        if not subject:
            await message.answer("❌ Xatolik yuz berdi! Tanlov noto'g'ri.")
            return
        
  # Initialize user data if not exists
        if user_id not in user_data:
            user_data[user_id] = {
                "subjects": {},
                "score": 0,
                "current_question": {},
                "all_quizzes": [],
                "current_poll": None,
                "start_time": None
            }
        
        # Get the correct quiz based on subject
        if "tenses" in message.text.lower():
            quiz_type = "tenses"
            if subject_key == "all_tenses":
                tests = []
                for tense in quizzes["tenses"].values():
                    tests.extend(tense)
                random.shuffle(tests)
            else:
                tests = quizzes["tenses"].get(subject_key, [])
        else:
            quiz_type = subject_key
            tests = quizzes.get(quiz_type, [])
        
        if not tests:
            await message.answer("❌ Ushbu test hozircha mavjud emas!")
            return
        
        # Initialize subject data if not exists
        if quiz_type not in user_data[user_id]["subjects"]:
            user_data[user_id]["subjects"][quiz_type] = {
                "correct": 0,
                "wrong": 0,
                "total": 0,
                "current_index": 0,
                "attempts": 0
            }
        
        # Reset quiz progress if starting new quiz
        user_data[user_id]["all_quizzes"] = tests.copy()
        user_data[user_id]["subjects"][quiz_type]["current_index"] = 0
        user_data[user_id]["subjects"][quiz_type]["attempts"] += 1
        user_data[user_id]["start_time"] = time.time()
        
        await message.answer(
            f"📢 {message.text} testi boshlandi!\n\n"
            f"ℹ️ Har bir savolga 30 sekund vaqt beriladi!\n"
            f"🔢 Jami savollar: {len(tests)} ta",
        )
        await send_next_question(user_id, quiz_type, message.text)
        
    except KeyError:
        await message.answer("❌ Ushbu test hozircha mavjud emas!")
    except Exception as e:
        logging.error(f"Error in start_quiz: {e}")
        await message.answer("❌ Testni boshlashda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

async def send_next_question(user_id: int, subject: str, quiz_name: str):
    try:
        # Validate user data
        if user_id not in user_data:
            await bot.send_message(user_id, "❌ Foydalanuvchi ma'lumotlari topilmadi!")
            return
        
        user_info = user_data[user_id]
        questions = user_info.get("all_quizzes", [])
        subject_info = user_info["subjects"][subject]
        quiz_menu = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="⬅️ Testni tugatish")],
            ],
            resize_keyboard=True
        )
        
        await bot.send_message(
            user_id,
            f"🔹 Test: {quiz_name}\n"
            f"🔢 Savol: {subject_info['current_index'] + 1}/{len(questions)}",
            reply_markup=quiz_menu
        )
        # Check if quiz is completed
        if subject_info["current_index"] >= len(questions):
            await show_quiz_results(user_id, subject, quiz_name, subject_info)
            return
        
        question_data = questions[subject_info["current_index"]]
        
        # Validate question data
        if not question_data or "options" not in question_data or "correct" not in question_data:
            await bot.send_message(user_id, "❌ Savol formati noto'g'ri!")
            return
        
        # Prepare options and shuffle
        shuffled_options = question_data["options"].copy()
        correct_answer = shuffled_options[question_data["correct"]]
        random.shuffle(shuffled_options)
        new_correct_index = shuffled_options.index(correct_answer)
        
        # Store current poll data
        user_info["current_poll"] = {
            "poll_id": None,
            "subject": subject,
            "correct_option": new_correct_index,
            "question_index": subject_info["current_index"],
            "quiz_name": quiz_name,
            "start_time": time.time()
        }
        
        # Send the poll question with timer
        poll_msg = await bot.send_poll(
            chat_id=user_id,
            question=question_data["question"],
            options=shuffled_options,
            type="quiz",
            correct_option_id=new_correct_index,
            is_anonymous=False,
            open_period=30  
        )
        
        user_info["current_poll"]["poll_id"] = poll_msg.poll.id
        
    except Exception as e:
        logging.error(f"Error in send_next_question: {e}")
        await bot.send_message(user_id, "❌ Savol yuborishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")


@dp.message(lambda message: message.text == "⬅️ Testni tugatish")
async def finish_quiz_early(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return
    
    if "current_poll" in user_data[user_id]:
        quiz_name = user_data[user_id]["current_poll"]["quiz_name"]
        subject = user_data[user_id]["current_poll"]["subject"]
        await show_quiz_results(user_id, subject, quiz_name, user_data[user_id]["subjects"][subject])



async def show_quiz_results(user_id: int, subject: str, quiz_name: str, subject_info: dict):
    try:



        # Calculate time taken
        time_taken = int(time.time() - user_data[user_id]["start_time"])
        minutes = time_taken // 30
        seconds = time_taken % 30
        


        # Calculate accuracy percentage
        accuracy = 0
        if subject_info['total'] > 0:
            accuracy = (subject_info['correct'] / subject_info['total']) * 100
        

        
        # Prepare result message
        result_text = (
            f"🎉 {quiz_name} testi tugadi!\n\n"
            f"✅ To'g'ri javoblar: {subject_info['correct']}\n"
            f"❌ Noto'g'ri javoblar: {subject_info['wrong']}\n"
            f"📊 Jami savollar: {subject_info['total']}\n"
            f"💯 Aniqlik: {accuracy:.1f}%\n"
            f"⏱ Sarflangan vaqt: {minutes} min {seconds} sec\n\n"
            f"🔢 Urinishlar soni: {subject_info.get('attempts', 1)}"
        )
        
        await bot.send_message(user_id, result_text)
        keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧠❤️👀 State Verbs"), KeyboardButton(text="📚 English Lessons")],
            [KeyboardButton(text="📜 Preposition Verbs"), KeyboardButton(text="🌟 Irregular Verbs")],
            [KeyboardButton(text="⏳ English Tenses"), KeyboardButton(text="👤 Profil")],
            [KeyboardButton(text="📈 Reyting"), KeyboardButton(text="📞 Adminga murojaat")],
        ],
        resize_keyboard=True
    )
    
        await bot.send_message(user_id, "Test muvaffaqiyatli yakunlandi!", reply_markup=keyboard)
        # Update ratings
        ratings[user_id] = user_data[user_id]["score"]
        sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
        user_rank = next((idx for idx, (uid, _) in enumerate(sorted_ratings, 1) if uid == user_id), 0)
        
        await bot.send_message(
            user_id,
            f"🏆 Reytingdagi o'rningiz: {user_rank}\n"
            f"👥 Jami ishtirokchilar: {len(sorted_ratings)}"
        )
        
        # Reset quiz progress
        subject_info.update({
            "total": 0,
            "correct": 0,
            "wrong": 0,
            "current_index": 0
        })
        
    except Exception as e:
        logging.error(f"Error in show_quiz_results: {e}")
        await bot.send_message(user_id, "❌ Natijalarni ko'rsatishda xatolik yuz berdi.")




@dp.poll_answer()
async def handle_poll_answer(poll_answer: types.PollAnswer):
    try:
        user_id = poll_answer.user.id

        # Validate user data
        if user_id not in user_data:
            return

        user_info = user_data[user_id]
        if "current_poll" not in user_info:
            return

        poll_data = user_info["current_poll"]

        # Check if answer is too late (after 35 seconds)
        if time.time() - poll_data.get("start_time", 0) > 35:  # 5 second buffer
            await bot.send_message(user_id, "⏰ Vaqt tugadi! Keyingi savolga o'tamiz.")
            user_info["subjects"][poll_data["subject"]]["wrong"] += 1
            user_info["subjects"][poll_data["subject"]]["total"] += 1
            user_info["subjects"][poll_data["subject"]]["current_index"] += 1
            await send_next_question(user_id, poll_data["subject"], poll_data["quiz_name"])
            return

        # Validate answer
        if not poll_answer.option_ids:
            return  # If user did not select any option, nothing happens

        selected_option = poll_answer.option_ids[0]  # Get selected option
        subject = poll_data["subject"]  # Get current subject
        correct_option = poll_data["correct_option"]  # Get correct answer index
        question_index = poll_data["question_index"]  # Get current question index
        quiz_name = poll_data["quiz_name"]  # Get quiz name

        # Get current question data
        question_data = user_info["all_quizzes"][question_index]
        correct_answer = question_data["options"][question_data["correct"]]  # Correct answer

        # Check if the answer is correct
        if selected_option == correct_option:
            user_info["subjects"][subject]["correct"] += 1  # Increase correct answers count
            user_info["score"] += 1  # Increase overall score
            feedback = "✅ To'g'ri javob!"
        else:
            feedback = f"❌ Noto'g'ri javob! To'g'ri javob: {correct_answer}"  # Show correct answer for wrong choice
            user_info["subjects"][subject]["wrong"] += 1  # Increase wrong answers count

        # Update question stats
        user_info["subjects"][subject]["total"] += 1  # Increase total questions count
        user_info["subjects"][subject]["current_index"] += 1  # Move to next question

        # Send feedback to user
        await bot.send_message(user_id, feedback)

        # Proceed to the next question
        await send_next_question(user_id, subject, quiz_name)

    except Exception as e:
        logging.error(f"Error in handle_poll_answer: {e}")
        if user_id in user_data:
            await bot.send_message(user_id, "❌ Javoblarni qayta ishlashda xatolik yuz berdi.")
    quiz_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⬅️ Testni tugatish")],
        ],
        resize_keyboard=True
    )
    
    await bot.send_message(
        user_id,
        f"🔹 Test: {poll_data['quiz_name']}\n"
        f"🔢 Keyingi savolga o'tilmoqda...",
        reply_markup=quiz_menu
    )


# Contact admin handler
@dp.message(F.text == "📞 Adminga murojaat")
async def contact_admin(message: Message):
    await message.answer(
        "✍️ Adminga xabar yuborish uchun matn, rasm, video yoki fayl yuboring.\n\n"
        "Yoki to'g'ridan-to'g'ri @admin ga yozishingiz mumkin.",
        reply_markup=types.ReplyKeyboardRemove()
    )

# User to admin message handler
@dp.message(F.chat.type == "private", ~F.from_user.id.in_(ADMIN_IDS))
async def user_to_admin(message: Message):
    try:
        # Format user info
        user_info = (
            f"👤 Foydalanuvchi: {message.from_user.full_name}\n"
            f"🆔 ID: {message.from_user.id}\n"
            f"📅 Sana: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        )
        
        # Forward different message types to admin
        if message.text:
            caption = f"{user_info}📝 Xabar: {message.text}"
            for admin_id in ADMIN_IDS:
                await bot.send_message(admin_id, caption, reply_markup=types.ForceReply())
        
        elif message.photo:
            caption = f"{user_info}📷 Rasm"
            for admin_id in ADMIN_IDS:
                await bot.send_photo(admin_id, message.photo[-1].file_id, 
                                   caption=caption, 
                                   reply_markup=types.ForceReply())
        
        elif message.video:
            caption = f"{user_info}🎥 Video"
            for admin_id in ADMIN_IDS:
                await bot.send_video(admin_id, message.video.file_id, 
                                   caption=caption, 
                                   reply_markup=types.ForceReply())
        
        elif message.document:
            caption = f"{user_info}📄 Fayl: {message.document.file_name}"
            for admin_id in ADMIN_IDS:
                await bot.send_document(admin_id, message.document.file_id, 
                                      caption=caption, 
                                      reply_markup=types.ForceReply())
        
        await message.answer("✅ Xabaringiz adminlarga yuborildi. Javobni kuting.")
    
    except Exception as e:
        logging.error(f"Xabar yuborishda xato: {e}")
        await message.answer("❌ Xabar yuborishda xatolik yuz berdi. Iltimos, keyinroq urunib ko'ring.")

# Admin reply handler
@dp.message(F.reply_to_message, F.from_user.id.in_(ADMIN_IDS))
async def admin_to_user(message: Message):
    try:
        # Extract original message text
        original_msg = message.reply_to_message.text or message.reply_to_message.caption
        
        if original_msg and "👤 Foydalanuvchi:" in original_msg:
            # Extract user ID
            user_id_line = next(line for line in original_msg.split('\n') if "🆔 ID:" in line)
            user_id = int(user_id_line.split(":")[1].strip())
            
            # Send reply to user
            reply_text = (
                "📩 Admin javobi:\n\n"
                f"{message.text}\n\n"
                "💬 Savolingiz bo'lsa, yana yozishingiz mumkin."
            )
            await bot.send_message(user_id, reply_text)
            await message.answer("✅ Javob foydalanuvchiga yuborildi.")
    
    except Exception as e:
        logging.error(f"Javob yuborishda xato: {e}")
        await message.answer("❌ Javob yuborishda xatolik. Foydalanuvchi ID topilmadi.")

# Admin paneli
@dp.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ Siz admin emassiz!")
        return

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Statistika")],
            [KeyboardButton(text="📢 Reklama yuborish")],
            [KeyboardButton(text="🏠 Asosiy menyu")],  # Asosiy menyuga qaytish tugmasi
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await message.answer("👋 Admin panelga xush kelibsiz!", reply_markup=keyboard)

# Asosiy menyuga qaytish
@dp.message(lambda message: message.text == "🏠 Asosiy menyu")
async def back_to_main_menu(message: types.Message):
    await start(message)  # start funksiyasini chaqiramiz

# Admin: Statistika
@dp.message(F.text == "📊 Statistika")
async def show_statistics(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ Siz admin emassiz!")
        return

    total_users = len(user_data)  # Foydalanuvchilar sonini hisoblash
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

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
