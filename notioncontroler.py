# Initialisation
import requests, json

"""
    Descrição:
        Cria uma página no notion com os dados passados no newPageData
    Atenção:
        Ainda não esta implementado
"""

token = 'token'
databaseID ="id do banco de dados do notion"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

# Create a Page
def createPage(databaseID, headers):
    createUrl = 'url do notion'
    newPageData = {
        "parent": { "database_id": databaseID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "DONA"
                        }
                    }
                ]
            },
            "Text": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "This is thienqc"
                            },
                        }
                    ]
                },
            "Checkbox": {
                    "checkbox": True
                },
            "Number": {
                    "number": 1999
            },
            "Select": {
                    "select": {
                        "name": "Mouse",
                    }
                },
            "Multi-select": {
                    "multi_select": [
                        {
                            "name": "Apple",
                        },
                        {
                            "name": "Banana",
                        }
                    ]
                },
            "Date": {
                    "date": {
                        "start": "2022-08-05",
                        "end": "2022-08-10",
                    }
                },
            "URL": {
                    "url": "google.com"
                },
            "Email": {
                    "email": "dolor@ipsum.com"
                },
            "Phone": {
                    "phone_number": "19191919"
                },
            "Person": {
                    "people": [
                        {
                            "id": "4af42d2d-a077-4808-b4f7-e960a93fd945",
                        }
                    ]
                },
            "Relation": {
                    "relation": [
                        {
                            "id": "fbb0a7f2-413e-4728-adbf-281ab14f0c33"
                        }
                    ]
                }
            }
        }
    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)

createPage(databaseID,headers)