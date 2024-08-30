from pydantic import BaseModel

class CommandIn(BaseModel):

    commands: list[str]
    user: str
    user_id: int

    # I think we can cut these
    # message_id: int
    # guild_id: int

class CommandOut(CommandIn):
    data: str # could be a dict idk 
