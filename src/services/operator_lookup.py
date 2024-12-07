from typing import List
from src.models.operator import Operator
from src.models.call import Call


class OperatorLookup:
    def __init__(self, operators: List[Operator]):
        self.operators = operators

    def get_operator_for_call(self, call: Call) -> str:
        """
        find the operator for a call based on the number prefix
        return 'Unknown' if no matching operator found
        """

        for operator in self.operators:
            if operator.attributes.is_number_in_range(call.attributes.number):
                return operator.attributes.operator

        return "Unknown"
