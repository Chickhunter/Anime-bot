from Shikimori import telethn
from Shikimori.events import register as tomori


@tomori(pattern="^/(all|mentionall|tagall|utag) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()

@tomori(pattern="^@(all|mentionall|tagall|utag) ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Tagged by an admin"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


# @tomori(pattern="^/users ?(.*)")
# async def _(event):
#     if event.fwd_from:
#         return
#     mentions = "Users : "
#     chat = await event.get_input_chat()
#     async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
#         mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
#     reply_message = None
#     if event.reply_to_msg_id:
#         reply_message = await event.get_reply_message()
#         await reply_message.reply(mentions)
#     else:
#         await event.reply(mentions)
#     await event.delete()


__mod_name__ = "《TagAll》"
__help__ = """
*Tag All*
 ❍ `/users` : Get txt file of all users in your group.
 ❍ `/all` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/tagall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/utag` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `/mentionall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@all` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@tagall` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@utag` : (reply to message or add another message) To mention all members in your group, without exception.
 ❍ `@mentionall` : (reply to message or add another message) To mention all members in your group, without exception.
"""
