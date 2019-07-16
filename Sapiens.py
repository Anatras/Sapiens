from pyrogram import Client, Filters, Emoji
from pyrogram.errors import RPCError
import threading
import schedule
import time

app = Client( 
"Userbot"
)



running = True

def startJob():
    while running==True:
        schedule.run_pending()
        time.sleep(1)

gruppi = [-1001100753533]

def pubblicità():
    membri = app.get_chat_members_count("sapiens3")
    messaggio = "#cercosponsor\n"+"🧠 🧠 🧠 🧠🧠🧠\n"+"🧠 @sapiens3\n"+f"🧠 👥 {membri}\n"+"🧠 👀 4000 / 24h\n"+"🧠 🧠 🧠 🧠🧠 🧠\n"+ "⛔️Clickbait\n"+"\n\n"+"#vendosponsor\n"+"🕒 15.01 - 20.01\n"+"💵 7€\n"+"🕒 21.00 - 10.00\n"+"💵 5€\n"+"\n"+"❗️ @SponsorBot ❗️\n"+"\n"+"ℹ️ @SapiensUserBot"
    for gruppo in gruppi:
        try:
            app.send_message(gruppo,messaggio)
        except RPCError as e:
            print(e)
            continue

t1 = threading.Thread(target=startJob)
t1.start()

schedule.every().day.at("10:00").do(pubblicità)
schedule.every().day.at("15:00").do(pubblicità)
schedule.every().day.at("20:00").do(pubblicità)

@app.on_message(Filters.private & ~Filters.me)
def first_msg(client, message):
    if app.get_history_count(message.chat.id) <= 2:
        message = message.reply("Collegamento alla chat di supporto di Sapiens³..")
        time.sleep(4)
        message.edit("Collegamento effettuato!")
        time.sleep(2)
        message.edit("🧠 Benvenuto nella chat di supporto di Sapiens³, un amministratore risponderà alla tua richiesta nel più breve tempo possibile")

@app.on_message(Filters.command(["form"]), group = 1)
def form(client,message):
    message.delete()
    app.send_message(message.chat.id,"🧠 Copia questo form e invialo a questa chat rispondendo alle seguenti domande:")
    messaggio = "**Da quanto tempo segui Sapiens³?** (__Settimane, Mesi, Anni__)"+"\n`R:`"+"\n\n"+"**Hai familiarità con traduzione e scrittura di testi argomentati e di carattere culturale?** (__Si, No__)"+"\n`R:`"+"\n\n"+"**Qual é il tuo livello di comprensione della lingua inglese?** (__1-10__)"+"\n`R:`"+"\n\n"+"**Qual è il numero minimo di traduzioni, della stessa lunghezza dei post pubblicati su sapiens, che garantiresti al canale settimanalmente?**  (__4-10__)"+"\n`R:`"+"\n\n"+"**Ritieni di sapere gestire e rispettare autonomamente le tempistiche per le traduzioni?** (__Si, No__)"+"\n`R:`"
    app.send_message(message.chat.id,messaggio)


app.run()

running = False
t1.join()

