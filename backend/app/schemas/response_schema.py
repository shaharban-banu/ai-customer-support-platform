from pydantic import BaseModel

# pylint: disable=too-few-public-methods
class TicketResponse(BaseModel):

    id: int
    message: str
    category: str
    sentiment: str
    priority: str
    summary: str

    class Config:

        from_attributes = True
        