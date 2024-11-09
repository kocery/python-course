def reverse_dict(input_dict):
    reversed_dict = {}

    for key, value in input_dict.items():
        if value in reversed_dict:
            if isinstance(reversed_dict[value], tuple):
                reversed_dict[value] = (*reversed_dict[value], key)
            else:
                reversed_dict[value] = (reversed_dict[value], key)
        else:
            reversed_dict[value] = key

    return reversed_dict


import pytest


def test_reverse_dict_cases():
    assert reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ("Ivanov", "Kuznecov"),
                                                                                   55521: "Petrov"}
    assert reverse_dict({"Ivanov": 12345, "Petrov": 67890}) == {12345: "Ivanov", 67890: "Petrov"}
    assert reverse_dict({"Ivanov": 1, "Petrov": 1, "Kuznecov": 1}) == {1: ("Ivanov", "Petrov", "Kuznecov")}
    assert reverse_dict({}) == {}
    assert reverse_dict({"Ivanov": "A", "Petrov": "B", "Kuznecov": "A"}) == {"A": ("Ivanov", "Kuznecov"), "B": "Petrov"}


def test_reverse_dict_with_unhashable_value():
    with pytest.raises(TypeError, match="unhashable type: 'list'"):
        reverse_dict({"Ivanov": [1, 2, 3], "Petrov": 67890})
