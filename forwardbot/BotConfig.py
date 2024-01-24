from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "1522127")
    API_HASH = environ.get("API_HASH", "1252ffe16baf341bfd7236f92df76b0e")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6971823310:AAE_QcYgfRlCIQsuR-zuIqhvnoyAzf35b4g")
    STRING_SESSION = environ.get("STRING_SESSION", "AQAXOc8APTglOd8gyen6KjU4VTT4FkxHD5RLgRA9Bh4y_K0GFB1Fs_bHy0pzRCtAixFG2EpQeMYGqSUHyYZ5MzWZep6niKWHkJt-qjSQMuYJOOIO4ncjj7EpxihRUWiZGb0j_sBuwHcnPKs_c25L78wAw84TS-FYvJt513BIBdDQWJt2EUysznHY_TvjffMDjaPJ8wJukNVOFyxsotMJiI1lLD2B1e7m6dehJFiGEhbj1qQclWTJMof5MH-TzEhoPSWGplEnKRtW-iMKDUJ5QjheMuLQD2cb_3hDtF9n6UC-ggxv-JFoZiT96xHQHGStmQkZ177wQmeFzNcfCmkacKA-YsFAXgAAAAA7-MTRAA")
    SUDO_USERS = environ.get("SUDO_USERS", "1006159057")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
