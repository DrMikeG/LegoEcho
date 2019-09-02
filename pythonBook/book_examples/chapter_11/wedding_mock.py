import unittest
from datetime import date

def calculate_age_at_wedding(person_id):
    """Calculate the age of a person at his or her wedding, given the
    ID of the person in the database.
    """
    # Get the person from the database, and pull out the birthday
    # and anniversary datetime.date objects.
    person = get_person_from_db(person_id)
    anniversary = person['anniversary']
    birthday = person['birthday']

    age = anniversary.year - birthday.year

    # If the birthday occurs later in the year than the anniversary, then
    # subtract one from the age.
    if birthday.replace(year=anniversary.year) > anniversary:
        age -= 1

    # Done; return the age.
    return age

def get_person_from_db(person_id):
    raise RuntimeError('The real 'get_person_from_db' function was called.')

# Import mock regardless of whether it is from the standard library
# or from the PyPI package.
try:
    from unittest import mock
except ImportError:
    import mock

class Tests(unittest.TestCase):
    def test_calculate_age_at_wedding(self):
        """Establish that the 'calculate_age_at_wedding' function seems
        to calculate a person's age at his wedding correctly, given
        a person ID.
        """
        # Since we are mocking a name in the current module, rather than
        # an imported module (the common case), we need a reference to
        # this module to send to 'mock.patch.object'.
        module = sys.modules[_name_]

        with mock.patch.object(module, 'get_person_from_db') as m:
            # Ensure that the get_person_from_db function returns
            # a valid dictionary.
            m.return_value = {'anniversary': date(2012, 4, 21),
                              'birthday': date(1986, 6, 15)}

            # Assert that that the calculation is done properly.
            age = calculate_age_at_wedding(person_id=42)
            self.assertEqual(age, 25)