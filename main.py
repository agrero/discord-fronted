# bot.py

if __name__ == '__main__':

    import os
    import discord_app

    from discord_app.DiscordClient import CustomClient

    # ah what another good looking candidate for some data validation 
    # using pydantic models

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_ROOT')
    API_URL = os.getenv('URL_ROOT')

    intents = discord_app.Intents.default()
    intents.message_content = True

    client = CustomClient(intents=intents)

    client.run(TOKEN)