import pytest
from datetime import datetime
from src.models.call import Call, CallAttributes
from pydantic import ValidationError


def test_risk_score_validation():
    """Test the risk score validation rules"""
    # Should fail for scores outside 0-1 range
    invalid_scores = [-0.1, 1.1, 2.0, -5]
    for score in invalid_scores:
        with pytest.raises(ValidationError):
            Call(
                type="call",
                id="123",
                attributes=CallAttributes(
                    date="2020-10-12T07:20:50.52Z",
                    riskScore=score,
                    greenList=False,
                    redList=False,
                ),
            )

    # Should accept valid scores
    valid_scores = [0, 0.5, 1, 0.1, 0.99]
    for score in valid_scores:
        Call(
            type="call",
            id="123",
            attributes=CallAttributes(
                date="2020-10-12T07:20:50.52Z",
                riskScore=score,
                greenList=False,
                redList=False,
            ),
        )


def test_date_parsing():
    """Test that dates are correctly converted to datetime objects"""
    call = Call(
        type="call",
        id="123",
        attributes=CallAttributes(
            date="2020-10-12T07:20:50.52Z",
            riskScore=0.5,
            greenList=False,
            redList=False,
        ),
    )
    assert isinstance(call.attributes.date, datetime)
    assert call.attributes.date.year == 2020
    assert call.attributes.date.month == 10
    assert call.attributes.date.day == 12


def test_optional_number():
    """Test that number field is optional"""
    # Should work with number
    Call(
        type="call",
        id="123",
        attributes=CallAttributes(
            date="2020-10-12T07:20:50.52Z",
            riskScore=0.5,
            greenList=False,
            redList=False,
            number="+44123456789",
        ),
    )

    # Should also work without number
    Call(
        type="call",
        id="123",
        attributes=CallAttributes(
            date="2020-10-12T07:20:50.52Z",
            riskScore=0.5,
            greenList=False,
            redList=False,
        ),
    )
