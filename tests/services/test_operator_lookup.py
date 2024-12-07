import pytest
from src.models.operator import Operator, OperatorAttributes
from src.models.call import Call, CallAttributes
from src.services.operator_lookup import OperatorLookup


@pytest.fixture
def operators():
    return [
        Operator(
            type="operator",
            id="1",
            attributes=OperatorAttributes(prefix="2000", operator="EE"),
        ),
        Operator(
            type="operator",
            id="2",
            attributes=OperatorAttributes(prefix="3000", operator="Vodafone"),
        ),
    ]


@pytest.fixture
def lookup(operators):
    return OperatorLookup(operators)


def test_get_operator_for_call_matching_operator(lookup):
    """Test operator lookup returns correct operator when number matches"""
    call = Call(
        type="call",
        id="123",
        attributes=CallAttributes(
            date="2020-10-12T07:20:50.52Z",
            riskScore=0.5,
            number="+442123456789",
            greenList=False,
            redList=False,
        ),
    )
    assert lookup.get_operator_for_call(call) == "EE"


def test_get_operator_for_call_no_matching_operator(lookup):
    """Test operator lookup returns 'Unknown' when no operator matches"""
    call = Call(
        type="call",
        id="123",
        attributes=CallAttributes(
            date="2020-10-12T07:20:50.52Z",
            riskScore=0.5,
            number="+441234567890",
            greenList=False,
            redList=False,
        ),
    )
    assert lookup.get_operator_for_call(call) == "Unknown"
