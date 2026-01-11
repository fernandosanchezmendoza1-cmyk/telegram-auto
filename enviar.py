from telethon import TelegramClient
import asyncio
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

grupo = os.environ["GRUPO"]
mensaje = os.environ["MENSAJE"]

async def main():
    async with TelegramClient("session", api_id, api_hash) as client:
        await client.send_message(grupo, mensaje)

asyncio.run(main())
