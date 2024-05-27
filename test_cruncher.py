from unittest.mock import Mock
from cruncher import NumberCruncher
import pytest


def test_number_cruncher_likes_even_numbers():
    """Test that the crunch method saves number facts for even numbers.

    Given:
         A Number cruncher instance getting an even result for its "crunch" method (eg 42)

    Result:
        Method returns "Yum! 42"
        The tummy attribute contains a dict such as {'number': 42, "fact": "42 is the meaning of life."}

    """
    requester_mock = Mock()
    requester_mock.call.return_value = {
        "number": 42,
        "fact": "42 is the meaning of life.",
    }
    fact = NumberCruncher(1, requester_mock)
    assert fact.crunch() == "Yum! 42"
    assert isinstance(fact.tummy(), list)
    assert fact.tummy() == [{"number": 42, "fact": "42 is the meaning of life."}]


def test_number_cruncher_hates_odd_numbers():
    """Test that the crunch method rejects number facts for odd numbers.

    Given:
         A Number cruncher instance getting an odd result for its "crunch" method eg 13

    Result:
        Method returns "Yuk! 13"
        The tummy attribute is unchanged.

    """
    requester_mock = Mock()
    requester_mock.call.return_value = {"number": 13}
    fact = NumberCruncher(1, requester_mock)
    assert fact.crunch() == "Yuk! 13"
    assert isinstance(fact.tummy(), list)
    assert fact.tummy() == []


def test_number_cruncher_discards_oldest_item_when_tummy_full():
    """Test that the crunch method maintains a maximum number of facts.

    Given:
         A Number cruncher instance with tummy size 3 having 3 items in tummy getting
         an even result for its "crunch" method, eg 24.

    Result:
        Method deletes oldest result from tummy (eg 42)
        Method returns "Burp! 42"
        The tummy attribute contains 24 but not 42.

    """
    requester_mock = Mock()
    requester_mock.call.return_value = {
        "number": 42,
        "fact": "42 is the meaning of life.",
    }
    fact = NumberCruncher(2, requester_mock)
    fact.crunch()
    requester_mock.call.return_value = {"number": 24, "fact": "24 is a great age."}
    fact.crunch()
    requester_mock.call.return_value = {"number": 46, "fact": "46 is whatever."}
    assert fact.crunch() == "Burp! 42"
    assert fact.tummy()[0]["number"] == 24
    for e in fact.tummy():
        assert e["number"] != 42


def test_number_cruncher_raises_runtime_error_if_invalid_number_request():
    """Test that there is a runtime error if NumberRequester response is
    invalid

    Given:
        A NumberCruncher instance, receiving an invalid NumberRequester
        response (eg an AttributeError)

    Result:
        Raises RuntimeError
    """
    requester_mock = Mock()
    requester_mock.call.return_value = {"result": "FAILURE"}
    fact = NumberCruncher(2, requester_mock)

    with pytest.raises(RuntimeError) as re:
        fact.crunch()
    assert str(re.value) == "Unexpected error"


def test_invalid_tummy_size_entry():
    requester_mock = Mock()
    requester_mock.call.return_value = {"number": 13}
    with pytest.raises(ValueError) as re:
        NumberCruncher(-1, requester_mock)

    assert str(re.value) == "maxlen must be non-negative"
