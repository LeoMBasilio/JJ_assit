import requests

def last_chat_id(__token__):
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(__token__)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                if ('new_chat_menber' in message_keys) or ('group_chat_created' in message_keys):
                    print(json_result['message']['chat']['id'])
                    return json_result['message']['chat']['id']
            print('nada encontrado')
        else:
            print(response.status_code)
    except Exception as e:
        print(e)

def send_message(__token__, __chat_id__, message):
    try:
        data = {"chat_id": __chat_id__, "text": message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(__token__)
        requests.post(url, data)
    except Exception as e:
        print(e)

def bot(menssgem):
    __token__ = "Token do bot"

    __chat_id__ = last_chat_id(__token__)

    send_message(__token__, __chat_id__, menssgem)