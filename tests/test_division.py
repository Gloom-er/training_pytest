from my_funcs.main import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divider, divis", [(ZeroDivisionError, 0, 10),
                                                                (TypeError, "2", 20)])
def test_zero_division_with_error(expected_exception, divider, divis):
    with pytest.raises(expected_exception):
        division(divis, divider)
