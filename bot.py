import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from comandos.cliente import cadastrar_handler, cadastrar_aposta_handler, minhas_apostas_handler, listar_ap_por_time_handler, listar_por_resultado_handler
from comandos.boasvindas import boas_vindas_handler, m_bom_dia_handler


load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")
ap = Flask(__name__)
bot = Bot(token=TOKEN_BOT)

app = ApplicationBuilder().token(TOKEN_BOT).build()
app.add_handler(cadastrar_handler)
app.add_handler(boas_vindas_handler)
app.add_handler(cadastrar_aposta_handler)
app.add_handler(minhas_apostas_handler)
app.add_handler(listar_ap_por_time_handler)
app.add_handler(m_bom_dia_handler)
app.add_handler(listar_por_resultado_handler)

@ap.router(f"/{TOKEN_BOT}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    app.update_queue.put(update)
    return "ok"
