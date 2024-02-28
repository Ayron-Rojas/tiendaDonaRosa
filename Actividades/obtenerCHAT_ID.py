import requests

def obtener_chat_id(token):
    response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    data = response.json()
    chat_id = data['result'][0]['message']['chat']['id']
    return chat_id