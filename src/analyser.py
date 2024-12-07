from typing import List
import pandas as pd
from .models.call import Call
from .models.operator import Operator
from .services.operator_lookup import OperatorLookup
from .services.risk_calculator import RiskCalculator


class CallAnalyser:
    def __init__(self, operators: List[Operator]):
        self.operator_lookup = OperatorLookup(operators)
        self.risk_calculator = RiskCalculator()

    def analyse_calls(self, calls: List[Call]) -> pd.DataFrame:
        """
        Analyse calls and return DataFrame of analysed call data.
        Returns calls sorted by date with formatted date strings.
        """
        analysed_calls = [
            {
                "id": call.id,
                "date": call.attributes.date,
                "number": call.attributes.number,
                "operator": self.operator_lookup.get_operator_for_call(call),
                "riskScore": self.risk_calculator.calculate_risk_score(call),
            }
            for call in calls
        ]

        df = pd.DataFrame(analysed_calls)

        return df.sort_values(by="date").assign(
            date=lambda df_: df_.date.dt.strftime("%Y-%m-%d")
        )

    def write_csv_report(self, df: pd.DataFrame, output_path: str):
        """Write analysed calls DataFrame to CSV file"""
        df.to_csv(output_path, index=False)
