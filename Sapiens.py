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
    messaggio = "#cercosponsor\n"+"🧠 🧠 🧠 🧠🧠🧠\n"+"🧠 @sapiens3\n"+f"🧠 👥 {membri}\n"+"🧠 👀 4000 / 24h\n"+"🧠 🧠 🧠 🧠🧠 🧠\n"+ "⛔️Clickbait\n"+"\n\n"+"#vendosponsor\n"+"🕒 15.01 - 20.01\n"+"💵 7€\n"+"🕒 21.00 - 10.00\n"+"💵 5€\n"+"\n"+"❗️ @SponsorBot ❗️\n"+"\n"+"ℹ️ @Sapiens3UserBot"
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

@app.on_message(Filters.command(["chelp"]), group = 1)
def form(client,message):
    message.delete()
    messaggio = "Scegli uno di questi link, l'unica differenza sta nell'immagine e la sua descrizione\n\n"+"t.me/chelpbot?start=resenda42627b7\n"+"t.me/chelpbot?start=resend2044eb46\n"+"t.me/chelpbot?start=resendf9c7f423\n"+"t.me/chelpbot?start=resendec5b0713\n"+"t.me/chelpbot?start=resend33d5414b\n"+"t.me/chelpbot?start=resendce779e29\n"+"t.me/chelpbot?start=resend8e73e6b1\n"+"t.me/chelpbot?start=resend0e9982f8\n"+"t.me/chelpbot?start=resend843b5558\n"+"t.me/chelpbot?start=resend7670a39a\n"
    app.send_message(message.chat.id,messaggio,disable_web_page_preview = True)

@app.on_message(Filters.command(["guida"]), group = 1)
def guida(client,message):
    message.delete()
    messaggio = (
        "LINEE GUIDA PER LA TRADUZIONE:\n\n"
        "https://telegra.ph/Linee-Guida-per-la-traduzione-06-12"
        )
    app.send_message(message.chat.id,messaggio,disable_web_page_preview = True)

@app.on_message(Filters.command(["eng"]), group = 1)
def eng(client,message):
    message.delete()
    app.send_message(message.chat.id,"TIL That women are better at discerning shades of colours, while men are better at tracking fast-moving objects and discerning detail from a distance. These are evolutionary details linked to a hunter-gatherer past.\nhttps://news.nationalgeographic.com/news/2012/09/120907-men-women-see-differently-science-health-vision-sex/", disable_web_page_preview = True)

@app.on_message(Filters.command(["it"]), group = 1)
def it(_,message):
    message.delete()
    caption = (
        "#SapeviChe\n"
        "Uomini e donne non vedono il mondo allo stesso modo: le donne sono maggiormente in grado di distinguere le varie **sfumature** dei colori, mentre gli uomini sono specializzati nella percezione dei **dettagli** da lontano e degli **oggetti in movimento**.\n\n"
        "Una ricerca del Brooklyn College (New York) dimostra che uomini e donne hanno subito un **diverso adattamento evolutivo**.\n" 
        "Gli uomini erano principalmente **cacciatori** e dovevano essere in grado di vedere le prede da lontano e in movimento; le donne invece erano **raccoglitrici** e si sono specializzate nella visione da vicino.\n\n"
        "📚 [Fonte](http://www.nationalgeographic.it/scienza/2012/09/07/news/uomini_e_donne_vedono_allo_stesso_modo_sapevatelo-1241673/)"
        )
    app.send_photo(
        message.chat.id,
        "it.jpg",
        caption = caption
        )

app.run()

running = False
t1.join()

