import os,sys
import subprocess
import glob
from os import path


def split_male_female(d: dict) -> tuple[dict, dict]:
    """
        A function that get dictionary as a parameter and returns 2 dictionaries -
        one for the elements where the "sex" field is equal to "male" and the other for
        the elements where the "sex" field is equal to "female"
        :param d: dictionary
        :return: two dictionaries, one for sex: female and the other for sex: male
    """
    if type(d) is not dict:
        print("TypeError: split_male_female's parameter must be a dictionary")
        return {}, {}
    male = {}
    female = {}
    for details in d.values():
        if details['sex'] == 'male':
            male[details['name']] = details
        elif details['sex'] == 'female':
            female[details['name']] = details
    return female, male


def find_median_average(d: dict) -> tuple[float, float]:
    """
        A function that get a dictionary,  finds the average age and median age of the ages inside the dictionaries
        of the given dictionary and print them
        :param d: dictionary
        :return: None
    """
    if type(d) is not dict:
        print("TypeError: find_median_average's parameter must be a dictionary")
        return 0, 0
    ages = []
    for details in d.values():
        ages.append(details['age'])
    print("The average age in the dictionary is " + str(sum(ages)/len(ages)))
    average = sum(ages)/len(ages)
    print("and the median age is", end=" ")
    ages.sort()
    if len(ages) % 2 != 0:
        print(ages[int((len(ages) + 1) / 2 - 1)])
        median = ages[int((len(ages) + 1) / 2 - 1)]
    else:
        m1 = int(len(ages)/2 - 1)
        m2 = int(len(ages)/2)
        print((ages[m1]+ages[m2])/2)
        median = (ages[m1]+ages[m2])/2
    return average, median


def print_values_above(d: dict, num: int = -1) -> None:
    """
        Function that get a dictionary and a positive number - optional,
        If a number is received - a function will print elements that have an age field greater than the number
        If no - a function will print all the elements of the dictionary
        :param d: dictionary
        :param num: integer number
        :return: None
    """
    if type(d) is not dict:
        print("TypeError: print_values_above's first parameter must be a dictionary")
        return
    bigger_ages = []
    if type(num) != int and type(num) != float:
        print("TypeError: print_values_above's second parameter must be a number type")
        return
    if num < 0:
        print(d.values())
        return
    else:
        for details in d.values():
            if details['age'] > num:
                bigger_ages.append(details)
    print(bigger_ages)


def main():
    data_set = {
        "1": {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"},
        "2": {"name": "Tal", "sex": "male", "age": 22},
        "3": {"name": "Tali", "sex": "female", "age": 42},
        "4": {"name": "Adam", "sex": "male", "age": 18}
    }
    female, male = split_male_female(data_set)
    print(female)
    print(male)
    find_median_average(data_set)
    print_values_above(data_set, 6)


main()
