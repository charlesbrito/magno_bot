from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from logica.crud import bom_dia

# Comando para boas vindas
async def boas_vindas(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Seja muito bem vindo, use o comando /cadastrar SEU NOME, SEU EMAIL, VALOR DA BANCA, para criar sua conta")

# Mensagem de bom dia 
async def m_bom_dia(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        telegram_id = update.effective_user.id
        good_dia = bom_dia(telegram_id)
        await update.message.reply_text(f"Bom dia {good_dia}")
    except Exception as e:
        await update.message.reply_text(f"Erro interno: {e}")


boas_vindas_handler = CommandHandler("start", boas_vindas)
m_bom_dia_handler = CommandHandler("Bom_dia", m_bom_dia)
