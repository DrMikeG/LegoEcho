import unittest
from datetime import date

def calculate_age_at_wedding(person):
    """Calculate the age of a person at his or her wedding, given the
    record of the person as a dictionary-like object.
    """
    # Pull out the birthday and anniversary datetime.date objects.
    anniversary = person['anniversary']
    birthday = person['birthday']

    # Calculate the age of the person on his or her wedding day.
    age = anniversary.year - birthday.year

    # If the birthday occurs later in the year than the anniversary, then
    # subtract one from the age.
    if birthday.replace(year=anniversary.year) > anniversary:
        age -= 1

    # Done; return the age.
    return age

class Tests(unittest.TestCase):
    def test_calculate_age_at_wedding(self):
        """Establish that the 'calculate_age_at_wedding' function seems
        to calculate a person's age at his wedding correctly, given
        a dictionary-like object representing a person.
        """
        # Assert that if the anniversary falls before the birthday
        # in a calendar year, that the calculation is done properly.
        person = {'anniversary': date(2012, 4, 21),
                  'birthday': date(1986, 6, 15)}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 25)

        # Assert that if the anniversary falls after the birthday
        # in a calendar year, that the calculation is done properly.
        person = {'anniversary': date(1969, 8, 11),
                  'birthday': date(1945, 2, 15)}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 24)

    def test_failure_case(self):
        """Assert a wrong age, and fail."""
        person = {'anniversary': date(2012, 4, 21),
                'birthday': date(1986, 6, 15)}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age, 99)