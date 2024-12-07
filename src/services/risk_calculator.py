from decimal import Decimal, ROUND_HALF_UP
from src.models.call import Call


class RiskCalculator:
    def calculate_risk_score(self, call: Call) -> float:
        """
        Calculate the final risk score for a call based on the rules:
            rounded half up to 1 DP (i.e. half way values or above are rounded up, values below half way are rounded down)
            e.g. 0.41 rounds to 0.4, 0.45 rounds to 0.5, 0.48 rounds to 0.5
            if on the green list, the value is 0.0
            if on the red list, the value is 1.0
            being on the green list has precedence on the red list (e.g. if a call is on the green list and the red list, the risk score will be 0.0)
        """

        if call.attributes.green_list:
            return 0.0

        if call.attributes.red_list:
            return 1.0

        # convert to Decimal for precise rounding
        risk_score = Decimal(str(call.attributes.risk_score))

        # round to 1 decimal place using ROUND_HALF_UP
        rounded_score = float(
            risk_score.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        )

        return rounded_score
