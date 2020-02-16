import something_test_to_see
from unittest import mock

@mock.patch('something_test_to_see.sum_random')
def test_random_sum(magic_mock):
    magic_mock.return_value = 5
    assert something_test_to_see.sum_random(2,3) == 5
