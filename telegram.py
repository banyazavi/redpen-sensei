import requests

def send_message(token, chat_id, text):
    telegram_host = 'https://api.telegram.org'
    telegram_sendmessage = f'{telegram_host}/bot{token}/sendmessage'
    params = {'chat_id': chat_id, 'text': text}
    return requests.get(telegram_sendmessage, params=params)
