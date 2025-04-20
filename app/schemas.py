from pydantic import BaseModel
from typing import Literal 

class ReplyRequest(BaseModel):
    platform: Literal["Twitter", "LinkedIn", "Instagram"]
    post_text: str

class ReplyResponse(BaseModel):
    generated_reply: str 
    