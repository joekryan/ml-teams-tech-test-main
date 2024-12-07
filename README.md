# ml-teams-tech-test
## Joe Ryan

ml-teams-tech-test-main/
├── src/
│   ├── __init__.py
│   ├── analyzer.py          # Main CallAnalyzer class
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
│   ├── conftest.py         # Shared test fixtures
│   ├── test_analyzer.py    # Main analyzer tests
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
└── README.mdour name here)
