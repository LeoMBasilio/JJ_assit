import Database as db
import mailcontroler as mc
import GerenciadorCredenciais as gc
import json

def main():
    print("Iniciando o programa")

    # credDB = gc.GerenciadorCredenciais().dbCredentials()
    credDB = gc.GerenciadorCredenciais().dbCredentialsLocal()

    search = db.Conector(credDB["host"], credDB["user"], credDB["password"], credDB["database"])

    mails = '''
            select email from tb_remetentes;
            ''' 

    materias = '''
                SELECT nome from tb_materias tm
                '''
    
    
    mails = [item[0] for item in search.query(mails)]

    materias = [item[0] for item in search.query(materias)]

    print(mails)
    print(materias)

    print("Iniciando o bot")
    mc.inbox(mails, materias)

if __name__ == "__main__":
    main()
