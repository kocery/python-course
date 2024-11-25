import unittest


def flatten(lst, depth=-1):
    """
    Функция для "сплющивания" вложенных списков до указанной глубины.

    :param lst: Список, который нужно сплющить.
    :param depth: Глубина, до которой нужно сплющить список.
                  -1 означает бесконечную глубину.
    :return: Сплющенный список.
    :raises ValueError: Если depth отрицательный и не равен -1.
    """
    if not isinstance(depth, int):
        raise TypeError("depth должен быть целым числом.")
    if depth < -1:
        raise ValueError("depth не может быть отрицательным, кроме -1 для бесконечной глубины.")

    result = []
    for item in lst:
        if isinstance(item, list):
            if depth > 0:
                # Сплющиваем с уменьшением глубины
                result.extend(flatten(item, depth - 1))
            elif depth == -1:
                # Бесконечная глубина
                result.extend(flatten(item, depth))
            else:
                # Текущая глубина достигнута, добавляем как есть
                result.append(item)
        else:
            result.append(item)
    return result


class TestFlatten(unittest.TestCase):

    def test_flatten_full_depth_default(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8]), [1, 2, 4, 5, 6, 7, 8])

    def test_flatten_full_depth_minus_one(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth=-1), [1, 2, 4, 5, 6, 7, 8])

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

    def test_flatten_negative_depth(self):
        with self.assertRaises(ValueError):
            flatten([1, 2, [3]], depth=-2)

    def test_flatten_non_integer_depth(self):
        with self.assertRaises(TypeError):
            flatten([1, 2, [3]], depth=1.5)

    def test_flatten_depth_minus_one(self):
        self.assertEqual(flatten([1, [2, [3, [4, 5]]]], depth=-1), [1, 2, 3, 4, 5])

    def test_flatten_depth_large_number(self):
        # Тестируем с большим числом, которое по сути эквивалентно бесконечной глубине
        self.assertEqual(flatten([1, [2, [3, [4, 5]]]], depth=100), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
