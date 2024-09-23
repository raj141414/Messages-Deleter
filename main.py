from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated

# Replace 'API_ID', 'API_HASH', and 'BOT_TOKEN' with your credentials
API_ID = '16501053'
API_HASH = 'd8c9b01c863dabacc484c2c06cdd0f6e'
BOT_TOKEN = '7721012312:AAF8Q0dYhN5vLYq5nvBnWvwkBvSEVgaKGns'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("delete_all") & filters.group)
async def delete_all(client, message):
    if not message.chat.permissions.can_delete_messages:
        await message.reply("I don't have permission to delete messages in this chat.")
        return

    async for msg in client.get_chat_history(message.chat.id):
        await client.delete_messages(message.chat.id, msg.message_id)

    await message.reply("All messages deleted!")

app.run()
