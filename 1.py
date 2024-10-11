def count_set_bits(n):
    count = 0
    f = False
    if n < 0:
        n = ~n
        f = True

    while n > 0:
        count += not (n & 1) if f else n & 1
        n >>= 1

    return count + 1 if f else count


def test_count_set_bits():
    assert count_set_bits(10) == 2, "Test case 1 failed"  # 10 -> 0...1010
    assert count_set_bits(0) == 0, "Test case 2 failed"  # 0 -> 0
    assert count_set_bits(1) == 1, "Test case 3 failed"  # 1 -> 0...1
    assert count_set_bits(1023) == 10, "Test case 4 failed"  # 1023 -> 0...1111111111 (10 единиц)
    assert count_set_bits(-1) == 1, "Test case 5 failed"  # -1 -> 1...1 (все биты установлены, но считаем 1 раз)
    assert count_set_bits(-10) == 3, "Test case 6 failed"  # -10 -> 1...0110
    assert count_set_bits(-123) == 3, "Test case 7 failed"  # -123 -> 1...0000101 (3 единицы)
    assert count_set_bits(-1023) == 2, "Test case 8 failed"  # -1023 -> 1...0000000001 (2 единицы)
    assert count_set_bits(
        2 ** 31 - 1) == 31, "Test case 9 failed"  # Максимальное положительное 32-битное число (31 единица)
    assert count_set_bits(
        -2 ** 31) == 1, "Test case 10 failed"  # Минимальное отрицательное 32-битное число (одна единица)

    print("All tests passed!")


test_count_set_bits()
