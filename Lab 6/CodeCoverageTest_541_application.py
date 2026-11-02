
import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


# Extra time charge test cases
def test_extra_time_charge():
    assert extra_time_charge("haircut", 20, "junior", False) == 0
    assert extra_time_charge("haircut", 60, "junior", False) == 300
    assert extra_time_charge("colour", 80, "senior", False) == 360
    assert extra_time_charge("spa", 100, "junior", True) == 100

    # Additional cases for complete code coverage
    assert extra_time_charge("haircut", 100, "junior", True) == 550
    assert extra_time_charge("haircut", 120, "junior", False) == 1620
    assert extra_time_charge("haircut", 120, "senior", False) == 2700


# Invalid input test cases
def test_invalid_service():
    with pytest.raises(ValueError):
        extra_time_charge("nail", 30, "junior", False)


def test_invalid_duration():
    with pytest.raises(ValueError):
        extra_time_charge("haircut", -5, "junior", False)


# Booking test cases
def test_can_book():
    assert can_book(2, 1, True) is True
    assert can_book(3, 1, True) is False
    assert can_book(2, 1, False) is True
    assert can_book(5, 1, False) is False
    assert can_book(2, 3, False) is False


# Arrival status test cases
def test_arrival_status():
    assert arrival_status(20, True, True) == "open"
    assert arrival_status(5, False, False) == "open"
    assert arrival_status(0, True, False) == "late"
    assert arrival_status(-20, False, False) == "closed"
