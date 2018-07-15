import pytest
from decimal import *
from indexOOP import *

def test_compute_pv_with_fv(fmodelWithFV):
    cal = Calculations()
    assert cal.computePV(fmodelWithFV["fv"], fmodelWithFV["rate"], fmodelWithFV["nPeriods"]) == Decimal('863.84')

def test_compute_pv_with_fv_but_nPeriods_smaller_than_zero(fmodelWithFV_nPeriodsSmallerThenZero):
    with pytest.raises(Exception):
        cal = Calculations()
        cal.computePV(fmodelWithFV_nPeriodsSmallerThenZero["fv"], fmodelWithFV_nPeriodsSmallerThenZero["rate"], 
           fmodelWithFV_nPeriodsSmallerThenZero["nPeriods"])

def test_compute_delta(fmodelComputeDelta):
    cal = Calculations()
    info1 = fmodelComputeDelta[0]
    info2 = fmodelComputeDelta[1]
    assert cal.computeDelta(info1["fv"], info1["rate"], info1["nPeriods"],
                            info2["fv"], info2["rate"], info2["nPeriods"]) == Decimal('4158.03')