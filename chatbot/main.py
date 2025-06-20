from fastapi import FastAPI, Request, Form
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/telegram")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body")
    from_number = form.get("From")

    print(f"Mensaje recibido de {from_number}: {incoming_msg}")

    resp = MessagingResponse()
    msg = resp.message()

    # Respuesta simple
    respuesta = f"Hola! Recibí tu mensaje: '{incoming_msg}'. Gracias por escribir."

    msg.body(respuesta)

    return str(resp)
