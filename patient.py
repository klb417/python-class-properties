import re


class Patient:
    def __init__(
        self,
        social_security_number,
        date_of_birth,
        account_number,
        first_name,
        last_name,
        address,
    ):
        self.__social_security_number = social_security_number
        self.__date_of_birth = date_of_birth
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    # Social security number
    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return "xxx-xx-xxxx"

    # Date of birth
    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return "xx/xx/xxxx"

    # Health insurance account number
    @property
    def account_number(self):
        try:
            return self.__account_number
        except AttributeError:
            return "xxxxxxxxxx"

    # First name
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "asdf"

    # Last name
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "asdf"

    # Full Name
    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return ""

    # Address
    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Address must be a string")


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103", "Daniela", "Agnoletti", "500 Infinity Way",
)

# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)  # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)  # "Daniela Agnoletti"


print(cashew.address)

cashew.address = "321 New Address St"

print(cashew.address)
