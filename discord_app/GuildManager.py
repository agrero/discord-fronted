import discord
from discord.guild import Guild


# can make a proctor class that uses both 
# creating guilds and categories
class GuildManager:

    
    async def make_text_channel(
            self, guild:Guild, channel_name:str='secret', secret:bool=True
        ):

        # this will be eventually handled by the Permissions class
        if secret:
            overwrites = {
                Guild.default_role : discord.PermissionOverwrite(
                    read_messages=False
                    # **obj_model_dump works here
                ),
                Guild.me: discord.PermissionOverwrite(
                    read_messages=True
                )
            }
        else:
            overwrites = {}


        # should make a category before
        channel = await guild.create_text_channel(
            name=f'{channel_name}', 
            # overwrites=overwrites, # need to add name change ability here
            # type=discord.ChannelType.text
        )

        return channel
        # can manipulate the channel variable 
        # to do thigns to it afterwards


    async def create_category(self):
        # to be added later
        pass

    # this might go in the toplevel thing
    async def clear_text_channel(self):
        pass

#await create_text_channel

# need to be able to make text channel

# change permissions to make it private (Different class)
# - per user based on discord_id


