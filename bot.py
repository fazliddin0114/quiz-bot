import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from aiogram import types, F


# BotFather tomonidan berilgan token
TOKEN = "7267797063:AAHjnlqhlLYU1rEAXf2S1VWLbKrTICagnak"  # Bu yerga haqiqiy tokenni qo'ying
ADMIN_IDS = [7871012050]  # Admin IDlari

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

"present_simple": [
    {
        "question": "She ___ to school every day.",
        "options": ["go", "goes", "going", "gone"],
        "correct": 1
    },
    {
        "question": "They ___ football on Sundays.",
        "options": ["play", "plays", "playing", "played"],
        "correct": 0
    },
    {
        "question": "He ___ not like coffee.",
        "options": ["do", "does", "doing", "done"],
        "correct": 1
    },
    {
        "question": "___ you speak English?",
        "options": ["Do", "Does", "Is", "Are"],
        "correct": 0
    },
    {
        "question": "We ___ TV in the evening.",
        "options": ["watch", "watches", "watching", "watched"],
        "correct": 0
    },
    {
        "question": "My mother ___ delicious cakes.",
        "options": ["make", "makes", "making", "made"],
        "correct": 1
    },
    {
        "question": "The sun ___ in the east.",
        "options": ["rise", "rises", "rising", "rose"],
        "correct": 1
    },
    {
        "question": "Cats ___ milk.",
        "options": ["love", "loves", "loving", "loved"],
        "correct": 0
    },
    {
        "question": "She ___ her homework every day.",
        "options": ["do", "does", "doing", "done"],
        "correct": 1
    },
    {
        "question": "I ___ breakfast at 7 am.",
        "options": ["have", "has", "having", "had"],
        "correct": 0
    },
    {
        "question": "Water ___ at 100 degrees Celsius.",
        "options": ["boil", "boils", "boiling", "boiled"],
        "correct": 1
    },
    {
        "question": "My parents ___ in a small village.",
        "options": ["live", "lives", "living", "lived"],
        "correct": 0
    },
    {
        "question": "___ your brother work here?",
        "options": ["Do", "Does", "Is", "Are"],
        "correct": 1
    },
    {
        "question": "This shop ___ at 9 o'clock every morning.",
        "options": ["open", "opens", "opening", "opened"],
        "correct": 1
    },
    {
        "question": "Birds ___ in the sky.",
        "options": ["fly", "flies", "flying", "flew"],
        "correct": 0
    },
    {
        "question": "She ___ three languages fluently.",
        "options": ["speak", "speaks", "speaking", "spoken"],
        "correct": 1
    },
    {
        "question": "We ___ our grandparents every weekend.",
        "options": ["visit", "visits", "visiting", "visited"],
        "correct": 0
    },
    {
        "question": "The train ___ at 5:30 pm.",
        "options": ["leave", "leaves", "leaving", "left"],
        "correct": 1
    },
    {
        "question": "___ they know the answer?",
        "options": ["Do", "Does", "Is", "Are"],
        "correct": 0
    },
    {
        "question": "My sister ___ as a nurse.",
        "options": ["work", "works", "working", "worked"],
        "correct": 1
    }
]

