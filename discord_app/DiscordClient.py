import discord
from .helper import get_command
from .children.ClientHandler import ClientHandler
from discord_app.GuildManager import GuildManager
from .children.handlers.RequestHandler import RequestHandler


class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $s: Discord Bot Command Prompt

    I think eventually this will swallow a more condensed
    Client Handler class
    """
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(
            self, 
            message, 
            url='http://0.0.0.0:8000', 
            # handler=ClientHandler()
        ) -> None:
        
        """
        On Message Response method

        listens to all discord messages accessible to the bot
        sends commands to listed api url & sends a message in the same
        discord channel as a response. Ignores messages without $s command
        prompt in the user message.

        !!! UPDATE ME
        handler: message response handler class
        !!!

        message: discord message class containing message content as well as
            ownership details. 
        url: url for api call
        
        returns: None
        """
    
        if message.author == self.user:
            return

        if message.content.startswith('$s'):
            handler = ClientHandler()
            response = await handler.get_boardstate(message, url)
            await message.channel.send(response.json()['puzzle'])

        if message.content.startswith('$t'):
            
            # NEED TO ADD CHECK SO YOU CAN'T MAKE MULTIPLE TEXT 
            # CHANNELS OF THE SAME NAME

            # should insert some verification here
            # 
            # 
            # # verification request is sent
            # 
            # # if approved: 
            # # # create secret text handler = ClientHandler()channel for user
            #  
            # # if not approved:
            # # # do nothing


            ####################
            # MESSAGE HANDLING #
            ####################

            # key input: $t {key}
            key = message.content.split(' ')[1]
            
            ########################
            # MESSAGE VERIFICATION #
            ########################

            # send database request
            
            # get user
            handler = ClientHandler(
                json={
                    'discord_id' : message.author.id,
                    'username' : message.author.name
                },
                commands=['get', 'user']
            )

            # extract key

            # verify key
            
            ####################
            # MESSAGE RESPONSE #
            ####################
            
            # overwrites
            overwrites = {
                message.author.guild.default_role : discord.PermissionOverwrite(
                    read_messages=False
                    # **obj_model_dump works here
                ),
                message.author.guild.me: discord.PermissionOverwrite(
                    read_messages=True
                )
            }

            # make channel in specific category
            await message.author.guild.create_text_channel(
                name=f'test_{message.author.name}',
                overwrites=overwrites,
                category = discord.utils.get(
                    message.author.guild.categories,
                    name='Testing Environments'
                )) # get Text Channels category
            
            await message.delete()

            # # init guild manager
            # manager = GuildManager(id=message.author.guild.id)
            # # print(message)
            
            # # create default_guild test
            # await manager.make_text_channel(channel_name='secret')

            # # create non default guild test
            # await manager.make_text_channel(
            #     guild_name='non_secret', 
            #     secret=False
            # )


        # for testing 
        if message.content.startswith('$test'):
            handler = ClientHandler(
                url = 'http://0.0.0.0:8000', # database url
                commands = get_command(message.content[2:]),
                json = '' # this hsould be the CommandIn Schema
            )
            # decompose message


            response = await handler.send_board(
                
            )