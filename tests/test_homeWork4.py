import pytest
from homeWork4 import Date
import logging

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture
def new_date():
    date1 = Date(2, 12, 1998)
    return date1


@pytest.fixture
def fake_date():
    try:
        date4 = Date(29, 2, 1991)
        return True
    except:
        return False


@pytest.mark.homeWork4
def test_str(new_date):
    mylogger.info("test for str function")
    assert new_date.__str__() == "2.12.1998"


@pytest.mark.homeWork4
def test_eq(new_date):
    mylogger.info("test for eq function")
    assert new_date == Date(2, 12, 1998)


@pytest.mark.homeWork4
def test_gt(new_date):
    mylogger.info("test for gt function")
    assert new_date > Date(2, 3, 1990)


@pytest.mark.homeWork4
def test_ge(new_date):
    mylogger.info("test for ge function")
    assert new_date >= Date(2, 12, 1998)
    assert new_date >= Date(13, 4, 1991)


@pytest.mark.homeWork4
def test_lt(new_date):
    mylogger.info("test for lt function")
    assert new_date < Date(13, 4, 2010)


@pytest.mark.homeWork4
def test_le(new_date):
    mylogger.info("test for le function")
    assert new_date <= Date(2, 12, 1998)
    assert new_date <= Date(3, 12, 1998)


@pytest.mark.homeWork4
def test_sub(new_date):
    mylogger.info("test for sub function")
    assert new_date - Date(2, 12, 1998) == 0
    assert new_date - Date(3, 4, 1980) > 0


@pytest.mark.homeWork4
def test_is_valid(fake_date):
    mylogger.info("test for isValid function")
    assert fake_date is not True


@pytest.mark.homeWork4
def test_get_next_day(new_date):
    mylogger.info("test for getNextDay function")
    assert new_date.getNextDay() == Date(3, 12, 1998)
    assert new_date.getNextDay() != Date(2, 12, 1998)


@pytest.mark.homeWork4
def test_get_next_days(new_date):
    mylogger.info("test for getNextDays function")
    assert new_date.getNextDays(5) == Date(7, 12, 1998)
    assert new_date.getNextDays(0) == Date(2, 12, 1998)


