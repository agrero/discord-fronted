# bot.py

if __name__ == '__main__':

    import os
    import discord

    # we need to fix this naming
    from discord_app.DiscordClient import CustomClient

    # ah what another good looking candidate for some data validation 
    # using pydantic models

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_ROOT')
    API_URL = os.getenv('URL_ROOT')

    intents = discord.Intents.default()
    intents.message_content = True

    client = CustomClient(intents=intents)

    client.run(TOKEN)