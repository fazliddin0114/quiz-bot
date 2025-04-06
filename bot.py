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

# BotFather tomonidan berilgan token
TOKEN = "7267797063:AAGBVPXJ0Nm5c0k3Xb9W3nXqZN0J7l9k48Y"  # Bu yerga haqiqiy tokenni qo'ying
ADMIN_IDS = [7871012050]  # Admin IDlari

bot = Bot(token=TOKEN)
dp = Dispatcher()



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
    "irregular_verbs_2": [
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
,
"irregular_verbs_4": [
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
"irregular_verbs_5": [
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
    "irregular_verbs_6": [
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
      "question": "Quyidagi gapni to‘g‘ri tartibda tuzing:",
      "options": ["She", "works", "in a hospital"],
      "correct": [0, 1, 2],
      "level": "oson"
    },
    {
      "question": "Gap bo‘laklarini to‘g‘ri tartibda joylashtiring:",
      "options": ["They", "usually", "drink", "tea", "in the morning"],
      "correct": [0, 1, 2, 3, 4],
      "level": "oson"
    },
    {
      "question": "To‘g‘ri ketma-ketlikni tanlang:",
      "options": ["My parents", "live", "in Tashkent"],
      "correct": [0, 1, 2],
      "level": "oson"
    },
    {
      "question": "Gapni to‘g‘ri tuzing:",
      "options": ["He", "doesn't", "play", "tennis"],
      "correct": [0, 1, 2, 3],
      "level": "oson"
    },
    {
      "question": "Quyidagi so‘zlarni tartib bilan joylashtiring:",
      "options": ["We", "often", "visit", "our grandparents"],
      "correct": [0, 1, 2, 3],
      "level": "oson"
    },
    {
      "question": "To‘g‘ri tartibni tanlang:",
      "options": ["The sun", "rises", "in the east"],
      "correct": [0, 1, 2],
      "level": "oson"
    },
    {
      "question": "Gap tuzilishini tanlang:",
      "options": ["She", "always", "arrives", "on time"],
      "correct": [0, 1, 2, 3],
      "level": "oson"
    },
    {
      "question": "To‘g‘ri javobni belgilang:",
      "options": ["I", "don't", "like", "horror movies"],
      "correct": [0, 1, 2, 3],
      "level": "oson"
    },
    {
      "question": "So‘z bo‘laklarini to‘g‘ri joylashtiring:",
      "options": ["He", "teaches", "mathematics", "at university"],
      "correct": [0, 1, 2, 3],
      "level": "oson"
    },
    {
      "question": "Tartib bilan to‘g‘ri joylashtiring:",
      "options": ["They", "watch", "TV", "after dinner"],
      "correct": [0, 1, 2, 3],
      "level": "oson"
    },
    {
      "question": "Quyidagi gapni to‘g‘ri tartibda tuzing:",
      "options": ["My brother", "plays", "football", "on weekends"],
      "correct": [0, 1, 2, 3],
      "level": "murakkab"
    },
    {
      "question": "Gap bo‘laklarini to‘g‘ri tartibda joylashtiring:",
      "options": ["She", "never", "eats", "fast food"],
      "correct": [0, 1, 2, 3],
      "level": "murakkab"
    },
    {
      "question": "To‘g‘ri ketma-ketlikni tanlang:",
      "options": ["Water", "boils", "at 100 degrees Celsius"],
      "correct": [0, 1, 2],
      "level": "murakkab"
    },
    {
      "question": "Gapni to‘g‘ri tuzing:",
      "options": ["We", "don't", "speak", "French"],
      "correct": [0, 1, 2, 3],
      "level": "murakkab"
    },
    {
      "question": "Quyidagi so‘zlarni tartib bilan joylashtiring:",
      "options": ["The bus", "leaves", "at 8:30", "every morning"],
      "correct": [0, 1, 2, 3],
      "level": "murakkab"
    },
    {
      "question": "To‘g‘ri tartibni tanlang:",
      "options": ["I", "usually", "go", "to bed", "at 11 p.m."],
      "correct": [0, 1, 2, 3, 4],
      "level": "murakkab"
    },
    {
      "question": "Gap tuzilishini tanlang:",
      "options": ["He", "works", "as a doctor"],
      "correct": [0, 1, 2],
      "level": "murakkab"
    },
    {
      "question": "To‘g‘ri javobni belgilang:",
      "options": ["They", "don't", "watch", "TV", "very often"],
      "correct": [0, 1, 2, 3, 4],
      "level": "murakkab"
    },
    {
      "question": "So‘z bo‘laklarini to‘g‘ri joylashtiring:",
      "options": ["She", "reads", "a book", "every night"],
      "correct": [0, 1, 2, 3],
      "level": "murakkab"
    },
    {
      "question": "Tartib bilan to‘g‘ri joylashtiring:",
      "options": ["We", "have", "lunch", "at 1 o'clock"],
      "correct": [0, 1, 2, 3],
      "level": "murakkab"
    },
    {
      "question": "Quyidagi gapni to‘g‘ri tartibda tuzing:",
      "options": ["The Earth", "revolves", "around the Sun"],
      "correct": [0, 1, 2],
      "level": "qiyin"
    },
    {
      "question": "Gap bo‘laklarini to‘g‘ri tartibda joylashtiring:",
      "options": ["He", "doesn't", "smoke"],
      "correct": [0, 1, 2],
      "level": "qiyin"
    },
    {
      "question": "To‘g‘ri ketma-ketlikni tanlang:",
      "options": ["I", "take", "a shower", "every morning"],
      "correct": [0, 1, 2, 3],
      "level": "qiyin"
    },
    {
      "question": "Gapni to‘g‘ri tuzing:",
      "options": ["She", "speaks", "three languages"],
      "correct": [0, 1, 2],
      "level": "qiyin"
    },
    {
      "question": "Quyidagi so‘zlarni tartib bilan joylashtiring:",
      "options": ["They", "don't", "like", "cold weather"],
      "correct": [0, 1, 2, 3],
      "level": "qiyin"
    },
    {
      "question": "To‘g‘ri tartibni tanlang:",
      "options": ["My sister", "studies", "at university"],
      "correct": [0, 1, 2],
      "level": "qiyin"
    },
    {
      "question": "Gap tuzilishini tanlang:",
      "options": ["We", "often", "go", "for a walk", "in the park"],
      "correct": [0, 1, 2, 3, 4],
      "level": "qiyin"
    },
    {
      "question": "To‘g‘ri javobni belgilang:",
      "options": ["He", "doesn't", "drink", "coffee"],
      "correct": [0, 1, 2, 3],
      "level": "qiyin"
    },
    {
      "question": "So‘z bo‘laklarini to‘g‘ri joylashtiring:",
      "options": ["The shop", "opens", "at 9 a.m."],
      "correct": [0, 1, 2],
      "level": "qiyin"
    },
    {
      "question": "Tartib bilan to‘g‘ri joylashtiring:",
      "options": ["I", "always", "brush", "my teeth", "before bed"],
      "correct": [0, 1, 2, 3, 4],
      "level": "qiyin"
    }
  ]
,
  "present_continuous": [
    {
      "question": "She ___ a book now.",
      "options": ["read", "reads", "is reading", "reading"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "They ___ football at the moment.",
      "options": ["play", "plays", "are playing", "playing"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "Look! It ___.",
      "options": ["rain", "rains", "is raining", "raining"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "What ___ you ___ now?",
      "options": ["do, do", "are, doing", "is, doing", "does, do"],
      "correct": 1,
      "level": "easy"
    },
    {
      "question": "The children ___ TV now.",
      "options": ["watch", "watches", "are watching", "watching"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "Listen! Someone ___.",
      "options": ["sing", "sings", "is singing", "singing"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "She ___ her homework now.",
      "options": ["do", "does", "is doing", "doing"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "They ___ to London next week.",
      "options": ["travel", "travels", "are traveling", "traveling"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "I ___ for my exam these days.",
      "options": ["study", "studies", "am studying", "studying"],
      "correct": 2,
      "level": "easy"
    },
    {
      "question": "Why ___ you ___?",
      "options": ["do, cry", "are, crying", "is, crying", "does, cry"],
      "correct": 1,
      "level": "easy"
    },
    {
      "question": "The baby ___ right now.",
      "options": ["sleep", "sleeps", "is sleeping", "sleeping"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "We ___ dinner at the moment.",
      "options": ["have", "has", "are having", "having"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "The students ___ for the test.",
      "options": ["prepare", "prepares", "are preparing", "preparing"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "Where ___ you ___ these days?",
      "options": ["do, live", "are, living", "is, living", "does, live"],
      "correct": 1,
      "level": "medium"
    },
    {
      "question": "My phone ___ at the moment.",
      "options": ["not work", "doesn't work", "isn't working", "not working"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "The workers ___ the road this week.",
      "options": ["repair", "repairs", "are repairing", "repairing"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "Look! The dog ___ with the children.",
      "options": ["play", "plays", "is playing", "playing"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "I ___ to the radio while cooking.",
      "options": ["listen", "listens", "am listening", "listening"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "They ___ a new house these days.",
      "options": ["build", "builds", "are building", "building"],
      "correct": 2,
      "level": "medium"
    },
    {
      "question": "Why ___ he ___ so fast?",
      "options": ["do, run", "is, running", "does, run", "are, running"],
      "correct": 1,
      "level": "medium"
    },
    {
      "question": "By this time tomorrow, I ___ to New York.",
      "options": ["fly", "will fly", "am flying", "will be flying"],
      "correct": 3,
      "level": "hard"
    },
    {
      "question": "This time next week, we ___ on the beach.",
      "options": ["lie", "will lie", "are lying", "will be lying"],
      "correct": 3,
      "level": "hard"
    },
    {
      "question": "Don't call at 8 PM - I ___ my online class then.",
      "options": ["have", "am having", "will have", "will be having"],
      "correct": 3,
      "level": "hard"
    },
    {
      "question": "While you ___ dinner tonight, I ___ my presentation.",
      "options": ["prepare, will practice", "are preparing, will be practicing", "prepare, am practicing", "are preparing, practice"],
      "correct": 1,
      "level": "hard"
    },
    {
      "question": "At midnight last night, I ___ still ___ my assignment.",
      "options": ["am, working", "was, working", "was, worked", "am, worked"],
      "correct": 1,
      "level": "hard"
    },
    {
      "question": "She ___ her degree when the pandemic started.",
      "options": ["is completing", "was completing", "completed", "completes"],
      "correct": 1,
      "level": "hard"
    },
    {
      "question": "The team ___ on this project since January.",
      "options": ["works", "is working", "has been working", "worked"],
      "correct": 2,
      "level": "hard"
    },
    {
      "question": "I ___ TV when suddenly the lights went out.",
      "options": ["watch", "watched", "was watching", "am watching"],
      "correct": 2,
      "level": "hard"
    },
    {
      "question": "They ___ dinner when we arrived.",
      "options": ["have", "had", "were having", "are having"],
      "correct": 2,
      "level": "hard"
    },
    {
      "question": "What ___ you ___ when I called you yesterday?",
      "options": ["do, do", "were, doing", "did, do", "are, doing"],
      "correct": 1,
      "level": "hard"
    }
  ] 
,




    
"past_simple": [
    {
        "question": "She ___ to Paris last year.",
        "options": ["go", "goes", "went", "gone"],
        "correct": 2
    },
    {
        "question": "They ___ a new car yesterday.",
        "options": ["buy", "buys", "bought", "buying"],
        "correct": 2
    },
    {
        "question": "He ___ his homework an hour ago.",
        "options": ["finish", "finishes", "finished", "finishing"],
        "correct": 2
    },
    {
        "question": "___ you see that movie last night?",
        "options": ["Do", "Does", "Did", "Are"],
        "correct": 2
    },
    {
        "question": "We ___ dinner at 8 pm yesterday.",
        "options": ["have", "has", "had", "having"],
        "correct": 2
    },
    {
        "question": "The sun ___ at 6 am yesterday.",
        "options": ["rise", "rises", "rose", "rising"],
        "correct": 2
    },
    {
        "question": "She ___ her keys this morning.",
        "options": ["lose", "loses", "lost", "losing"],
        "correct": 2
    },
    {
        "question": "I ___ a letter to my friend last week.",
        "options": ["write", "writes", "wrote", "written"],
        "correct": 2
    },
    {
        "question": "They ___ home late last night.",
        "options": ["come", "comes", "came", "coming"],
        "correct": 2
    },
    {
        "question": "He ___ his breakfast quickly.",
        "options": ["eat", "eats", "ate", "eating"],
        "correct": 2
    },
    {
        "question": "We ___ very tired after the trip.",
        "options": ["are", "were", "was", "is"],
        "correct": 1
    },
    {
        "question": "Shakespeare ___ many famous plays.",
        "options": ["write", "writes", "wrote", "written"],
        "correct": 2
    },
    {
        "question": "___ they visit you last summer?",
        "options": ["Do", "Does", "Did", "Are"],
        "correct": 2
    },
    {
        "question": "The war ___ in 1945.",
        "options": ["end", "ends", "ended", "ending"],
        "correct": 2
    },
    {
        "question": "She ___ her arm when she fell.",
        "options": ["break", "breaks", "broke", "broken"],
        "correct": 2
    },
    {
        "question": "I ___ my wallet at the restaurant.",
        "options": ["leave", "leaves", "left", "leaving"],
        "correct": 2
    },
    {
        "question": "They ___ married in 2010.",
        "options": ["get", "gets", "got", "gotten"],
        "correct": 2
    },
    {
        "question": "The phone ___ while I was sleeping.",
        "options": ["ring", "rings", "rang", "rung"],
        "correct": 2
    },
    {
        "question": "We ___ a great time at the party.",
        "options": ["have", "has", "had", "having"],
        "correct": 2
    },
    {
        "question": "He ___ me a beautiful gift.",
        "options": ["give", "gives", "gave", "given"],
        "correct": 2
    }
]
,
"past_continuous": [
    {
        "question": "She ___ TV when I called.",
        "options": ["watch", "watched", "was watching", "were watching"],
        "correct": 2
    },
    {
        "question": "They ___ football at 5 pm yesterday.",
        "options": ["play", "played", "were playing", "was playing"],
        "correct": 2
    },
    {
        "question": "What ___ you ___ when the phone rang?",
        "options": ["was, doing", "were, doing", "did, do", "do, do"],
        "correct": 1
    },
    {
        "question": "I ___ a book when you called.",
        "options": ["read", "reads", "was reading", "were reading"],
        "correct": 2
    },
    {
        "question": "The children ___ when the teacher came in.",
        "options": ["talk", "talks", "were talking", "was talking"],
        "correct": 2
    },
    {
        "question": "He ___ his car when the accident happened.",
        "options": ["drive", "drives", "was driving", "were driving"],
        "correct": 2
    },
    {
        "question": "We ___ dinner when the guests arrived.",
        "options": ["have", "has", "were having", "was having"],
        "correct": 2
    },
    {
        "question": "She ___ a shower when the doorbell rang.",
        "options": ["take", "takes", "was taking", "were taking"],
        "correct": 2
    },
    {
        "question": "They ___ to music when I saw them.",
        "options": ["listen", "listens", "were listening", "was listening"],
        "correct": 2
    },
    {
        "question": "The sun ___ when I woke up.",
        "options": ["shine", "shines", "was shining", "were shining"],
        "correct": 2
    },
    {
        "question": "I ___ my homework when the lights went out.",
        "options": ["do", "did", "was doing", "were doing"],
        "correct": 2
    },
    {
        "question": "The students ___ while the teacher was explaining.",
        "options": ["talk", "talked", "were talking", "was talking"],
        "correct": 2
    },
    {
        "question": "What ___ you ___ at 8 pm yesterday?",
        "options": ["were, doing", "was, doing", "did, do", "do, do"],
        "correct": 0
    },
    {
        "question": "The phone ___ while I was cooking.",
        "options": ["ring", "rang", "was ringing", "were ringing"],
        "correct": 2
    },
    {
        "question": "She ___ when I entered the room.",
        "options": ["cry", "cried", "was crying", "were crying"],
        "correct": 2
    },
    {
        "question": "We ___ the news when the power failed.",
        "options": ["watch", "watched", "were watching", "was watching"],
        "correct": 2
    },
    {
        "question": "The birds ___ when I left home.",
        "options": ["sing", "sang", "were singing", "was singing"],
        "correct": 2
    },
    {
        "question": "He ___ a letter when his pen broke.",
        "options": ["write", "wrote", "was writing", "were writing"],
        "correct": 2
    },
    {
        "question": "They ___ about their future plans when I joined them.",
        "options": ["talk", "talked", "were talking", "was talking"],
        "correct": 2
    },
    {
        "question": "I ___ to work when I met my old friend.",
        "options": ["walk", "walked", "was walking", "were walking"],
        "correct": 2
    }
]
,
"future_simple": [
    {
        "question": "She ___ to London next month.",
        "options": ["travel", "travels", "will travel", "is traveling"],
        "correct": 2
    },
    {
        "question": "They ___ a new house next year.",
        "options": ["buy", "buys", "will buy", "are buying"],
        "correct": 2
    },
    {
        "question": "I think it ___ tomorrow.",
        "options": ["rain", "rains", "will rain", "is raining"],
        "correct": 2
    },
    {
        "question": "___ you help me with this?",
        "options": ["Do", "Does", "Will", "Are"],
        "correct": 2
    },
    {
        "question": "We ___ the exam next week.",
        "options": ["take", "takes", "will take", "are taking"],
        "correct": 2
    },
    {
        "question": "He ___ 18 next month.",
        "options": ["be", "is", "will be", "are"],
        "correct": 2
    },
    {
        "question": "I promise I ___ late.",
        "options": ["not be", "won't be", "am not", "not"],
        "correct": 1
    },
    {
        "question": "They ___ at 8 am tomorrow.",
        "options": ["arrive", "arrives", "will arrive", "are arriving"],
        "correct": 2
    },
    {
        "question": "She ___ a doctor when she grows up.",
        "options": ["become", "becomes", "will become", "is becoming"],
        "correct": 2
    },
    {
        "question": "___ you marry me?",
        "options": ["Do", "Does", "Will", "Are"],
        "correct": 2
    },
    {
        "question": "I'm sure you ___ the test.",
        "options": ["pass", "passes", "will pass", "are passing"],
        "correct": 2
    },
    {
        "question": "They ___ probably ___ late.",
        "options": ["will, be", "are, being", "do, be", "does, be"],
        "correct": 0
    },
    {
        "question": "What ___ you ___ after graduation?",
        "options": ["do, do", "will, do", "are, doing", "does, do"],
        "correct": 1
    },
    {
        "question": "The meeting ___ at 3 pm tomorrow.",
        "options": ["start", "starts", "will start", "is starting"],
        "correct": 2
    },
    {
        "question": "I hope the weather ___ nice for our picnic.",
        "options": ["is", "will be", "be", "are"],
        "correct": 1
    },
    {
        "question": "She ___ definitely ___ to the party.",
        "options": ["will, come", "is, coming", "does, come", "do, come"],
        "correct": 0
    },
    {
        "question": "We ___ our grandparents this weekend.",
        "options": ["visit", "visits", "will visit", "are visiting"],
        "correct": 2
    },
    {
        "question": "The train ___ in ten minutes.",
        "options": ["leave", "leaves", "will leave", "is leaving"],
        "correct": 2
    },
    {
        "question": "___ they finish the project on time?",
        "options": ["Do", "Does", "Will", "Are"],
        "correct": 2
    },
    {
        "question": "I ___ you as soon as I arrive.",
        "options": ["call", "calls", "will call", "am calling"],
        "correct": 2
    }
]
,
"future_continuous": [
    {
        "question": "This time tomorrow, I ___ on the beach.",
        "options": ["lie", "will lie", "will be lying", "am lying"],
        "correct": 2
    },
    {
        "question": "At 8 pm tonight, they ___ dinner.",
        "options": ["have", "will have", "will be having", "are having"],
        "correct": 2
    },
    {
        "question": "Don't call at 9 - I ___ my favorite show.",
        "options": ["watch", "will watch", "will be watching", "am watching"],
        "correct": 2
    },
    {
        "question": "What ___ you ___ this time next week?",
        "options": ["will, do", "are, doing", "will, be doing", "do, do"],
        "correct": 2
    },
    {
        "question": "She ___ for her exam all day tomorrow.",
        "options": ["study", "will study", "will be studying", "is studying"],
        "correct": 2
    },
    {
        "question": "They ___ to Paris this time next month.",
        "options": ["fly", "will fly", "will be flying", "are flying"],
        "correct": 2
    },
    {
        "question": "We ___ a meeting at 10 am tomorrow.",
        "options": ["have", "will have", "will be having", "are having"],
        "correct": 2
    },
    {
        "question": "He ___ his car at 5 pm tomorrow.",
        "options": ["wash", "will wash", "will be washing", "is washing"],
        "correct": 2
    },
    {
        "question": "The sun ___ when we wake up tomorrow.",
        "options": ["shine", "will shine", "will be shining", "is shining"],
        "correct": 2
    },
    {
        "question": "I ___ TV at this time tomorrow.",
        "options": ["watch", "will watch", "will be watching", "am watching"],
        "correct": 2
    },
    {
        "question": "At midnight tonight, we ___ soundly.",
        "options": ["sleep", "will sleep", "will be sleeping", "are sleeping"],
        "correct": 2
    },
    {
        "question": "This time next year, I ___ at university.",
        "options": ["study", "will study", "will be studying", "am studying"],
        "correct": 2
    },
    {
        "question": "The workers ___ the road all day tomorrow.",
        "options": ["repair", "will repair", "will be repairing", "are repairing"],
        "correct": 2
    },
    {
        "question": "What ___ she ___ at 3 pm tomorrow?",
        "options": ["will, do", "is, doing", "will, be doing", "does, do"],
        "correct": 2
    },
    {
        "question": "The plane ___ over the Atlantic at this time tomorrow.",
        "options": ["fly", "will fly", "will be flying", "is flying"],
        "correct": 2
    },
    {
        "question": "They ___ their anniversary all evening.",
        "options": ["celebrate", "will celebrate", "will be celebrating", "are celebrating"],
        "correct": 2
    },
    {
        "question": "I ___ for you at the station when your train arrives.",
        "options": ["wait", "will wait", "will be waiting", "am waiting"],
        "correct": 2
    },
    {
        "question": "The kids ___ in the pool all afternoon.",
        "options": ["swim", "will swim", "will be swimming", "are swimming"],
        "correct": 2
    },
    {
        "question": "At 7 am tomorrow, I ___ to work.",
        "options": ["drive", "will drive", "will be driving", "am driving"],
        "correct": 2
    },
    {
        "question": "The chef ___ a special dish for the guests at this time tomorrow.",
        "options": ["prepare", "will prepare", "will be preparing", "is preparing"],
        "correct": 2
    }
]
}
# Foydalanuvchi ma'lumotlari
user_data = {}
ratings = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧠❤️👀 State Verbs"),  KeyboardButton(text="📚 English Lessons")],
            [KeyboardButton(text="📜 Preposition Verbs"), KeyboardButton(text="🌟 Irregular Verbs")],
            [KeyboardButton(text="⏳ English Tenses"),    KeyboardButton(text="👤 Profil")],  
            [KeyboardButton(text="📈 Reyting"),           KeyboardButton(text="📞 Adminga murojaat")],
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
            [KeyboardButton(text="♻️ Barcha Preposition Verbs")],
            [KeyboardButton(text="⬅️ Ortga")],
        ],
        resize_keyboard=True
    )

    await message.answer(
        "📜 *Preposition Verbs testlaridan birini tanlang:*\n\n"
        "📌 *Asosiy fe’llar:*\n"
        "1️⃣ P verb 1 - Eng ko‘p ishlatiladigan preposition verbs\n\n"
        "📌 *Qo‘shimcha fe’llar:*\n"
        "2️⃣ P verb 2 - Ko‘proq ishlatiladigan preposition verbs\n\n"
        "📌 *Kengaytirilgan fe’llar:*\n"
        "3️⃣ P verb 3 - Qo‘shimcha va murakkab preposition verbs\n\n"
        "📌 *Murakkab fe’llar:*\n"
        "4️⃣ P verb 4 - Kam uchraydigan va qiyin preposition verbs\n\n"
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


@dp.message(lambda message: message.text == "⏳ English Tenses")
async def show_tenses_menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⏳ Present Simple"), KeyboardButton(text="⏳ Present Continuous")],
            [KeyboardButton(text="⏳ Present Perfect"), KeyboardButton(text="⏳ Present Perfect Cont.")],
            [KeyboardButton(text="⏳ Past Simple"), KeyboardButton(text="⏳ Past Continuous")],
            [KeyboardButton(text="⏳ Past Perfect"), KeyboardButton(text="⏳ Past Perfect Cont.")],
            [KeyboardButton(text="⏳ Future Simple"), KeyboardButton(text="⏳ Future Continuous")],
            [KeyboardButton(text="⏳ Future Perfect"), KeyboardButton(text="⏳ Future Perfect Cont.")],
            [KeyboardButton(text="♻️ Barcha Tenses")],
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
@dp.message(lambda message: message.text == "3️⃣ Quantifiers")
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
    "📜 P verb 1", "📜 P verb 2", "📜 P verb 3", "📜 P verb 4",
    "🌟 I verb 1", "🌟 I verb 2", "🌟 I verb 3", "🌟 I verb 4", "🌟 I verb 5", "🌟 I verb 6", "🌟 I verb All",
    "⏳ Present Simple", "⏳ Present Continuous", "⏳ Present Perfect", "⏳ Present Perfect Cont.",
    "⏳ Past Simple", "⏳ Past Continuous", "⏳ Past Perfect", "⏳ Past Perfect Cont.",
    "⏳ Future Simple", "⏳ Future Continuous", "⏳ Future Perfect", "⏳ Future Perfect Cont.",
    "♻️ Barcha Tenses", "♻️ Barcha Preposition Verbs", "♻️ Barcha Irregular Verbs"
])
async def start_quiz(message: types.Message):
    try:
        user_id = message.from_user.id
        subjects_map = {
            "🧠❤️👀 State Verbs": "state",
            "📜 P verb 1": "p_verb_1",
            "📜 P verb 2": "p_verb_2",
            "📜 P verb 3": "p_verb_3",
            "📜 P verb 4": "p_verb_4",
            "🌟 I verb 1": "irregular_verbs_1",
            "🌟 I verb 2": "irregular_verbs_2",
            "🌟 I verb 3": "irregular_verbs_3",
            "🌟 I verb 4": "irregular_verbs_4",
            "🌟 I verb 5": "irregular_verbs_5",
            "🌟 I verb 6": "irregular_verbs_6",
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
            "♻️ Barcha Tenses": "all_tenses",
            "♻️ Barcha Preposition Verbs": "all_preposition_verbs",
            "♻️ Barcha Irregular Verbs": "all_irregular_verbs"
        }
        
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
        
        # Initialize subject data if not exists
        if subject not in user_data[user_id]["subjects"]:
            user_data[user_id]["subjects"][subject] = {
                "correct": 0,
                "wrong": 0,
                "total": 0,
                "current_index": 0,
                "attempts": 0
            }
        
        # Reset quiz progress if starting new quiz
        user_data[user_id]["all_quizzes"] = quizzes[subject].copy()
        user_data[user_id]["subjects"][subject]["current_index"] = 0
        user_data[user_id]["subjects"][subject]["attempts"] += 1
        user_data[user_id]["start_time"] = time.time()
        
        await message.answer(
            f"📢 {message.text} testi boshlandi!\n\n"
            f"ℹ️ Har bir savolga 1 daqiqa vaqt beriladi!\n"
            f"🔢 Jami savollar: {len(quizzes[subject])} ta",
            reply_markup=types.ReplyKeyboardRemove()
        )
        await send_next_question(user_id, subject, message.text)
        
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
            open_period=60  # 1 minute time limit
        )
        
        user_info["current_poll"]["poll_id"] = poll_msg.poll.id
        
    except Exception as e:
        logging.error(f"Error in send_next_question: {e}")
        await bot.send_message(user_id, "❌ Savol yuborishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

async def show_quiz_results(user_id: int, subject: str, quiz_name: str, subject_info: dict):
    try:
        # Calculate time taken
        time_taken = int(time.time() - user_data[user_id]["start_time"])
        minutes = time_taken // 60
        seconds = time_taken % 60
        
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
        
        # Check if answer is too late (after 1 minute)
        if time.time() - poll_data.get("start_time", 0) > 65:  # 5 second buffer
            await bot.send_message(user_id, "⏰ Vaqt tugadi! Keyingi savolga o'tamiz.")
            user_info["subjects"][poll_data["subject"]]["wrong"] += 1
            user_info["subjects"][poll_data["subject"]]["total"] += 1
            user_info["subjects"][poll_data["subject"]]["current_index"] += 1
            await send_next_question(user_id, poll_data["subject"], poll_data["quiz_name"])
            return
        
        # Validate answer
        if not poll_answer.option_ids:
            return
        
        selected_option = poll_answer.option_ids[0]
        subject = poll_data["subject"]
        correct_option = poll_data["correct_option"]
        question_index = poll_data["question_index"]
        quiz_name = poll_data["quiz_name"]
        
        # Get current question data
        question_data = user_info["all_quizzes"][question_index]
        correct_answer = question_data["options"][question_data["correct"]]
        
        # Update scores
        if selected_option == correct_option:
            user_info["subjects"][subject]["correct"] += 1
            user_info["score"] += 1
            feedback = "✅ To'g'ri javob!"
        else:
            feedback = f"❌ Noto'g'ri javob! To'g'ri javob: {correct_answer}"
            user_info["subjects"][subject]["wrong"] += 1
        
        user_info["subjects"][subject]["total"] += 1
        user_info["subjects"][subject]["current_index"] += 1
        
        await bot.send_message(user_id, feedback)
        await send_next_question(user_id, subject, quiz_name)
        
    except Exception as e:
        logging.error(f"Error in handle_poll_answer: {e}")
        if user_id in user_data:
            await bot.send_message(user_id, "❌ Javoblarni qayta ishlashda xatolik yuz berdi.")


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
