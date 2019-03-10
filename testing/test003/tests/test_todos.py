from nose.tools import assert_is_not_none
from test003.services import get_todos


def test_request_response():
    response = get_todos()
    assert_is_not_none(response)
