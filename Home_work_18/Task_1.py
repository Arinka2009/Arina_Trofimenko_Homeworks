# Task 1st
import re


class Email:
    def __init__(self, email: str):
        Email.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        # used validation criteria from  https://help.xmatters.com/ondemand/trial/valid_email_format.htm
        validator = r"^[a-zA-Z0-9]+[_.-]?[a-zA-Z0-9]+[@][a-zA-Z0-9\-]+[.][a-zA-Z]{2,}$"

        if not re.match(validator, email):
            raise ValueError(f'{email} is NOT valid')
        print(f'{email} is valid')
        return email
    

# check the code
Email('abc-d@mail.com')  # --> valid email
Email('abc-@mail.com')  # --> Invalid. Rise Error
Email('abc.def@mail..com')  # --> Invalid. Rise Error
Email('abc.def@mail.cc')  # --> valid email
