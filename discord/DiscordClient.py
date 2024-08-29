import discord
from helper import get_command
from children.ClientHandler import ClientHandler


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