import requests
import json

def consultar_ollama(mensaje_usuario):
    payload = {
        "model": "gemma:2b", 
        "messages": [
            {"role": "user", "content": mensaje_usuario}
        ]
    }

    try:
        respuesta = requests.post("http://localhost:11434/api/generate", json=payload)
        respuesta.raise_for_status()
        data = respuesta.json()

        # Extraer la respuesta del modelo
        mensaje_respuesta = data.get("message", {}).get("content", "")

        return mensaje_respuesta or "No hubo respuesta del modelo."
    except Exception as e:
        return f"⚠️ Error al conectar con Ollama: {e}"

