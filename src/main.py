import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

main_content = {'content': 'Hello World'}
headers = {'Content-Type': 'application/json'}

response = requests.post(
    webhook_url,
    json.dumps(main_content),
    headers=headers)
