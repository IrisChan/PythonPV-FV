import pytest
from indexOOP import *

@pytest.fixture
def fmodelWithFV():
    return {
        "rate": 0.05, 
        "fv": 1000, 
        "nPeriods": 3
    }

@pytest.fixture
def fmodelWithFV_nPeriodsSmallerThenZero():
    return {
        "rate": 0.05,
        "fv": 1000,
        "nPeriods": -3
    }

@pytest.fixture
def fmodelComputeDelta():
    return [
        {"rate": 0.07, "fv": 500, "nPeriods": 1},
        {"rate": 0.095, "fv": 750, "nPeriods": 3}
    ]