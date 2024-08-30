
from .handlers.BoardHandler import BoardHandler
from .handlers.RequestHandler import RequestHandler


class ClientHandler(
    RequestHandler, # requests related methods and atts
    BoardHandler # board related methods and atts
    ):
    def __init__(self) -> None:
        super().__init__(self)


    async def get_board(self):
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

    async def send_board(self, message) -> None:
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

        



