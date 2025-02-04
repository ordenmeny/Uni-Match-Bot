import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")

async def set_chat_id(chat_id, uniq_code):
    url = f"{HOST}/users/api/get-bot/{uniq_code}/"
    data = {
        "uniq_code": "",
        "chat_id": chat_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.patch(url, json=data) as response:
            if response.status in (200, 201):
                result = await response.json()
                print(result.get("data"))
                return result
            else:
                error_message = await response.text()
                return None