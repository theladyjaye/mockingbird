import unittest
import context
from mockingbird import mockingbird
from mockingbird.generators import MockRealName
from mockingbird.generators import MockString
from mockingbird.generators import MockPhone
from mockingbird.generators import MockEmail
from mockingbird.generators import MockDate
from mockingbird.generators import MockInt
#from mockingbird.generators import MockBoolean
#from mockingbird.generators import MockChoice
#from mockingbird.generators import MockObject
#from mockingbird.generators import MockList

from models import Contact
from models import ContactMeta
from models import AddressBook

class MockingbirdSuite(unittest.TestCase):

    def test_realname(self):
        data = MockRealName()
        result = data()
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 1)

    def test_string(self):
        data = MockString(min=4, max=10)
        result = data()
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 1)

    def test_phone(self):
        data = MockPhone()
        result = data()
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 1)

    def test_email(self):
        data = MockEmail()
        result = data()
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 1)

    def test_date(self):
        data = MockDate()
        result = data()
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 1)

    def test_int(self):
        data = MockInt(min=20, max=30)
        
        for i in range(50):
            result = data()
            self.assertIsNotNone(result)
            self.assertTrue(result > 19)

    def test_realname_string(self):
        mockingbird.spec(Contact, {"name": MockRealName(),
                                   "label": MockString(min=4, max=10)})

        contact = mockingbird.Contact()

        self.assertIsInstance(contact, Contact)
        self.assertIsNotNone(contact.name)
        self.assertIsNotNone(contact.label)
        self.assertGreater(len(contact.name), 1)
        self.assertGreater(len(contact.label), 1)

    # def test_simple(self):
    #     mockingbird.spec(ContactMeta, {"phone": MockRealName(),
    #                                "label": MockString(min=4, max=10)})        




    #     class ContactMeta(object):
    # def __init__(self):
    #     self.phone = None
    #     self.email = None
    #     self.dob = None,
    #     self.age = 0
    #     self.is_married = False