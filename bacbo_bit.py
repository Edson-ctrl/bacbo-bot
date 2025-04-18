import os
import time
import random
import requests

# Configurações
WATI_TOKEN = os.getenv("WATI_TOKEN")
PHONE_NUMBER = "+244941633034"  # Número que receberá as mensagens
SINAIS = ["Tie", "Banker", "Player"]

def gerar_sinal():
    return random.choice(SINAIS)

def enviar_sinal(sinal):
    url = "https://app.wati.io/api/v1/sendSessionMessage"
    headers = {
        "Authorization": f"Bearer {WATI_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "phone": PHONE_NUMBER,
        "message": f"Sinal Bac Bo: Aposte em *{sinal}* agora!"
    }
    response = requests.post(url, headers=headers, json=payload)
    print("Enviado:", response.status_code, response.text)

def main():
    while True:
        sinal = gerar_sinal()
        enviar_sinal(sinal)
        time.sleep(60)  # Envia um sinal por minuto (ajuste
