def is_leap_year(year: int) -> bool:
    """
       Determine if a given year is a leap year.

       A year is a leap year if it is:
       - Divisible by 400, OR
       - Divisible by 4 but not by 100

       Args:
           year: The year to check (must be a positive integer)

       Returns:
           bool: True if the year is a leap year, False otherwise
           """

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


print(is_leap_year(2020))


