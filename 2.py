def my_zip(x, y):
    return [(x[_], y[_]) for _ in range(min(len(x), len(y)))]


def test_custom_zip():
    assert my_zip([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")], "Test case 1 failed"
    assert my_zip([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")], "Test case 2 failed"
    assert my_zip([1, 2], ["a", "b", "c"]) == [(1, "a"), (2, "b")], "Test case 3 failed"
    assert my_zip([1, 2, 3], ["x", "y", "z"]) == [(1, "x"), (2, "y"), (3, "z")], "Test case 4 failed"
    assert my_zip(["a", "b", "c"], [1, 2, 3]) == [("a", 1), ("b", 2), ("c", 3)], "Test case 5 failed"
    assert my_zip([], ["a", "b", "c"]) == [], "Test case 6 failed"
    assert my_zip([1, 2, 3], []) == [], "Test case 7 failed"
    assert my_zip([], []) == [], "Test case 8 failed"

    print("All tests passed!")


test_custom_zip()
