from imap_tools import MailBox, AND, OR, NOT
from datetime import date
from JJBot import bot
from time import sleep
import re



__mail = "email"
__pswd = "senha"

mails = ["lista de emails"]
materias = ["Teste", "Processos Ágeis de Desenvolvimento", "Ambientação Digital", "Avaliação Integrada de Competências em Coding I", "Plano de Acompanhamento de Carreira em Coding I", "Estrutura de Dados", "Modelagem de Dados", "Fundamentos de Devops", "Linguagem de Banco de Dados", "Programação Orientada a Objetos"]
while True:

    try:
        with MailBox("imap.gmail.com").login(__mail, __pswd) as mailbox:
            print("mail entre")
            for msg in mailbox.fetch(AND(OR(text=mails), AND(date=date.today(), seen=False))):
                for mat in materias:
                    subject = re.search(mat, msg.subject)
                    link = re.search("http", msg.text)
                    prova = (re.search("Prova", msg.subject) or re.search("Prova", msg.text))
                    af = (re.search("AF", msg.subject,) or re.search("AF", msg.text))
                    if subject:
                        if prova or af:
                            print("###### Prova De ", mat, "######")
                            print(msg.text)
                            
                            botmsg = "###### Prova De {} ###### \n {}".format(mat, msg.text)

                            if link:
                                print("contem um link")
                                
                                botmsg = "###### Prova De {} ###### \n {} \n Contem um link que pode nao estar anexado na notificação".format(mat, msg.text)
                            
                            bot(botmsg)
                        elif not (prova or af):
                            print("chama api para materia comum passnasdo a materia", mat)
                            
                            botmsg = "###### Nova atividade na materia {} ######".format(mat)

                            if link:
                                print("contem link")
                            
                                botmsg = "###### Nova atividade na materia {} ###### \n {} \n Contem um link que pode nao estar anexado na notificação".format(mat, msg.text)

                            bot(botmsg)

        sleep(1200)

    except Exception as e:
        print(e)
        break