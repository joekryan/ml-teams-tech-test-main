import pytest
from src.models.operator import Operator, OperatorAttributes
from pydantic import ValidationError


def test_valid_operator():
    """Test that an operator is valid"""
    Operator(
        type="operator",
        id="test-id",
        attributes=OperatorAttributes(
            prefix="2000",
            operator="EE",
        ),
    )


def test_prefix_validation():
    """Test prefix must be 4 digits ending in '000'"""
    invalid_prefixes = [
        "123",  # too short
        "12345",  # too long
        "2001",  # doesn't end in 000
        "0000",  # can't start with 0
        "abcd",  # not digits
        "a000",  # not digits
    ]

    for prefix in invalid_prefixes:
        with pytest.raises(ValidationError):
            Operator(
                type="operator",
                id="test-id",
                attributes=OperatorAttributes(prefix=prefix, operator="Vodafone"),
            )


def test_type_validation():
    """Test type must be 'operator'"""
    with pytest.raises(ValidationError):
        Operator(
            type="not-operator",
            id="test-id",
            attributes=OperatorAttributes(prefix="2000", operator="Vodafone"),
        )


def test_number_in_range():
    """Test number range checking logic"""
    operator = Operator(
        type="operator",
        id="test-id",
        attributes=OperatorAttributes(prefix="2000", operator="Vodafone"),
    )

    # Numbers in 2000-2999 range should return True
    assert operator.attributes.is_number_in_range("+442143999888")
    assert operator.attributes.is_number_in_range("+332143999888")
    assert operator.attributes.is_number_in_range("+012143999888")

    # Numbers outside 2000-2999 range should return False
    assert not operator.attributes.is_number_in_range("+443000123456")
    assert not operator.attributes.is_number_in_range("+441999123456")
    assert not operator.attributes.is_number_in_range("+448423666777")
