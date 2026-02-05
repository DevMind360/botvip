import os
import asyncio
from telegram import Bot
from datetime import datetime

TOKEN = "6731563142:AAGIpMoq-6Db3pBFlMwpiGzpvMUG16Zljc4"
CHAT_ID = "-1001728374742"  # Sostituisci con l'ID del tuo gruppo

bot = Bot(token=TOKEN)

MESSAGE = """
📺  VIP TV 📺
🔥🔥🔥TUTTO LO STREAMING E SERVIZI ON DEMAND IN UN SOLO PACCHETTO !!!🔥🔥🔥
@babbonataleamz

🔥🔥🔥PROVA GRATUTA🔥🔥🔥

PRONTO A DISDIRE TUTTI I TUOI ABBONAMENTI???

👉 Qualità 4K, FULL HD, HD, SD, 
👉 Server Estero (SICURO)
👉 1 dispositivo (2/3 su richiesta)

✅ DĪSNĒY PLUS
✅ NĒTFLĪX 
🇮🇹 SK¥ PACCHETTO FULL 
🌍 SK¥ PACCHETTO FULL ESTERI 
⚽️ DĀZN
⚽️ CHAMPIONS LEAGUE
📺 MEDĪASET PRĒMIUM FULL HD,HD,SD,+1
📡Tutti i Canali TV SAT
🏍 MOTO GP ON BOARD 
🏎 FORMULA 1 ON BOARD| CAMERA CAM
🔞 CANALI  HOTCLUB E ON DEMAND
🎥 PRIMAFILA LIVE FULL HD
👉 PRIMAFILA 
👉 CANALI TEMATICI
👉 EAGLE ITALIA
⚽️ SPORT/CALCIO/DĀZN/LEGAPRO  💎EUROPEI/MONDIALI💎
👉 ELEVEN SPORT
👉 MYSPORT
👉 SPORT INTERNAZIONALI
🖥 FULL HD, HD, SD, +1

💎 CONTATATEMI IN PRIVATO PER I PREZZI 
➖➖➖➖➖➖➖➖➖
@babbonataleamz
✅ Compatibilità con:
📱Android      📺SmartTV 
📱IOS              🖲BoxTV/FireStick
💻PC/MAC     📽ENIGMA2    

🏧 PAGAMENTI SICURI:
💳 Carta
🅿️ PayPal
🅱️ Bitcoin 

@babbonataleamz

✅ Abbiamo prezzi bomba!!✅ 
@babbonataleamz

✅Contattami per qualsisi informazione o se desideri provare gratuitamente !! ✅
"""

MESSAGE2 = """
⭐️ <b>VIP TV</b>⭐️
Vivi l’esperienza di <b>STREAMING</b> definitiva con la nostra <b>PROVA GRATUITA</b> disponibile ora! ✅

🔥PROVA subito il nostro <b>PACCHETTO COMPLETO</b>🔥Dīsnēy Plus, Nētflīx, SK¥, DĀZN, e tanto altro! 

ABBIAMO I <b>PREZZI PIU' BASSI</b> SUL MERCATO CON UNA QUALITA' IMPECCABILE!!!

@babbonataleamz
Contattami in privato per info e 
<b>PROVA GRATUITA</b>🌐💎 #Streaming #ProvaGratuita
"""

async def main():
    bot = Bot(token=TOKEN)
    minute = datetime.utcnow().minute

    if minute % 10 < 5:
        print("Invio messaggio 1...")
        await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
    else:
        print("Invio messaggio 2...")
        await bot.send_message(
            chat_id=CHAT_ID,
            text=MESSAGE2,
            parse_mode="HTML"
        )

    print("Fatto! Script terminato.")

asyncio.run(main())




