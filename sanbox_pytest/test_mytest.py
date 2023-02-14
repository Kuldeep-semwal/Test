from mytest import square

import pytest

@pytest.fixture
def input_value():
    return 4
def test_square_gives_correct_values():
    subject = square(input_value)

    assert subject == 16