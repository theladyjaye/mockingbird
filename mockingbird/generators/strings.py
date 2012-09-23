from .base import MockingbirdGenerator
from mockingbird.repositories.strings.text import TextGenerator
from mockingbird.repositories.strings.names import NameGenerator
from mockingbird.repositories.strings.names import FirstNameGenerator
from mockingbird.repositories.strings.names import LastNameGenerator
from mockingbird.repositories.strings.names import UserNameGenerator
from mockingbird.repositories.strings.email import EmailGenerator
from mockingbird.repositories.strings.phone import PhoneNumberGenerator
from mockingbird.repositories.strings.dates import DateGenerator


class MockString(MockingbirdGenerator):
    def __init__(self, min=1, max=1, count=None, value=None, repo=TextGenerator):
        self.repo = repo(min=min, max=max, count=count, value=value)


class MockUserName(MockingbirdGenerator):
    def __init__(self, repo=UserNameGenerator):
        self.repo = repo()


class MockRealName(MockingbirdGenerator):
    def __init__(self, repo=NameGenerator):
        self.repo = repo()


class MockFirstName(MockingbirdGenerator):
    def __init__(self, repo=FirstNameGenerator):
        self.repo = repo()


class MockLastName(MockingbirdGenerator):
    def __init__(self, repo=LastNameGenerator):
        self.repo = repo()


class MockEmail(MockingbirdGenerator):
    def __init__(self, repo=EmailGenerator):
        self.repo = repo()


class MockPhoneNumber(MockingbirdGenerator):
    def __init__(self, repo=PhoneNumberGenerator):
        self.repo = repo()


class MockDate(MockingbirdGenerator):
    def __init__(self,
                 min_month=1,
                 max_month=12,
                 min_year=2000,
                 max_year=None,
                 format="%m/%d/%Y",
                 repo=DateGenerator):

        self.repo = repo(min_month=min_month,
                         max_month=max_month,
                         min_year=min_year,
                         format=format)
