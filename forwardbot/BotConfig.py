from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "27610252")
    API_HASH = environ.get("API_HASH", "73e16fc08192ba7c1d52d4dc9fa2b220")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6487620358:AAE4iz1l7VIALr0mUVdMp5GDhlNM5DEqQfM")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOJoBu6bhB3nam2-3jQkD6gTKvwWklLmEqsbFI_YelLJb5gv7tbz-r28SPvEUrtgtl3BhUkAiEI3UQWwumrYqKQ795frc9qIYEfr-bt6SacacS4o3hUZ-8TBe4tKJoycbzGNvIo2FmKTExFFQOKhFEL524ckMhteEH89JefBbjVftylufgkoE2i0ZFlr1i-mdo7l4a__jSAlD0p32pfF0lce0GBGb_pZ2zgYYdqi1HNNnrHRAjXys0xRhh1jS120xaBmDaJMZFwCKFNdHjs9tm3q54tjQ7MgY6d7lCYB8dKiRyCnfRDaFQhygYxvp5q4yKt3tnMxiZxYqgUxXCwXPtz8qkoc=")
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
