import pytest
from src.linear_search import linear_search


def test_statement_coverage_valid_found():
    result = linear_search([10, 20, 30, 40, 50], 30)
    assert result == 2


def test_statement_coverage_valid_not_found():
    result = linear_search([10, 20, 30, 40, 50], 99)
    assert result == -1


def test_decision_coverage_invalid_type_for_v():
    with pytest.raises(TypeError):
        linear_search(None, 10)


def test_decision_coverage_invalid_length():
    with pytest.raises(ValueError):
        linear_search([1, 2, 3], 2)


def test_condition_coverage_invalid_key_type():
    with pytest.raises(TypeError):
        linear_search([1, 2, 3, 4, 5], 2.5)


def test_condition_coverage_invalid_element_type():
    with pytest.raises(TypeError):
        linear_search([1, 2, 3, None, 5], 3)


def test_loop_exits_early_when_key_found():
    result = linear_search([5, 6, 7, 8, 9], 5)
    assert result == 0


def test_loop_runs_until_end_when_key_not_found():
    result = linear_search([5, 6, 7, 8, 9], 10)
    assert result == -1