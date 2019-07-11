def test_data_guava_is_most_recent(data, guava):
    expect = (data / "guava.txt").open().read()
    actual = guava.open().read()
    assert expect == actual


def test_data_heck_is_most_recent(data, heck):
    expect = (data / "heck.txt").open().read()
    actual = heck.open().read()
    assert expect == actual


def test_guava_does_not_implement_unicode_grapheme(guava, heck):
    assert guava.open().read() != heck.open().read()
