
from ia import consultar_ollama
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

TOKEN = "7919086667:AAGidlGfy71eI3aVQhhkTX_R0G4ptjoLolk"
OLLAMA_URL = "http://localhost:11434/api/generate"

# función para enviar mensaje a Ollama
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


# comando /start

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy el asistente de Agrocomercial M Y M. Es un gusto que estes aqui.🤖. ¿En qué te puedo ayudar?")

# responder con IA
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    respuesta_ia = consultar_ollama(user_message)
    await update.message.reply_text(respuesta_ia)

# iniciar el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

