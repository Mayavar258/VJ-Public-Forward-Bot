from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "27610252")
    API_HASH = environ.get("API_HASH", "73e16fc08192ba7c1d52d4dc9fa2b220")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6487620358:AAE4iz1l7VIALr0mUVdMp5GDhlNM5DEqQfM")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOLoBu1giFqgzdzOMYmWoOlCeaozPvGVk8pcaxp_0-94fSDE5LcDvoIJ_RWClAUXOP28eFIpJNWDGbhG-LOrFqeZPJbq4DSYONphgA_SUoOSOCAQFkA-3df_DwRR1YOar8xN1kqlURD_WW8tThEyOaJEHgxKRpoX2d8onhd87TWzPS1mG6qOfkeL34gPqsy9LlEWJpLJhfClfr8t5mMLV4mXnVa1CAmaLGU7KCmhMuV5DvZs9Tr9cme25ksVOJY1l1xMXW5hGGFycjRcA4GRqzmIJOecQi4XG_3l7GDfATNDeYgzAADfK6HGG7mDwElbOGq5qbSL8kDFA0PCQqz_DPtSEvJg=")
    SUDO_USERS = environ.get("SUDO_USERS", "5319623393")
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
