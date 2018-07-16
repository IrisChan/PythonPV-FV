import pytest
from index import *

@pytest.fixture
def fmodelWithFV():
    return {
        "rate": 0.095, 
        "fv": 750, 
        "nPeriods": 3,
        "pv": 571.25
    }

@pytest.fixture
def fmodelWithFV_nPeriodsSmallerThenZero():
    return {
        "rate": 0.05,
        "fv": 1000,
        "nPeriods": -3
    }

@pytest.fixture
def fmodelWithFV_list():
    return [
        FModel(0.085, 3, fv=500),
        FModel(0.075, 2, fv=250),
        FModel(0.1, 5, fv=600)
    ]

@pytest.fixture
def fmodelWithFV_list_PV():
    return [
        391.46,
        216.34,
        372.56
    ]

@pytest.fixture
def fmodelComputeDelta():
    return [
        {"rate": 0.085, "fv": 500, "nPeriods": 1},
        {"rate": 0.095, "fv": 750, "nPeriods": 3},
        {"delta": 11041.09}
    ]