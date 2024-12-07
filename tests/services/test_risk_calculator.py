import pytest
from src.models.call import Call, CallAttributes
from src.services.risk_calculator import RiskCalculator


@pytest.fixture
def calculator():
    return RiskCalculator()


def create_test_call(
    risk_score: float, green_list: bool = False, red_list: bool = False
) -> Call:
    """Helper function to create test call objects"""
    return Call(
        type="call",
        id="test-id",
        attributes=CallAttributes(
            date="2020-10-12T07:20:50.52Z",
            riskScore=risk_score,
            number="+441234567890",
            greenList=green_list,
            redList=red_list,
        ),
    )


def test_green_list_precedence(calculator):
    """Test that green list returns 0.0 even if on red list"""
    call = create_test_call(risk_score=0.8, green_list=True, red_list=True)
    assert calculator.calculate_risk_score(call) == 0.0


def test_red_list(calculator):
    """Test that red list returns 1.0 when not on green list"""
    call = create_test_call(risk_score=0.2, red_list=True)
    assert calculator.calculate_risk_score(call) == 1.0


def test_rounding_rules(calculator):
    """Test various rounding scenarios"""
    test_cases = [
        (0.41, 0.4),  # Below half - round down
        (0.44, 0.4),  # Below half - round down
        (0.45, 0.5),  # Exactly half - round up
        (0.46, 0.5),  # Above half - round up
        (0.48, 0.5),  # Above half - round up
        (0.01, 0.0),  # Edge case - near zero
        (0.99, 1.0),  # Edge case - near one
    ]

    for input_score, expected_score in test_cases:
        call = create_test_call(risk_score=input_score)
        assert calculator.calculate_risk_score(call) == expected_score


def test_no_special_lists(calculator):
    """Test normal rounding when not on any special lists"""
    call = create_test_call(risk_score=0.567)
    assert calculator.calculate_risk_score(call) == 0.6
