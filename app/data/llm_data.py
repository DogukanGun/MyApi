from pydantic import BaseModel


class DonationMessage(BaseModel):
    role: str
    content: str
