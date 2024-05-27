from unittest.mock import patch
from cruncher import NumberRequester
from freezegun import freeze_time


@patch("cruncher.requests.get")
def test_number_requester_returns_a_valid_result_when_called(mock_call):
    """Test that the call method returns a valid item.

    Given:
         A NumberRequester instance making a successful call

    Result:
        A result as a dict in the form {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}

    """
    requester_mock = mock_call.return_value
    requester_mock.status_code = 200
    requester_mock.text = "13 is lucky for some."

    test = NumberRequester()

    assert test.call() == {
        "result": "SUCCESS",
        "number": 13,
        "fact": "13 is lucky for some.",
    }


@patch("cruncher.requests.get")
def test_number_requester_returns_error_result_for_non_200_response(mock_call):
    """Test that the call method returns a valid item when a request fails.

    Given:
         A NumberRequester instance making an unsuccessful call

    Result:
        A result as a dict in the form {'result': 'FAILURE', 'error_code': 404}

    """
    requester_mock = mock_call.return_value
    requester_mock.status_code = 404
    requester_mock.text = ""

    test = NumberRequester()

    assert test.call() == {"result": "FAILURE", "error_code": 404}


@patch("cruncher.requests.get")
def test_number_requester_keeps_log_of_requests(mock_call):
    """Test that a NumberRequester instance keeps a log of its own requests.

    Given:
        A NumberRequester is instantiated.
        The NumberRequester.call method is called 5 times at known times.

    Result:
        The NumberRequester.log attribute returns a array of five valid results. Each result
        is a serialisable dict in the form:
        {'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math',
        'result': 'SUCCESS', 'number': 49}
    Ensure that you test that each dict is exactly correct - including the 'call_time'.
    """

    requester_mock = mock_call.return_value
    requester_mock.status_code = 200
    requester_mock.text = "49"

    test = NumberRequester()

    times = ["2024-05-02T16:45:01", "2024-05-02T16:46:01", "2024-05-02T16:47:01", "2024-05-02T16:48:01", "2024-05-02T16:49:01"]

    for i in range(5): 
        freezer = freeze_time(times[i])
        freezer.start()
        test.call()
        freezer.stop()    
        assert test.log[i]["request_number"] == i + 1        
        assert test.log[i]["call_time"] == times[i]            
        assert test.log[i]["end_point"] == "http://numbersapi.com/random/math"
        assert test.log[i]["result"] == "SUCCESS"
        assert test.log[i]["number"] == 49

    assert len(test.log) == 5
