from pydantic import BaseModel, field_validator
from typing import Literal
import re


class OperatorAttributes(BaseModel):
    prefix: str
    operator: str

    @field_validator("prefix")
    def check_prefix(cls, v) -> str:
        # must be 4 digits ending in '000'
        if not re.match(r"^[1-9][0-9]{3}$", v) or not v.endswith("000"):
            raise ValueError(
                "prefix must be 4 digits ending in 000 and not start with 0"
            )
        return v

    def is_number_in_range(self, number: str) -> bool:
        """Check if a number falls within the operator's prefix range"""
        # get the 4 digits after the country code
        prefix_to_check = number[3:7]

        try:
            prefix_num = int(prefix_to_check)
            range_start = int(self.prefix)  # "2000" -> 2000
            range_end = range_start + 999  # 2999
            return range_start <= prefix_num <= range_end
        except (ValueError, IndexError):
            return False


class Operator(BaseModel):
    type: Literal["operator"]
    id: str
    attributes: OperatorAttributes
