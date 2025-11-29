import pytest
from compound_interest_calculator import compound_interest

def test_doubles_correctly(capsys):
    doubled_year = compound_interest(1000, 0.10, 20)
    assert doubled_year == 8
    captured = capsys.readouterr().out
    assert "Year 8:" in captured
    assert "The savings double after **8 years**." in captured

def test_does_not_double(capsys):
    doubled_year = compound_interest(1000, 0.01, 5)
    assert doubled_year is None
    captured = capsys.readouterr().out
    assert "The savings did NOT double" in captured

def test_exact_year_values(capsys):
    compound_interest(100, 0.10, 2)
    captured = capsys.readouterr().out
    assert "Year 1: £110.00" in captured
    assert "Year 2: £121.00" in captured