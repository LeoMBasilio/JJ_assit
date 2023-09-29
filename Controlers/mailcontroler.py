from imap_tools import MailBox, AND, OR, NOT
from datetime import date
from JJBot import bot
from time import sleep
import re
import sys


__mail = "email"
__pswd = "senha"

mails = ["lista de emails"]
materias = ["Teste", "Processos Ágeis de Desenvolvimento", "Ambientação Digital", "Avaliação Integrada de Competências em Coding I", "Plano de Acompanhamento de Carreira em Coding I", "Estrutura de Dados", "Modelagem de Dados", "Fundamentos de Devops", "Linguagem de Banco de Dados", "Programação Orientada a Objetos"]

padrao_url = 'https?://\S+|www\.\S+'
padrao_date = '\d{1,2}/\d{1,2}/\d{4}'

while True:

    try:
        with MailBox("imap.gmail.com").login(__mail, __pswd) as mailbox:
            print("inbox")
            inbox = mailbox.fetch(AND(OR(text=mails), AND(seen=False)))
            print("tamaho do inbox: ", sys.getsizeof(inbox))
            for msg in inbox:
                for mat in materias:
                    print(mat)
                    subject = re.search(mat, msg.subject)
                    print(subject)
                    prazo = (re.search("prazo", msg.text) or re.search("Prazo", msg.text))
                    print(prazo)

                    link = re.findall(padrao_url, msg.text)
                    print(link)
                    prazos_date = re.findall(padrao_date, msg.text)
                    print(prazos_date)    

                    prova = (re.search("Prova", msg.subject) or re.search("Prova", msg.text) or re.search("prova", msg.text))
                    print(prova)
                    af = (re.search("AF", msg.subject,) or re.search("AF", msg.text))
                    print(af)
                    
                    
                    if subject:
                        if prova or af:
                            print("Prova De ", mat)
                            
                            botmsg = "Prova De {} \n {}".format(mat, msg.text)

                            if prazo:

                                if link:
                                    print("contem um link")
                                    botmsg = "Prova De {} \n datas: {} \n link: {}".format(mat, prazos_date, link)

                                botmsg = "Prova De {} \n datas: {}".format(mat, prazos_date)

                            elif link:

                                botmsg = "Prova De {} \n link: {}".format(mat, link)

                            
                            bot(botmsg)
                            sleep(120)

                        elif not (prova or af):
                            print("materia", mat)
                            
                            botmsg = "Nova atividade de {} ".format(mat)

                            if prazo:

                                if link:
                                    print("contem um link")
                                    botmsg = "Nova atividade de {} \n datas: {} \n link: {}".format(mat, prazos_date, link)

                                botmsg = "Nova atividade de {} \n datas: {}".format(mat, prazos_date)

                            elif link:

                                botmsg = "Nova atividade de {} \n link: {}".format(mat, link)

                            bot(botmsg)
                            sleep(120)

                        else:
                            print("materia", mat)
                            
                            botmsg = "Nova atividade de {} ".format(mat)

                            if prazo:

                                if link:
                                    print("contem um link")
                                    botmsg = "Nova atividade de {} \n datas: {} \n link: {}".format(mat, prazos_date, link)

                                botmsg = "Nova atividade de {} \n datas: {}".format(mat, prazos_date)

                            elif link:

                                botmsg = "Nova atividade de {} \n link: {}".format(mat, link)

                            bot(botmsg)
                            sleep(120)
                    
    except Exception as e:
        print(e)
        break