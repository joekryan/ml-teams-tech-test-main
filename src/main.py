import json
from pathlib import Path
from .models.call import Call
from .models.operator import Operator
from .analyser import CallAnalyser


def main():
    """
    main function to combine everything
    1. load call and opeartor json files
    2. process calls using CallAnalyser
    3. Generate CSV report.
    """

    data_dir = Path("data")

    with open(data_dir / "calls.json", "r") as f:
        calls_data = json.load(f)
        calls = [Call.model_validate(call) for call in calls_data["data"]]

    with open(data_dir / "operators.json", "r") as f:
        operators_data = json.load(f)
        operators = [
            Operator.model_validate(operator) for operator in operators_data["data"]
        ]

    analyser = CallAnalyser(operators)
    analysed_calls = analyser.analyse_calls(calls)

    output_path = data_dir / "report.csv"
    analyser.write_csv_report(analysed_calls, output_path)

    print(f"Report written to {output_path}")


if __name__ == "__main__":
    main()
