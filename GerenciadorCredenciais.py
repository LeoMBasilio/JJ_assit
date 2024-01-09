import requests as rq
import json

class GerenciadorCredenciais:
    def __init__(self):
        self.url = "http://localhost:5000"
        self.headers = {"Content-Type": "Authentication"}
        self.token = None
        self.path = 'D:\Projetos\JJ_assit_original\Credenciais.json'
    
    def email(self):
        response = rq.get(self.url + "/Email", headers=self.headers)
        return response.json()

    def BotToken(self):
        response = rq.get(self.url + "/JJtoken", headers=self.headers)
        return response.json()
    
    def dbCredentials(self):
        response = rq.get(self.url + "/dbCredentials", headers=self.headers)
        return response.json()
    
    def emailLocal(self):
        with open(self.path, "r") as file:
            return json.load(file)
        
    def BotTokenLocal(self):
        with open(self.path, "r") as file:
            return json.load(file)
        
    def dbCredentialsLocal(self):
        with open(self.path, "r") as file:
            return json.load(file)