from pyrogram import Client, Filters, Emoji
from pyrogram.errors import RPCError, FloodWait, MessageEditTimeExpired
import threading
import schedule
import time
import random
import re
import json

app = Client( 
"Userbot"
)

running = True

def startJob():
    while running==True:
        schedule.run_pending()
        time.sleep(1)

def aggiornaGiorno():
    giocatori[utente]["giorni"] += 1
    SaveJson("traduzioni.json",risorsePers)

gruppi = [-1001100753533,-1001179969920]
liste = [-1001144479124]

def messaggioSapiens():
    messaggio = app.iter_history(-1001483265011)
    messaggio = random.choice(list(messaggio))
    messaggio.delete()
    messaggio.forward("sapiens3",as_copy = True)

def conteggioSettimanale():
    for utente in giocatori:
        giocatori[utente]["conteggioSettimanale"] = 0

f = open("programma.txt")
programma = f.read()
if programma == "True":
    app.send_message("Anatras02","Ho avviato il bot, e la programmazione è attiva!")
    schedule.every().day.at("15:00").do(messaggioSapiens).tag("sapiensTag")
    schedule.every().day.at("20:00").do(messaggioSapiens).tag("sapiensTag")
f.close()

schedule.every().monday.do(conteggioSettimanale)


def pubblicità():
    membri = app.get_chat_members_count("sapiens3")
    messaggio = "#cercosponsor\n"+"🧠 🧠 🧠 🧠🧠🧠\n"+"🧠 @sapiens3\n"+f"🧠 👥 {membri}\n"+"🧠 👀 4000 / 24h\n"+"🧠 🧠 🧠 🧠🧠 🧠\n"+ "⛔️Clickbait\n"+"\n\n"+"#vendosponsor\n"+"🕒 15.01 - 20.01\n"+"💵 7€\n"+"🕒 21.00 - 10.00\n"+"💵 5€\n"+"\n"+"❗️ @SponsorBot ❗️\n"+"\n"+"ℹ️ @Sapiens3UserBot"
    for gruppo in gruppi:
        try:
            app.send_message(gruppo,messaggio)
        except RPCError as e:
            print(e)
            continue
def prenotazioneFly():
    messaggioListaFly = " 🧠CURIOSITÀ E SCIENZA 🧠 - @Sapiens3"
    for lista in liste:
        try:
            app.send_message(listaFly, messaggioListaFly)
        except RPCError as e:
            print(e)
            continue

schedule.every().saturday.at("23:50").do(prenotazioneFly)

t1 = threading.Thread(target=startJob)
t1.start()

schedule.every().saturday.at("23:50").do(prenotazioneFly)
schedule.every().day.at("10:00").do(pubblicità)
schedule.every().day.at("15:00").do(pubblicità)
schedule.every().day.at("20:00").do(pubblicità)

with open('giocatori.json', 'r') as fp:
    giocatori = json.load(fp)

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

@app.on_message(Filters.command(["ita"]), group = 1)
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

@app.on_message(Filters.command(["link"]) & Filters.me, group = 1)
def link(client,message):
    message.delete()
    messaggio = (
        "Link delle chat per i traduttori:\n\n"
        "Sapiens ENG, da cui prendere il materiale da tradurre:\n"
        "t.me/joinchat/AItIX0g7FrpzrfncYF06vQ \n\n"
        "Sapiens Beta, in cui postare il materiale una volta tradotto:\n"
        "t.me/joinchat/AAAAAEZl0oC2n8wrha268A"
        )
    app.send_message(message.chat.id,messaggio,disable_web_page_preview = True)

@app.on_message(Filters.command(["programma"]) & Filters.user(["Anatras02","Sapiens3UserBot"]), group = 1)
def programmaFunc(_,message):
    global programma
    try:
        flag = message.command[1]
    except IndexError:
        flag = None

    if flag == None:
        if programma == "True":
            message.reply("La programmazione è attiva\n\nPer attivarla usa il comando `/programma disattiva`")
            return
        if programma == "False":
            message.reply("La programmazione è disabilitata\n\nPer disattivarla usa il comando `/programma attiva`")
            return

    if flag.lower() == "attiva":
        programma = "True"
        message.reply("Programmazione attivata!")
        schedule.every().day.at("15:00").do(messaggioSapiens).tag("sapiensTag")
        schedule.every().day.at("20:00").do(messaggioSapiens).tag("sapiensTag")
    elif flag.lower() == "disattiva":
        programma = "False"
        schedule.clear('sapiensTag')
        message.reply("Programmazione disattivata!")
    else:
        message.reply("Tag validi: `attiva`,`disattiva`,`vuoto`")

    f = open("programma.txt", "w")
    f.write(str(programma))
    f.close()

