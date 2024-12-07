from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


class CallAttributes(BaseModel):
    date: datetime
    risk_score: float = Field(alias="riskScore", ge=0.0, le=1.0)
    number: str
    green_list: bool = Field(alias="greenList")
    red_list: bool = Field(alias="redList")


class Call(BaseModel):
    type: Literal["call"]
    id: str
    attributes: CallAttributes
