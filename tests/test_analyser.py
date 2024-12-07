import pytest
import pandas as pd
from src.models.call import Call, CallAttributes
from src.models.operator import Operator, OperatorAttributes
from src.analyser import CallAnalyser
import tempfile
from pathlib import Path


@pytest.fixture
def operators():
    return [
        Operator(
            type="operator",
            id="1",
            attributes=OperatorAttributes(prefix="2000", operator="EE"),
        )
    ]


@pytest.fixture
def calls():
    return [
        Call(
            type="call",
            id="1",
            attributes=CallAttributes(
                date="2020-01-01T12:00:00Z",
                riskScore=0.5,
                number="+442123456789",
                greenList=False,
                redList=False,
            ),
        ),
        Call(
            type="call",
            id="2",
            attributes=CallAttributes(
                date="2019-01-01T12:00:00Z",
                riskScore=0.8,
                number="+441234567890",
                greenList=True,
                redList=False,
            ),
        ),
    ]


@pytest.fixture
def analyser(operators):
    return CallAnalyser(operators)


def test_analyse_calls(analyser, calls):
    """Test that calls are analysed correctly and sorted by date"""
    df = analyser.analyse_calls(calls)

    assert len(df) == 2
    # Check sorting
    assert df.iloc[0]["id"] == "2"  # 2019 call should be first
    assert df.iloc[1]["id"] == "1"  # 2020 call should be second

    # Check first call details
    assert df.iloc[0]["date"] == "2019-01-01"
    assert df.iloc[0]["number"] == "+441234567890"
    assert df.iloc[0]["operator"] == "Unknown"
    assert df.iloc[0]["riskScore"] == 0.0  # Green list

    # Check second call details
    assert df.iloc[1]["date"] == "2020-01-01"
    assert df.iloc[1]["number"] == "+442123456789"
    assert df.iloc[1]["operator"] == "EE"
    assert df.iloc[1]["riskScore"] == 0.5


def test_write_csv_report(analyser, calls):
    """Test CSV report generation"""
    df = analyser.analyse_calls(calls)

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "test_report.csv"
        analyser.write_csv_report(df, output_path)

        # Read and verify CSV
        result_df = pd.read_csv(output_path)
        assert len(result_df) == 2
        assert result_df.iloc[0]["date"] == "2019-01-01"
        assert result_df.iloc[1]["date"] == "2020-01-01"
