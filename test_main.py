from main import compare


def test_compare():
    assert compare(2, 1) is True
    assert compare(1, 2) is False
    assert compare(1, 1) is False


if __name__ == "__main__":
    test_compare()