@app.on_message(Filters.command(["fixAll"]) & Filters.user(["Anatras02","Sapiens3UserBot","EmeraldBot"]), group = 1)
def fixAll(_,message):
    rx = r'([^ ]+) - (http.+)'
    messaggi = app.iter_history(-1001169693822)

    for messaggio in messaggi:
        testo = ""
        regex = False
        try:
            messaggioText = messaggio.caption.markdown.split("\n")
        except AttributeError:
            pass
        for line in messaggioText:
            mo = re.match(rx,line)
            if mo:
                index = messaggioText.index(line)
                resto = "\n".join(messaggioText[:index])
                fine = "\n".join(messaggioText[index+1:])
                testo = resto + f"\n[📚 {mo.group(1)}]({mo.group(2)})\n" + fine
                regex = True

        if regex == True:
            time.sleep(5)
            try:
                messaggioEditato = messaggio.edit_caption(testo)
                messaggioEditato.forward(-1001181078144, as_copy = True)
                messaggioEditato.delete()
            except FloodWait as e:
                print("Flood Wait:",e.x)
                time.sleep(e.x)
                messaggioEditato = messaggio.edit_caption(testo)
                messaggioEditato.forward(-1001181078144, as_copy = True)
                messaggioEditato.delete()
    message.reply("Finito!")

@app.on_message(Filters.command(["id"]))
def id(_,message):
    message.reply(message.chat.id)

def SaveJson(fileName,dictName):
    with open(fileName, 'w') as fp:
        json.dump(dictName, fp,sort_keys=True, indent=4)
 
@app.on_message(Filters.command(["add"]) & (Filters.user(["Anatras02","EmeraldBot","Sapiens3UserBot","ClaireClok"]) | Filters.channel), group = 1)
def add(_,message):
    rx = r'/add (\d+)?\s?@?(\w+)'
    mo = re.match(rx,message.text)

    if mo:
        utente = mo.group(2)
        if utente not in giocatori:
            giocatori[utente] = dict()
            giocatori[utente]["andamento"] = 0 
            giocatori[utente]["giorni"] = 0 
            giocatori[utente]["andamentoSettimanale"] = 0 
            schedule.every().monday.do(conteggioSettimanale)

        if mo.group(1) == None:
            giocatori[utente]["andamento"] += 1
            giocatori[utente]["andamentoSettimanale"] += 1
        else:
            giocatori[utente]["andamento"] += int(mo.group(1))
            giocatori[utente]["andamentoSettimanale"] += int(mo.group(1))

        message.reply(f"**{mo.group(2)}** dall'inizio ha fatto **{giocatori[utente]['andamento']}** traduzioni\nQuesta settimana ha fatto **{giocatori[utente]['andamentoSettimanale']}** traduzioni")
        SaveJson("giocatori.json",giocatori)
    else:
        message.reply("Sintassi non valida\n\n`/add (numero) username`\nIl numero è facoltativo")

@app.on_message(Filters.command(["counter"]) & (Filters.user(["Anatras02","EmeraldBot","Sapiens3UserBot"]) | Filters.channel), group = 1)
def add(_,message):
    andamentoSettimanale = "**Andamento Settimanale**\n"
    andamentoTotale = "**Anamento Totale**\n"
    for utente in giocatori:
        andamentoSettimanale += f'{utente} - {giocatori[utente]["andamentoSettimanale"]}\n'
        andamentoTotale += f'{utente} - {giocatori[utente]["andamento"]}\n'

    app.send_message(message.chat.id,andamentoSettimanale+"\n"+andamentoTotale)

app.run()

running = False
t1.join()

