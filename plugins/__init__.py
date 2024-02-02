from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from database.users_chats_db import db
from info import SUPPORT_CHAT
from aiohttp import web
from utils import temp


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response(text="𝘌𝘷𝘢 𝘮𝘢𝘳𝘪𝘢 𝘨𝘳𝘰𝘶𝘱")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def banned_users(_, client, message: Message):
    return (message.from_user is not None or not message.sender_chat) and (message.from_user.id in temp.BANNED_USERS)

async def disabled_chat(_, client, message: Message):
    return message.chat.id in temp.BANNED_CHATS

@Client.on_message(filters.private & filters.incoming & filters.create(banned_users))
async def ban_reply(bot, message):
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(f"𝘚𝘰𝘳𝘳𝘺 𝘋𝘶𝘥𝘦， 𝘠𝘰𝘶 𝘈𝘳𝘦 𝘉𝘢𝘯𝘯𝘦𝘥 𝘛𝘰 𝘜𝘴𝘦 𝘔𝘦. \n𝘉𝘢𝘯 𝘙𝘦𝘢𝘴𝘰𝘯: {ban['ban_reason']}")

@Client.on_message(filters.group & filters.incoming & filters.create(disabled_chat))
async def grp_bd(bot, message):
    buttons = [[InlineKeyboardButton('🔮𝘚𝘶𝘱𝘱𝘰𝘳𝘵🔮', url=f'https://t.me/{SUPPORT_CHAT}')]]
    chat = await db.get_chat(message.chat.id)
    k = await message.reply(text=f"𝘊𝘏𝘈𝘛 𝘕𝘖𝘛 𝘈𝘓𝘓𝘖𝘞𝘌𝘋 \n\n𝘔𝘺 𝘈𝘥𝘮𝘪𝘯𝘴 𝘏𝘢𝘴 𝘙𝘦𝘴𝘵𝘳𝘪𝘤𝘵𝘦𝘥 𝘔𝘦 𝘍𝘳𝘰𝘮 𝘞𝘰𝘳𝘬𝘪𝘯𝘨 𝘏𝘦𝘳𝘦 ! 𝘐𝘧 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘛𝘰 𝘒𝘯𝘰𝘸 𝘔𝘰𝘳𝘦 𝘈𝘣𝘰𝘶𝘵 𝘐𝘵 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘚𝘶𝘱𝘱𝘰𝘳𝘵..\n𝘙𝘦𝘢𝘴𝘰𝘯 : <code>{chat['reason']}</code>.", reply_markup=InlineKeyboardMarkup(buttons))
    try: await k.pin()
    except: pass
    await bot.leave_chat(message.chat.id)
