import requests
import os

def getNotionDatabaseData():
    
    databaseId = os.environ["NOTION_DATABASE_ID"]

    url = f"https://api.notion.com/v1/databases/{databaseId}"

    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json",
        "Authorization": os.environ["NOTION_INTERNAL_INTEGRATION_TOKEN"]
    }

    response = requests.get(url, headers=headers)

    return response.json()

print(getNotionDatabaseData())