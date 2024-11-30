import unittest


def cycle(iterable):
    while True:
        yield from iterable


def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def take(iterable, count=-1):
    if count == -1:
        yield from iterable
    for _, e in zip(range(count), iterable):
        yield e


class TestCycleFunction(unittest.TestCase):
    def test_cycle_with_finite_take(self):
        result = list(take(cycle([1, 2, 3]), 10))
        expected = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
        self.assertEqual(result, expected)


class TestChainFunction(unittest.TestCase):
    def test_chain_with_lists(self):
        result = list(chain([1, 2], [3, 4]))
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_chain_with_strings(self):
        result = list(chain("ab", "cd"))
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(result, expected)

    def test_chain_with_mixed_iterables(self):
        result = list(chain([1, 2], "hello", (3, 4)))
        expected = [1, 2, 'h', 'e', 'l', 'l', 'o', 3, 4]
        self.assertEqual(result, expected)


class TestTakeFunction(unittest.TestCase):
    def test_take_with_default_count(self):
        result = list(take([1, 2, 3]))
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_take_with_positive_count(self):
        result = list(take([1, 2, 3, 4, 5], 3))
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_take_with_count_zero(self):
        result = list(take([1, 2, 3], 0))
        expected = []
        self.assertEqual(result, expected)

    def test_take_with_negative_count(self):
        result = list(take([1, 2, 3], -5))
        expected = []
        self.assertEqual(result, expected)

    def test_take_with_count_exceeding_length(self):
        result = list(take([1, 2, 3], 5))
        expected = [1, 2, 3]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
