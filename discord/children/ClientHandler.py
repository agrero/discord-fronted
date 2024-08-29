import requests

from fastapi.encoders import jsonable_encoder

# Add this function to helper
from helper import get_command

# need this import somehow (can just implement when its all modularized)

# SUDOKU
# from sudoku.classes.game.Board import Board
# -> REPLACEMENT
from .handlers.BoardHandler import BoardHandler
from .handlers.RequestHandler import RequestHandler

# SCHEMAS
# from sudoku.schemas.api import CommandIn
# -> REPLACEMENT
from .schemas import discord

# MANIUPLATIONS SHOULD HAPPEN NOT HERE
# ALSO TRY AND SLIM THIS DOWN AND MAKE IT PART OF THE CUSTOMCLIENT
class ClientHandler(
    RequestHandler, BoardHandler
    ):
    def __init__(self) -> None:
        super().__init__(self)


    async def get_board(self) -> requests.json :
        """
        Top level handler for board post responses
        
        ! NOTE

        I think at some point we should make this return the content
        of post instead of the post 

        I think that fits thematically with assess_method 
        being inherited from the post handler
        """

        try:
            post = self.assess_method(self.commands[-1])
        except:
            raise ValueError("Object missing components")

        # need to figure out what piece is the board
        # after we determine what piece is the board,
        # we need to make this method return it fancy

        # if the functinal method works here, we 
        # jsut need to make it return whatever we want
        return post.json()

    async def send_board(self, message, url:str) -> None:
        """
        sends board state to discord utilizing get_boardstate
        method.

        message: a message in the form of an on_message discord 
            response
        url: api url

        returns: None
        """
        
        # post.json() returns just a json
        await message.channel.send(self.get_board()) 
        



