import random
from src.linear_search import linear_search
from oracle import oracle_linear_search


def test_random_generated_cases_100():
    random.seed(42)

    for _ in range(100):
        v = [random.randint(-10, 10) for _ in range(5)]
        key = random.randint(-10, 10)

        expected = oracle_linear_search(v, key)
        actual = linear_search(v, key)

        assert actual == expected


def test_random_generated_cases_500():
    random.seed(123)

    for _ in range(500):
        v = [random.randint(-100, 100) for _ in range(5)]
        key = random.randint(-100, 100)

        expected = oracle_linear_search(v, key)
        actual = linear_search(v, key)

        assert actual == expected