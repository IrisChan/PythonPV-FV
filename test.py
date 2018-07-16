import pytest
from decimal import *
from index import *

def test_compute_pv_with_fv(fmodelWithFV):
    cal = Calculations()
    assert cal.computePV(fmodelWithFV["fv"], fmodelWithFV["rate"], fmodelWithFV["nPeriods"]) == Decimal(str(fmodelWithFV["pv"]))

def test_compute_pv_with_fv_but_nPeriods_smaller_than_zero(fmodelWithFV_nPeriodsSmallerThenZero):
    with pytest.raises(ValueError):
        cal = Calculations()
        cal.computePV(fmodelWithFV_nPeriodsSmallerThenZero["fv"], fmodelWithFV_nPeriodsSmallerThenZero["rate"], 
           fmodelWithFV_nPeriodsSmallerThenZero["nPeriods"])

def test_compute_pv_with_fv_for_list(fmodelWithFV_list, fmodelWithFV_list_PV):
    cal = Calculations()
    res = cal.computePVfromListOfInput(fmodelWithFV_list)

    assert len(res) == len(fmodelWithFV_list_PV)
    for amount, expected in zip(res, fmodelWithFV_list_PV):
        assert amount == Decimal(str(expected))

def test_compute_delta(fmodelComputeDelta):
    cal = Calculations()
    info1 = fmodelComputeDelta[0]
    info2 = fmodelComputeDelta[1]
    info3 = fmodelComputeDelta[2]
    assert cal.computeDelta(info1["fv"], info1["rate"], info1["nPeriods"],
                            info2["fv"], info2["rate"], info2["nPeriods"]) == Decimal(str(info3["delta"]))