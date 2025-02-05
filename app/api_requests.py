import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
DRF_API_TOKEN = os.getenv("DRF_API_TOKEN")

async def set_chat_id(chat_id, uniq_code):
    headers = {"Authorization": f"Token {DRF_API_TOKEN}"}

    url = f"{HOST}/users/api/get-bot/{uniq_code}/"
    data = {
        "uniq_code": "",
        "chat_id": chat_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.patch(url, json=data, headers=headers) as response:
            if response.status in (200, 201):
                result = await response.json()
                return result
            else:
                # error_message = await response.text()
                return None

async def get_user(chat_id):
    headers = {"Authorization": f"Token {DRF_API_TOKEN}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{HOST}/users/api/get-user/{chat_id}', headers=headers) as response:
            if response.status in (200, 201):
                return await response.json()
            else:
                return None