from collections.abc import Hashable


def is_hashable(obj):
    return isinstance(obj, Hashable)


def reverse_dict(input_dict):
    reversed_dict = {}

    for key, value in input_dict.items():
        if not is_hashable(value):
            raise TypeError(f"Value '{value}' is not hashable.")

        if value in reversed_dict:
            if isinstance(reversed_dict[value], tuple):
                reversed_dict[value] = (*reversed_dict[value], key)
            else:
                reversed_dict[value] = (reversed_dict[value], key)
        else:
            reversed_dict[value] = key

    return reversed_dict


def test_invert_dict():
    assert reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ("Ivanov", "Kuznecov"),
                                                                                   55521: "Petrov"}, "Test case 1 failed"
    assert reverse_dict({"Ivanov": 12345, "Petrov": 67890}) == {12345: "Ivanov", 67890: "Petrov"}, "Test case 2 failed"
    assert reverse_dict({"Ivanov": 1, "Petrov": 1, "Kuznecov": 1}) == {
        1: ("Ivanov", "Petrov", "Kuznecov")}, "Test case 3 failed"

    try:
        reverse_dict({"Ivanov": [1, 2, 3], "Petrov": 67890})
    except TypeError as e:
        assert str(e) == "Value '[1, 2, 3]' is not hashable.", "Test case 4 failed"
    else:
        assert False, "Test case 4 failed - exception not raised"

    assert reverse_dict({}) == {}, "Test case 5 failed"
    assert reverse_dict({"Ivanov": "A", "Petrov": "B", "Kuznecov": "A"}) == {"A": ("Ivanov", "Kuznecov"),
                                                                             "B": "Petrov"}, "Test case 6 failed"

    print("All tests passed!")


test_invert_dict()
