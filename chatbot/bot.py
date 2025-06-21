
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from db import fetch_products 

load_dotenv()

# Token y URL de Ollama
TOKEN = os.getenv("TELEGRAM_TOKEN", "7919086667:AAGidlGfy71eI3aVQhhkTX_R0G4ptjoLolk")
OLLAMA_URL = "http://localhost:11434/api/generate"

# Función para consultar a Ollama
def consultar_ollama(mensaje_usuario):
    prompt = f"Eres un asistente para una agrocomercial. Responde con claridad y cordialidad.\nUsuario: {mensaje_usuario}\nChatbot:"
    datos = {
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    }
    respuesta = requests.post(OLLAMA_URL, json=datos)
    if respuesta.status_code == 200:
        return respuesta.json()["response"]
    else:
        return "Lo siento, no puedo responder en este momento."

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy el asistente de Agrocomercial M Y M. Es un gusto que estés aquí 🤖. ¿En qué te puedo ayudar?")

# Manejar mensajes del usuario
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # Buscar productos en la base de datos
    productos = fetch_products(user_message)

    if productos:
        respuesta = "📦 Estos son los productos que encontré:\n"
        for nombre, categoria, descripcion, precio in productos:
            respuesta += f"• {nombre} ({categoria}): {descripcion} - L.{precio}\n"
    else:
        # Si no hay productos, responder con IA
        respuesta = consultar_ollama(user_message)

    await update.message.reply_text(respuesta)

# Iniciar el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot iniciado y en espera de mensajes...")
    app.run_polling()

