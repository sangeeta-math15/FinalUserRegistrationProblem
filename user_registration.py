import re

from user_registrationException import InputError

"""
    re specifies a set of strings that matches it; the functions in this module let you check 
    if a particular string matches a given regular expression
"""

FIRST_NAME = "^[A-Z]{1}[a-z]{2,}$"


class UserRegistration:
    """
    create class for validating user registration
    """

    def __init__(self):
        pass

    def first_name_validation(self, fname_input):
        """
        :return:
        :param fname_input: user input
        :return: true for valid username
        """

        if re.match(FIRST_NAME, fname_input):
            return True


if __name__ == '__main__':

    user_reg = UserRegistration()

    fname_input = input("Enter First Name:")
    matched_input = user_reg.first_name_validation(fname_input)

    try:
        if not matched_input:
            raise InputError(" Enter the first name with minimum three characters ")

    except InputError as e:
        print(str(e))

