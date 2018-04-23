import config
import requests
from time import sleep

def get_updates_json(request):
    params ={'timeout':100, 'offset': None}
    response = requests.get(config.token + 'getUpdates', proxies=config.proxies, data=params)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_text(update):
    text_id=update['message']['text']
    return text_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(config.token + 'sendMessage', data=params, proxies=config.proxies)
    return response

def main():
    update_id = last_update(get_updates_json(config.token))['update_id']
    while True:
        if update_id == last_update(get_updates_json(config.token))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(config.token))), get_text(last_update(get_updates_json(config.token))))
            update_id +=1
        sleep(1)

if __name__ == '__main__':
    main()