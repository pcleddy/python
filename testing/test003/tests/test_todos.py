from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
from test003.services import get_todos


@patch('test003.services.requests.get')
def test_getting_todos(mock_get):
    mock_get.return_value.ok = True
    response = get_todos()
    assert_is_not_none(response)
