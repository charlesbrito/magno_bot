import os
from dotenv import load_dotenv
from datetime import datetime
from telegram import Update
from logica.crud import criar_cliente, criar_aposta, listar_apostas, listar_por_time, listar_por_resultado
from telegram.ext import ContextTypes, CommandHandler

load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")

# Cadastrar Cliente
async def cadastrar_cliente(update: Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        nome = context.args[0]
        email = context.args [1]
        banca = float(context.args[2])
        telegram_id = update.effective_user.id
        cliente = criar_cliente(nome, email, banca, telegram_id)
        await update.message.reply_text(f"✅Cliente {cliente.nome} cadastrado com sucesso")
    except Exception as e:
        await update.message.reply_text(f"Erro ao cadastrar:{e}")

# Cadastrar Apostas
async def cadastrar_aposta(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        evento = context.args[0]
        data_evento = datetime.strptime(context.args[1], '%d-%m-%Y')
        tipo_aposta = context.args[2]
        valor_apostado = float(context.args[3])
        odd = float(context.args[4])
        possivel_retorno = odd * valor_apostado
        resultado = context.args[5]
        telegram_id = update.effective_user.id
        aposta = criar_aposta(evento,data_evento,tipo_aposta,valor_apostado,odd,possivel_retorno,resultado,telegram_id)
        await update.message.reply_text(f"✅Aposta {aposta.evento} criada com sucesso")
    except Exception as e:
        await update.message.reply_text(f"erro:{e}")

# Listar minhas apostas
async def minhas_apostas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        telegram_id = update.effective_user.id
        apostas = listar_apostas(telegram_id)

        if not apostas:
            await update.message.reply_text("Você não tem nenhuma aposta cadastrada")
            return

        for aposta in apostas:
            texto = (
                f"📝 Aposta Registrada\n\n"
                f"Jogo: {aposta.evento}\n"
                f"Data do Evento: {aposta.data_evento.strftime('%d/%m/%Y') if aposta.data_evento else '---'}\n"
                f"Tipo da Aposta: {aposta.tipo_aposta}\n"
                f"Valor Apostado: R$ {aposta.valor_apostado:.2f}\n"
                f"Odd: {aposta.odd}\n"
                f"Possível Retorno: R$ {aposta.possivel_retorno:.2f}\n"
                f"Resultado: {aposta.resultado}\n"
                f"Data de Registro: {aposta.data_aposta.strftime('%d/%m/%Y') if aposta.data_aposta else '---'}\n"
            )
            await update.message.reply_text(texto)

    except Exception as e:
        await update.message.reply_text(f"Erro ao listar apostas: {e}")

#Listar por time
async def listar_ap_por_time(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        telegram_id = update.effective_user.id
        time = listar_por_time(telegram_id, context.args[0])

        if not time:
            await update.message.reply_text("Você não tem nenhuma aposta cadastrada")
            return
        
        for aposta in time:
            texto = (
                f"📝 Aposta Registrada\n\n"
                f"Jogo: {aposta.evento}\n"
                f"Data do Evento: {aposta.data_evento.strftime('%d/%m/%Y') if aposta.data_evento else '---'}\n"
                f"Tipo da Aposta: {aposta.tipo_aposta}\n"
                f"Valor Apostado: R$ {aposta.valor_apostado:.2f}\n"
                f"Odd: {aposta.odd}\n"
                f"Possível Retorno: R$ {aposta.possivel_retorno:.2f}\n"
                f"Resultado: {aposta.resultado}\n"
                f"Data de Registro: {aposta.data_aposta.strftime('%d/%m/%Y') if aposta.data_aposta else '---'}\n"
            )
            await update.message.reply_text(texto)

    except Exception as e:
        await update.message.reply_text(f"Erro ao listar apostas: {e}")

async def listar_ap_por_resultado(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try:
        telegram_id = update.effective_user.id
        resultado_1 = listar_por_resultado(telegram_id, context.args[0])

        if not resultado_1:
            await update.message.reply_text("Você não tem nenhuma aposta cadastrada")
            return
        
        for aposta in resultado_1:
            texto = (
                f"📝 Aposta Registrada\n\n"
                f"Jogo: {aposta.evento}\n"
                f"Data do Evento: {aposta.data_evento.strftime('%d/%m/%Y') if aposta.data_evento else '---'}\n"
                f"Tipo da Aposta: {aposta.tipo_aposta}\n"
                f"Valor Apostado: R$ {aposta.valor_apostado:.2f}\n"
                f"Odd: {aposta.odd}\n"
                f"Possível Retorno: R$ {aposta.possivel_retorno:.2f}\n"
                f"Resultado: {aposta.resultado}\n"
                f"Data de Registro: {aposta.data_aposta.strftime('%d/%m/%Y') if aposta.data_aposta else '---'}\n"
            )
            await update.message.reply_text(texto)

    except Exception as e:
        await update.message.reply_text(f"Erro ao listar apostas: {e}")




cadastrar_handler = CommandHandler("cadastrar", cadastrar_cliente)
cadastrar_aposta_handler = CommandHandler("cad_aposta", cadastrar_aposta)
minhas_apostas_handler = CommandHandler("minhas_apostas", minhas_apostas)
listar_ap_por_time_handler = CommandHandler("listar_p_time", listar_ap_por_time)
listar_por_resultado_handler = CommandHandler("listar_p_resul", listar_ap_por_resultado)