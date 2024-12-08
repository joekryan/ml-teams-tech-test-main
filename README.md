# ml-teams-tech-test
# Joe Ryan
```bash
ml-teams-tech-test-main/
├── src/
│   ├── __init__.py
│   ├── analyser.py          # Main CallAnalyser class
│   ├── models/
│   │   ├── __init__.py
│   │   ├── call.py         # Call data model
│   │   ├── operator.py     # Operator data model
│   │   └── validators.py   # Shared validation logic
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── operator_lookup.py    # Operator lookup logic
│   │   └── risk_calculator.py    # Risk score calculation logic
│
├── tests/
│   ├── __init__.py
│   ├── test_analyser.py    # Main analyser tests
│   ├── models/
│   │   ├── test_call.py
│   │   ├── test_operator.py
│   │   └── test_validators.py
│   └── services/
│       ├── test_operator_lookup.py
│       └── test_risk_calculator.py
│
├── data/                   # Sample data for testing
│   ├── calls.json
│   └── operators.json
│
├── pyproject.toml         # Poetry config & dependencies
├── .gitignore
└── README.md
```

## Overview

This system processes call data and operator information to:
- Match calls to network operators based on number prefixes
- Calculate risk scores following business rules
- Generate formatted CSV reports
- Sort and analyse call patterns

## Installation

### UV
install uv if not already installed
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

run uv to run the project

```bash
uv run -m src.main
```

## Pip

with python ">=3.12"
```bash
run pip install -r requirements.txt
```

activate your python environment and run

```bash
python -m src.main
```
This will:
1. Load call and operator data from JSON files in `data/`
2. Process the calls according to business rules
3. Generate a report at `data/report.csv`

# Business Rules

### Risk Score Calculation
- Rounded to 1 decimal place
- Green list calls: score = 0.0
- Red list calls: score = 1.0
- Green list takes precedence over red list

### Operator Matching
- Based on number prefix ranges
- Returns "Unknown" if no operator matches
- Uses "Withheld" for missing numbers

## Testing

Run the test suite:
```bash
pytest
```

## Further Work
1.	Enhanced Operator Matching Logic:
Currently, the operator lookup logic assumes all phone numbers follow a +XX 2 digit country code format. In the future, I could:
*Introduce support for multiple country codes.
*Implement more robust number parsing to handle various international formats or malformed inputs gracefully.
*Add configuration-driven operator ranges, making it easier to update or extend operator prefixes without code changes.

2.	More Resilient Input Validation:
The JSON data loading process could be improved by:
*Adding comprehensive validation for the structure and fields in the input JSON files.
*Providing more informative error messages when data is missing or malformed.

3.	Add Proper Logging and Monitoring

4.	Scalability and Performance:
As data volumes grow:
*Consider optimising data loading and transformations to handle larger datasets efficiently.
*Explore options for parallelising or caching operator lookups.

5. Continuous Integration and Deployment:
*Add CI/CD pipelines for automated testing, linting, and deployments.
*Integrate coverage reports and static analysis tools for continual quality improvement.
*Expand the test suite to include more edge cases and integration tests.

## Dependencies

- Python 3.12
- pandas: Data processing
- pydantic: Data validation
- pytest: Testing
