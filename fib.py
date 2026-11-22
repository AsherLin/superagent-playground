"""Print the first 20 terms of the Fibonacci sequence."""


def fibonacci(count):
    """Return the first ``count`` Fibonacci numbers: 1, 1, 2, 3, 5, ..."""
    terms = []
    a, b = 1, 1
    for _ in range(count):
        terms.append(a)
        a, b = b, a + b
    return terms


def main():
    print(*fibonacci(20))


if __name__ == "__main__":
    main()
