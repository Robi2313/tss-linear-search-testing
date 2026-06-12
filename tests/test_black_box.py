import pytest
from src.linear_search import linear_search


def test_key_on_first_position():
    assert linear_search([7, 1, 2, 3, 4], 7) == 0


def test_key_in_middle_position():
    assert linear_search([1, 2, 7, 3, 4], 7) == 2


def test_key_on_last_position():
    assert linear_search([1, 2, 3, 4, 7], 7) == 4


def test_key_not_found():
    assert linear_search([1, 2, 3, 4, 5], 9) == -1


def test_first_occurrence_is_returned():
    assert linear_search([3, 1, 3, 4, 3], 3) == 0


def test_invalid_list_length_too_short():
    with pytest.raises(ValueError):
        linear_search([1, 2, 3, 4], 3)


def test_invalid_list_length_too_long():
    with pytest.raises(ValueError):
        linear_search([1, 2, 3, 4, 5, 6], 3)


def test_invalid_input_not_list():
    with pytest.raises(TypeError):
        linear_search("12345", 3)


def test_invalid_key_type():
    with pytest.raises(TypeError):
        linear_search([1, 2, 3, 4, 5], "3")


def test_invalid_element_type():
    with pytest.raises(TypeError):
        linear_search([1, 2, "3", 4, 5], 3)