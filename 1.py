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


print(count_set_bits(31))  # Вывод: 5
print(count_set_bits(-123))  # Вывод: 3
