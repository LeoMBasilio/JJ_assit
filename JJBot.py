import requests
import GerenciadorCredenciais as gc

"""
    Descrição:
        Classe responsável por fazer a conexão com o bot
"""
class Bot:
    def __init__(self, __token__):
        self.__token__ = __token__

    def last_chat_id(self):
        try:
            url = "https://api.telegram.org/bot{}/getUpdates".format(self.__token__)
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

    def send_message(self, __chat_id__, message):
        try:
            data = {"chat_id": __chat_id__, "text": message}
            url = "https://api.telegram.org/bot{}/sendMessage".format(self.__token__)
            requests.post(url, data)
        except Exception as e:
            print(e)

    def bot(self, menssgem):
        # credChat = gc.GerenciadorCredenciais().BotToken()
        credChat = gc.GerenciadorCredenciais().BotTokenLocal()

        __chat_id__ = credChat['chatId'] #last_chat_id(__token__)

        self.send_message(__chat_id__, menssgem)

# def last_chat_id(__token__):
#     try:
#         url = "https://api.telegram.org/bot{}/getUpdates".format(__token__)
#         response = requests.get(url)
#         if response.status_code == 200:
#             json_msg = response.json()
#             for json_result in reversed(json_msg['result']):
#                 message_keys = json_result['message'].keys()
#                 if ('new_chat_menber' in message_keys) or ('group_chat_created' in message_keys):
#                     print(json_result['message']['chat']['id'])
#                     return json_result['message']['chat']['id']
#             print('nada encontrado')
#         else:
#             print(response.status_code)
#     except Exception as e:
#         print(e)

# def send_message(__token__, __chat_id__, message):
#     try:
#         data = {"chat_id": __chat_id__, "text": message}
#         url = "https://api.telegram.org/bot{}/sendMessage".format(__token__)
#         requests.post(url, data)
#     except Exception as e:
#         print(e)

# def bot(menssgem):
#     __token__ = "6647615711:AAGDgZD-TcQV8KklHlu0PuFLDDgUWULk-4I"

#     __chat_id__ =  "-4057661365" #last_chat_id(__token__)

#     send_message(__token__, __chat_id__, menssgem)

# bot("teste")