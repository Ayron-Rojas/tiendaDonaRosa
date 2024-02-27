import requests

def obtenerCHAT_ID(TOKEN):
    respuesta = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    datos = respuesta.json()
    chat_ID = datos['result'][0]['message']['chat']['id']
    return chat_ID