from pyrogram import Client, filters
import asyncio

API_ID = '16501053'  # Your API ID
API_HASH = 'd8c9b01c863dabacc484c2c06cdd0f6e'  # Your API Hash
BOT_TOKEN = '7721012312:AAF8Q0dYhN5vLYq5nvBnWvwkBvSEVgaKGns'  # Your Bot Token

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("delete_all") & filters.group)
async def delete_all(client, message):
    try:
        bot_member = await client.get_chat_member(message.chat.id, client.me.id)

        if bot_member.status in ["administrator", "creator"]:
            if hasattr(bot_member, "privileges"):
                permissions = bot_member.privileges
                if not permissions.can_delete_messages:
                    await message.reply("I don't have permission to delete messages in this chat.")
                    return
            else:
                await message.reply("The bot has administrator rights but cannot check privileges.")
                return

            # Get the chat history
            messages = await client.get_chat_history(message.chat.id)
            total_messages = len(messages)

            if total_messages == 0:
                await message.reply("No messages to delete.")
                return

            progress_message = await message.reply(f"Deleting {total_messages} messages...")

            # Delete messages with progress indication
            for index, msg in enumerate(messages):
                await client.delete_messages(message.chat.id, msg.message_id)
                await progress_message.edit(f"Deleted {index + 1}/{total_messages} messages.")
                await asyncio.sleep(2)  # Wait for 2 seconds between deletions

            await progress_message.edit("All messages deleted!")

        else:
            await message.reply("I need to be an administrator to delete messages.")
    
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
        print(f"Error: {str(e)}")

app.run()
