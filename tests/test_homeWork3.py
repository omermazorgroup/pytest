import pytest
import homeWork3
import logging

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture
def create_data_set():
    data_set = {
      "1": {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"},
      "2": {"name": "Tal", "sex": "male", "age": 22},
      "3": {"name": "Tali", "sex": "female", "age": 42},
      "4": {"name": "Adam", "sex": "male", "age": 18}
    }
    return data_set


@pytest.mark.homeWork3
def test_split_male_female(create_data_set):
    mylogger.info("test for split male and female function")
    male, female = homeWork3.split_male_female(create_data_set)
    assert len(male) + len(female) == len(create_data_set)


@pytest.mark.homeWork3
def test_find_median_average(create_data_set):
    mylogger.info("test for find median average function")
    average, median = homeWork3.find_median_average(create_data_set)
    sum1 = 0
    for item in create_data_set.values():
        sum1 += item["age"]
    assert average * len(create_data_set) == sum1


@pytest.mark.homeWork3
def test_print_values_above(capfd, create_data_set):
    mylogger.info("test for print values above function")
    homeWork3.print_values_above(create_data_set, 54)
    out, error = capfd.readouterr()
    res = list(eval(out))
    assert (homeWork3.print_values_above(create_data_set, 53),
            isinstance(homeWork3.print_values_above(create_data_set, 13), type(None)))
    assert len(res) < len(create_data_set)

