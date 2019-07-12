def test_matches_unit_heck_custompy(heck_unit, custompy_unit):
    expect = heck_unit.open().read()
    actual = custompy_unit.open().read()
    assert expect == actual
