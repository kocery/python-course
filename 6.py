import unittest


def flatten(lst, depth=None):
    result = []
    for item in lst:
        if isinstance(item, list) and (depth is None or depth > 0):
            result.extend(flatten(item, None if depth is None else depth - 1))
        else:
            result.append(item)
    return result


class TestFlatten(unittest.TestCase):

    def test_flatten_full_depth(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8]), [1, 2, 4, 5, 6, 7, 8])

    def test_flatten_depth_1(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1), [1, 2, 4, 5, 6, [7], 8])

    def test_flatten_depth_2(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth=2), [1, 2, 4, 5, 6, 7, 8])

    def test_flatten_no_nested_lists(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_flatten_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_mixed_depth(self):
        self.assertEqual(flatten([1, [2, [3, [4, 5]]]], depth=2), [1, 2, 3, [4, 5]])

    def test_flatten_depth_zero(self):
        self.assertEqual(flatten([1, [2, [3, [4, 5]]]], depth=0), [1, [2, [3, [4, 5]]]])


if __name__ == '__main__':
    unittest.main()