"present_continuous": [
    {
        "question": "She ___ a book now.",
        "options": ["read", "reads", "is reading", "reading"],
        "correct": 2
    },
    {
        "question": "They ___ football at the moment.",
        "options": ["play", "plays", "are playing", "playing"],
        "correct": 2
    },
    {
        "question": "Look! It ___.",
        "options": ["rain", "rains", "is raining", "raining"],
        "correct": 2
    },
    {
        "question": "What ___ you ___ now?",
        "options": ["do, do", "are, doing", "is, doing", "does, do"],
        "correct": 1
    },
    {
        "question": "The children ___ TV now.",
        "options": ["watch", "watches", "are watching", "watching"],
        "correct": 2
    },
    {
        "question": "Listen! Someone ___.",
        "options": ["sing", "sings", "is singing", "singing"],
        "correct": 2
    },
    {
        "question": "She ___ her homework now.",
        "options": ["do", "does", "is doing", "doing"],
        "correct": 2
    },
    {
        "question": "They ___ to London next week.",
        "options": ["travel", "travels", "are traveling", "traveling"],
        "correct": 2
    },
    {
        "question": "I ___ for my exam these days.",
        "options": ["study", "studies", "am studying", "studying"],
        "correct": 2
    },
    {
        "question": "Why ___ you ___?",
        "options": ["do, cry", "are, crying", "is, crying", "does, cry"],
        "correct": 1
    },
    {
        "question": "The baby ___ right now.",
        "options": ["sleep", "sleeps", "is sleeping", "sleeping"],
        "correct": 2
    },
    {
        "question": "We ___ dinner at the moment.",
        "options": ["have", "has", "are having", "having"],
        "correct": 2
    },
    {
        "question": "The students ___ for the test.",
        "options": ["prepare", "prepares", "are preparing", "preparing"],
        "correct": 2
    },
    {
        "question": "Where ___ you ___ these days?",
        "options": ["do, live", "are, living", "is, living", "does, live"],
        "correct": 1
    },
    {
        "question": "My phone ___ at the moment.",
        "options": ["not work", "doesn't work", "isn't working", "not working"],
        "correct": 2
    },
    {
        "question": "The workers ___ the road this week.",
        "options": ["repair", "repairs", "are repairing", "repairing"],
        "correct": 2
    },
    {
        "question": "Look! The dog ___ with the children.",
        "options": ["play", "plays", "is playing", "playing"],
        "correct": 2
    },
    {
        "question": "I ___ to the radio while cooking.",
        "options": ["listen", "listens", "am listening", "listening"],
        "correct": 2
    },
    {
        "question": "They ___ a new house these days.",
        "options": ["build", "builds", "are building", "building"],
        "correct": 2
    },
    {
        "question": "Why ___ he ___ so fast?",
        "options": ["do, run", "is, running", "does, run", "are, running"],
        "correct": 1
    }
]

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
ratings = {}  # Reyting tizimi

@dp.message(lambda message: message.text in [
    "🧠 State Verbs",
    "📜 P verb 1", "📜 P verb 2", "📜 P verb 3", "📜 P verb 4",
    "🌟 I verb 1", "🌟 I verb 2", "🌟 I verb 3", "🌟 I verb 4",
    "⏳ Present Simple", "⏳ Present Continuous",
    "⏳ Past Simple", "⏳ Past Continuous",
    "⏳ Future Simple", "⏳ Future Continuous",
    "♻️ Barcha Preposition Verbs", "♻️ Barcha Irregular Verbs", "♻️ Barcha Tenses"
])
async def start_quiz(message: types.Message):
    user_id = message.from_user.id
    subject_map = {
        "🧠 State Verbs": ["state"],
        "📜 P verb 1": ["p_verb_1"],
        "📜 P verb 2": ["p_verb_2"],
        "📜 P verb 3": ["p_verb_3"],
        "📜 P verb 4": ["p_verb_4"],
        "🌟 I verb 1": ["irregular_verbs_1"],
        "🌟 I verb 2": ["irregular_verbs_2"],
        "🌟 I verb 3": ["irregular_verbs_3"],
        "🌟 I verb 4": ["irregular_verbs_4"],
        "⏳ Present Simple": ["present_simple"],
        "⏳ Present Continuous": ["present_continuous"],
        "⏳ Past Simple": ["past_simple"],
        "⏳ Past Continuous": ["past_continuous"],
        "⏳ Future Simple": ["future_simple"],
        "⏳ Future Continuous": ["future_continuous"],
        "♻️ Barcha Preposition Verbs": ["p_verb_1", "p_verb_2", "p_verb_3", "p_verb_4"],
        "♻️ Barcha Irregular Verbs": ["irregular_verbs_1", "irregular_verbs_2", "irregular_verbs_3", "irregular_verbs_4"],
        "♻️ Barcha Tenses": ["present_simple", "present_continuous", "past_simple", "past_continuous", "future_simple", "future_continuous"]
    }
    
    subjects = subject_map.get(message.text)
    if not subjects:
        await message.answer("❌ Xatolik yuz berdi!")
        return

    if user_id not in user_data:
        user_data[user_id] = {"subjects": {}, "score": 0, "current_question": {}, "all_quizzes": []}
    
    # Barcha testlar uchun savollarni birlashtirish
    all_questions = []
    for subject in subjects:
        if subject not in user_data[user_id]["subjects"]:
            user_data[user_id]["subjects"][subject] = {
                "correct": 0, 
                "wrong": 0, 
                "total": 0, 
                "current_index": 0
            }
        all_questions.extend(quizzes[subject])
    
    # Agar barcha testlar tanlangan bo'lsa
    if len(subjects) > 1:
        user_data[user_id]["all_quizzes"] = all_questions
        user_data[user_id]["current_subject"] = "all"
        user_data[user_id]["subjects"]["all"] = {
            "correct": 0,
            "wrong": 0,
            "total": 0,
            "current_index": 0
        }
    
    await message.answer(f"📢 {message.text} testi boshlandi!")
    await send_next_question(user_id, subjects[0] if len(subjects) == 1 else "all", message.text)  # message.text ni qo'shdik

