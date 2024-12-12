#!/usr/bin/env python
import math


def get_divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def main() -> None:
    with open("input") as f:
        minimum_gifts = int(f.read().strip())

    minimum_sum = minimum_gifts // 10
    i = 0
    while True:
        i += 1
        sum_divisors = sum(get_divisors(i))
        if sum_divisors >= minimum_sum:
            break

    print(i)


if __name__ == "__main__":
    main()
