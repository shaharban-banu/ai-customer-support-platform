from pydantic import BaseModel

class TicketRequest(BaseModel):
    message:str
    