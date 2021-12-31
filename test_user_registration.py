import pytest

from user_registration import UserRegistration

u_reg = UserRegistration()


def test_first_name():
    """
    :return: true for valid first name otherwise false
    """
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False


def test_last_name():
    """
    :return: true for valid last name otherwise false
    """
    assert u_reg.last_name_validation("Math") == True or u_reg.last_name_validation("math") == False


def test_email():
    """
    :return: true for email validation otherwise false
    """
    assert u_reg.email_validation("sangeeta.1rn18mca30@gmail.com") == True or u_reg.email_validation("sangeeta.gmail.com") == False



