from pyrogram import Client, filters

API_ID = '16501053'  # Replace with your actual API ID
API_HASH = 'd8c9b01c863dabacc484c2c06cdd0f6e'  # Replace with your actual API Hash
BOT_TOKEN = '7721012312:AAF8Q0dYhN5vLYq5nvBnWvwkBvSEVgaKGns'  # Replace with your actual Bot Token

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("delete_all") & filters.group)
async def delete_all(client, message):
    bot_member = await client.get_chat_member(message.chat.id, client.me.id)

    print(f"Bot Status: {bot_member.status}")

    # Check if the bot is an administrator
    if bot_member.status in ["administrator", "creator"]:
        # Verify that the bot has permission to delete messages
        if not bot_member.privileges or not bot_member.privileges.can_delete_messages:
            await message.reply("I don't have permission to delete messages in this chat.")
            return

        # Deleting messages
        async for msg in client.get_chat_history(message.chat.id):
            await client.delete_messages(message.chat.id, msg.message_id)

        await message.reply("All messages deleted!")
    else:
        await message.reply("I need to be an administrator to delete messages.")

app.run()
