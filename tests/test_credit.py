"""Tests unitaires de calculate_risk()."""

import pytest

from credit import calculate_risk


# Partie A - Cas normaux
def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"


# Partie B - Cas limites
def test_zero_income_raises_error():
    with pytest.raises(ValueError):
        calculate_risk(0, 100, 30)


def test_negative_income_raises_error():
    with pytest.raises(ValueError):
        calculate_risk(-1000, 100, 30)


def test_zero_debt_is_low_risk():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_0_3_is_low_risk():
    # 300 / 1000 = 0.3 : la condition est "> 0.3", donc pas MEDIUM
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_0_6_is_medium_risk():
    # 600 / 1000 = 0.6 : la condition est "> 0.6", donc pas HIGH
    assert calculate_risk(1000, 600, 30) == "MEDIUM"


# Entrées invalides supplémentaires
def test_negative_debt_raises_error():
    with pytest.raises(ValueError):
        calculate_risk(1000, -50, 30)


def test_minor_client_raises_error():
    with pytest.raises(ValueError):
        calculate_risk(1000, 100, 17)


@pytest.mark.parametrize(
    ("income", "debt", "expected"),
    [
        (1000, 301, "MEDIUM"),
        (1000, 601, "HIGH"),
        (2000, 2000, "HIGH"),
    ],
)
def test_values_just_above_thresholds(income, debt, expected):
    assert calculate_risk(income, debt, 30) == expected
