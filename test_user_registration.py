import pytest

from user_registration import UserRegistration

u_reg = UserRegistration()


def test_first_name():
    """
    :return: true for valid first name otherwise false
    """
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False
