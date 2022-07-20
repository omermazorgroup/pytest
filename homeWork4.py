class Date:
    def __init__(self, day: int, month: int, year: int):
        if not all(isinstance(i, int) for i in [day, month, year]):
            raise TypeError("one or more of the data is not an integer")
        if day < 1 or day > 31:
            raise ValueError("day must be between 1 to 31!")
        if month < 1 or month > 12:
            raise ValueError("month must be between 1 to 12!")
        if (str(year)[0] != '-' and len(str(year)) != 4) or (str(year)[0] == '-' and len(str(year)) != 5):
            raise ValueError("the length of the number of the year must be four digits!")
        self.day = day
        self.month = month
        self.year = year
        if not self.isValid():
            raise ValueError("the date is not valid!")

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    def __ge__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day >= other.day:
                    return True
        return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def __le__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day <= other.day:
                    return True
        return False

    def __sub__(self, other) -> int:
        current = self
        days = 0
        if self > other:
            while self > other:
                other = other.getNextDay()
                days += 1
        elif self < other:
            while current < other:
                current = self.getNextDay()
                days += 1
        else:
            return 0
        return days

    def isValid(self) -> bool:
        """
        A Function that checks whether a date is valid. A valid date is:
        Date consists of 3 numbers
        In January, March, May, July, August, October and December - day ranges from 1-31
        In April, June, September and November - day ranges from 1-30
        In February - between 1-28 in a non-leap year, 1-29 in a leap year.
        :param self: Date
        :return: boolean, True if the date is valid and false if not
        """
        if self.month in (4, 6, 9, 11):
            if self.day > 30:
                return False
        elif self.month == 2:
            if self.isLeapYear():
                if self.day > 29:
                    return False
            else:
                if self.day > 28:
                    return False
        return True

    def	getNextDay(self):
        """
        Returns the date of tomorrow without changing the current date
        For example, if the date is 28.2.2016 - the next day is 29.2.2016,
        if the date is 28.2.2017 - the day after is 1.3.2017, if the date is 31.12.2000 -
        the day after is 1.1.2001
        :param self: Date
        :return: Date, the date of the next day from self
        """
        nextDay = Date(self.day, self.month, self.year)
        if self.month in (1, 3, 5, 7, 8, 10, 12):
            month_length = 31
        elif self.month == 2:
            if self.isLeapYear():
                month_length = 29
            else:
                month_length = 28
        else:
            month_length = 30
        if self.day < month_length:
            nextDay.day = nextDay.day + 1
        else:
            nextDay.day = 1
            if self.month == 12:
                nextDay.month = 1
                nextDay.year = nextDay.year + 1
            else:
                nextDay.month = nextDay.month + 1
        return nextDay

    def getNextDays(self, daysToAdd: int):
        """
        A function that receives a date and an integer number and returns a
        date after the same number (in days) from the current date
        :param self: Date
        :param daysToAdd: a integer number
        :return: Date, a date "daysToAddd" days later the current date
        """
        nextDays = Date(self.day, self.month, self.year)
        for day in range(0, daysToAdd):
            nextDays = nextDays.getNextDay()
        return nextDays

    def isLeapYear(self) -> bool:
        """
        A function that receives a date and checks whether
        the year of that date is a leap year or not
        :param self: Date
        :return: boolean, True if the year of the current date is a leap year, False if not
        """
        if self.year % 400 == 0 and self.year % 100 == 0:
            return True
        elif (self.year % 4 == 0) and (self.year % 100 != 0):
            return True
        else:
            return False


def main():
    d = Date(28, 2, 2016)
    d3 = d.getNextDays(5)
    d2 = Date(11, 6, 2022)
    print(d, d3)


if __name__ == '__main__':
    main()

