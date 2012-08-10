import unittest
import context
from mockingbird import Mockingbird
from mockingbird.generators import MockRealName
from mockingbird.generators import MockString
from mockingbird.generators import MockPhone
from mockingbird.generators import MockEmail
from mockingbird.generators import MockDate
from mockingbird.generators import MockInt
from mockingbird.generators import MockBoolean
from mockingbird.generators import MockChoice
from mockingbird.generators import MockObject
#from mockingbird.generators import MockObjectList
from mockingbird.exceptions import MissingSpec

from models import Contact
from models import ContactMeta
from models import AddressBook

class MockingbirdSuite(unittest.TestCase):

    def test_missing_spec_attr(self):
        mockingbird = Mockingbird()

        with self.assertRaises(MissingSpec):
            mockingbird.Phantom()

        with self.assertRaises(AttributeError):
            mockingbird.Phantom()

    def test_missing_spec_key(self):
        mockingbird = Mockingbird()

        with self.assertRaises(MissingSpec):
            mockingbird["Phantom"]

        with self.assertRaises(KeyError):
            mockingbird["Phantom"]

    def test_spec_key(self):
        mockingbird = Mockingbird()
        mockingbird.spec(Contact, {})
        data = mockingbird["Contact"]()
        self.assertIsInstance(data, Contact)

    def test_spec_attr(self):
        mockingbird = Mockingbird()
        mockingbird.spec(Contact, {})
        data = mockingbird.Contact()
        self.assertIsInstance(data, Contact)

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
        
        for i in range(20):
            result = data()
            self.assertIsNotNone(result)
            self.assertTrue(result > 19)

    def test_boolean(self):
        data = MockBoolean()
        
        for i in range(20):
            result = data()
            self.assertIsInstance(result, bool)

    def test_boolean_true(self):
        data = MockBoolean(value=True)
        
        for i in range(20):
            result = data()
            self.assertIsInstance(result, bool)
            self.assertTrue(result)

    def test_boolean_false(self):
        data = MockBoolean(value=False)
        
        for i in range(20):
            result = data()
            self.assertIsInstance(result, bool)
            self.assertFalse(result)

    def test_choice(self):
        choices = ["lucy", "ollie", "clark"]
        data = MockChoice(choices)
        
        for i in range(20):
            result = data()
            self.assertIn(result, choices)

    def test_choice_boolean(self):
        choices = [True, False]
        data = MockChoice(choices)
        
        for i in range(20):
            result = data()
            self.assertIn(result, choices)

    def test_choice_single(self):
        choices = ["lucy"]
        data = MockChoice(choices)
        
        for i in range(20):
            result = data()
            self.assertEqual(result, "lucy")

    def test_object(self):
        mockingbird = Mockingbird()
        mockingbird.spec(Contact, {"name": MockRealName(),
                                   "label": MockString(min=4, max=10)})
        data = MockObject(Contact)
        result = data()

        self.assertIsInstance(result, Contact)
        self.assertIsNotNone(result.name)
        self.assertIsNotNone(result.label)
        self.assertTrue(len(result.name) > 1)
        self.assertTrue(len(result.label) > 1)

    def test_list(self):
        pass
            

    def test_realname_string(self):
        mockingbird = Mockingbird()
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