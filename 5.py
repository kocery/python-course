import unittest


def sum(x, y):
    return x + y


def specialize(fun, *args, **kwargs):
    def f(*extra_args, **extra_kwargs):
        return fun(*args, *extra_args, **kwargs, **extra_kwargs)

    return f


class TestSpecialize(unittest.TestCase):

    def test_specialize_with_single_keyword_argument(self):
        plus_one = specialize(sum, y=1)
        self.assertEqual(plus_one(10), 11, "Failed when y=1 was provided as a keyword argument")

    def test_specialize_with_both_positional_arguments(self):
        just_two = specialize(sum, 1, 1)
        self.assertEqual(just_two(), 2, "Failed when both arguments were provided positionally")

    def test_specialize_with_additional_positional_arguments(self):
        partial_sum = specialize(sum, 5)
        self.assertEqual(partial_sum(3), 8, "Failed when one argument was pre-set, and the second was provided later")

    def test_specialize_with_additional_keyword_argument(self):
        partial_sum = specialize(sum, x=4)
        self.assertEqual(partial_sum(y=6), 10,
                         "Failed when one argument was pre-set as a keyword argument and the second was provided later as a keyword")

    def test_specialize_with_no_predefined_arguments(self):
        dynamic_sum = specialize(sum)
        self.assertEqual(dynamic_sum(4, 7), 11,
                         "Failed when no arguments were pre-set, and both were provided at call time")


if __name__ == '__main__':
    unittest.main()
