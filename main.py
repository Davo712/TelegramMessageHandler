from telethon import TelegramClient, utils
from telethon import events
from telethon.tl import types
from telethon.tl.types import PeerChannel, PeerChat, PeerUser
import venv

api_id = 1
api_hash = '2'

chat_id = 3
chat = types.PeerChat(chat_id)
message_syntax = 'https://t.me/c/'

client = TelegramClient('anon.session', api_id, api_hash)
client.start()
print("Application started")


@client.on(events.NewMessage())
async def main(event):
    if isinstance(event.message.peer_id, PeerChannel):
        end_message = message_syntax + str(event.message.peer_id.channel_id) + "/" + str(event.message.id)
    if isinstance(event.message.peer_id, PeerChat):
        end_message = message_syntax + str(event.message.peer_id.chat_id) + "/" + str(event.message.id)
    if isinstance(event.message.peer_id, PeerUser):
        end_message = message_syntax + str(event.message.peer_id.user_id) + "/" + str(event.message.id)

    dialog = event.chat if event.chat else (await event.get_chat())
    dialog_title = utils.get_display_name(dialog)

    sender_name = (await event.message.get_sender()).username

    content = event.message.message + "\nLink: " + end_message + "\nDialog Name: " + dialog_title + "\nSender: " + sender_name

    if dialog.id != chat_id:
        await client.send_message(chat, content)


client.run_until_disconnected()
