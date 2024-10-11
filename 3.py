def create_matrix(s):
    return [list(map(float, _.split(" "))) for _ in s.split(" | ")]


def test_parse_matrix():
    assert create_matrix("1 2 | 3 4") == [[1.0, 2.0], [3.0, 4.0]], "Test case 1 failed"
    assert create_matrix("0.5 1.2 | 3.4 4.5") == [[0.5, 1.2], [3.4, 4.5]], "Test case 2 failed"
    assert create_matrix("1 2 3") == [[1.0, 2.0, 3.0]], "Test case 3 failed"
    assert create_matrix("1 | 2 | 3") == [[1.0], [2.0], [3.0]], "Test case 4 failed"
    assert create_matrix("1 2.5 | -3 4.0 | 5.25 6") == [[1.0, 2.5], [-3.0, 4.0], [5.25, 6.0]], "Test case 5 failed"
    assert create_matrix("-1 -2 | -3 -4") == [[-1.0, -2.0], [-3.0, -4.0]], "Test case 6 failed"
    assert create_matrix("1e3 2.5e-3 | 1.0e2 -2.5e1") == [[1000.0, 0.0025], [100.0, -25.0]], "Test case 7 failed"
    assert create_matrix("1 2 | 3") == [[1.0, 2.0], [3.0]], "Test case 8 failed"
    assert create_matrix("42") == [[42.0]], "Test case 9 failed"

    print("All tests passed!")


test_parse_matrix()