async def send_next_question(user_id, subject, quiz_name):  # quiz_name parametrini qo'shdik
    user_info = user_data[user_id]
    
    # Agar barcha testlar ishlanayotgan bo'lsa
    if subject == "all":
        questions = user_info["all_quizzes"]
        subject_info = user_info["subjects"]["all"]
    else:
        questions = quizzes[subject]
        subject_info = user_info["subjects"][subject]
    
    if subject_info["current_index"] >= len(questions):
        await bot.send_message(
            user_id,
            f"🎉 {quiz_name} testi tugadi! Natijangiz: {subject_info['correct']}/{subject_info['total']}"
        )
        
        sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
        user_rank = next((idx for idx, (uid, _) in enumerate(sorted_ratings, 1) if uid == user_id), None)
        await bot.send_message(user_id, f"📊 Reytingdagi o'rningiz: {user_rank}")
        
        subject_info["total"] = 0
        subject_info["correct"] = 0
        subject_info["wrong"] = 0
        subject_info["current_index"] = 0
        
        # Agar barcha testlar bo'lsa, all_quizzes ni tozalash
        if subject == "all":
            user_info["all_quizzes"] = []
        return
    
    question_data = questions[subject_info["current_index"]]
    
    shuffled_options = question_data["options"].copy()
    correct_answer = shuffled_options[question_data["correct"]]
    random.shuffle(shuffled_options)
    new_correct_index = shuffled_options.index(correct_answer)
    
    user_info["current_poll"] = {
        "poll_id": None,
        "subject": subject,
        "correct_option": new_correct_index,
        "question_index": subject_info["current_index"],
        "quiz_name": quiz_name  # quiz_name ni saqlaymiz
    }
    
    poll_msg = await bot.send_poll(
        chat_id=user_id,
        question=question_data["question"],
        options=shuffled_options,
        type="quiz",
        correct_option_id=new_correct_index,
        is_anonymous=False
    )
    
    user_info["current_poll"]["poll_id"] = poll_msg.poll.id

@dp.poll_answer()
async def handle_poll_answer(poll_answer: types.PollAnswer):
    user_id = poll_answer.user.id
    user_info = user_data.get(user_id)
    
    if not user_info or "current_poll" not in user_info:
        return
    
    selected_option = poll_answer.option_ids[0]
    subject = user_info["current_poll"]["subject"]
    correct_answer = user_info["current_poll"]["correct_option"]
    question_index = user_info["current_poll"]["question_index"]
    quiz_name = user_info["current_poll"]["quiz_name"]  # quiz_name ni olamiz
    
    # Javobni tekshirish
    if selected_option == correct_answer:
        user_info["subjects"][subject]["correct"] += 1
        user_info["score"] += 1
        feedback = "✅ To'g'ri javob!"
    else:
        if subject == "all":
            # Barcha testlar uchun to'g'ri javobni topish
            question_data = user_info["all_quizzes"][question_index]
            correct_option_text = question_data["options"][question_data["correct"]]
        else:
            correct_option_text = quizzes[subject][question_index]["options"][quizzes[subject][question_index]["correct"]]
        feedback = f"❌ Noto'g'ri javob! To'g'ri javob: {correct_option_text}"
    
    user_info["subjects"][subject]["total"] += 1
    user_info["subjects"][subject]["current_index"] += 1
    
    # Reytingni yangilash
    ratings[user_id] = user_info["score"]
    
    # Javob haqida xabar
    await bot.send_message(user_id, feedback)
    
    # Keyingi savolni yuborish
    await send_next_question(user_id, subject, quiz_name)  # quiz_name ni uzatamiz

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


# Botni ishga tushirish
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")

