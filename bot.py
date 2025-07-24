import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from comandos.cliente import cadastrar_handler, cadastrar_aposta_handler, minhas_apostas_handler, listar_ap_por_time_handler, listar_por_resultado_handler
from comandos.boasvindas import boas_vindas_handler, m_bom_dia_handler


load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")


app = ApplicationBuilder().token(TOKEN_BOT).build()
app.add_handler(cadastrar_handler)
app.add_handler(boas_vindas_handler)
app.add_handler(cadastrar_aposta_handler)
app.add_handler(minhas_apostas_handler)
app.add_handler(listar_ap_por_time_handler)
app.add_handler(m_bom_dia_handler)
app.add_handler(listar_por_resultado_handler)
app.run_polling()
