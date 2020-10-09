#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def welcome_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("""**Hey [{}](tg://user?id={})!!\n Please Read <a href='https://t.me/Discovery_Updates/7'>This Message</a> To know how to use Me  \n""", disable_web_page_preview=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("`/leech`: Reply to direct download link, it will upload to telegram.\n \n`/gleech`: Reply to direct link, it will upload to cloud.\n \n`/tleech`: This will mirror the telegram files to cloud.\n \n`/status`: Check current status of bot.\n \n`/leech archive`: Upload torrent and files to telegram in tar.gz format.\n \n`/gleech archive`: compress file/folder and upload to cloud.\n \n`/leech unzip`: This will unzip the ZIP file and upload to telegram.\n \n`/gleech unzip`: This will unzip the ZIP file and upload to cloud.\n \n`/leech unrar`: This will unrar the RAR file and upload to telegram\n \n`/gleech unrar`: This will unrar the RAR file and upload to cloud.\n \n`/leech untar`: This will untar the TAR file and upload to telegram.\n \n`/gleech untar`: This will untar the TAR file and upload to cloud.\n \n`/tleech unzip`: This will unzip the telegram ZIP file and upload to cloud.\n \n`/tleech unrar`: This will unrar the telegram RAR file and upload to cloud.\n \n`/tleech untar`: This will untar the telegram TAR file and upload to cloud.\n \n`/getsize`: This will give you total size of your destination folder in cloud.\n \n`/ytdl`: Reply to any YouTube video link to download the video. \n \n`/ytdl gdrive`: Reply to any YouTube video link to download the video. This will download and upload to cloud.\n \n`/pytdl`: Download videos from youtube playlist link and will upload to telegram.\n \n`/pytdl gdrive`: Download youtube playlist and upload to cloud.\n \n`/renewme`: Clear files from server of @AbirHasan2005.\n")


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
