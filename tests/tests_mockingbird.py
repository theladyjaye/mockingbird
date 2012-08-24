import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from mockingbird import Mockingbird
from mockingbird.generators import MockRealName
from mockingbird.generators import MockString
from mockingbird.generators import MockPhoneNumber
from mockingbird.generators import MockEmail
from mockingbird.generators import MockDate
from mockingbird.generators import MockInt
from mockingbird.generators import MockBoolean
from mockingbird.generators import MockChoice
from mockingbird.generators import MockObject
from mockingbird.generators import MockObjectList

from .models import Contact
from .models import ContactMeta
from .models import AddressBook
from .models import Message


class MockingbirdCoreSuite(unittest.TestCase):

    def setUp(self):
        self.mockingbird = Mockingbird()

    def test_spec_key(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact, {})
        data = mockingbird["Contact"]()
        self.assertTrue(isinstance(data, Contact))

    def test_spec_attr(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact, {})
        data = mockingbird.Contact()
        self.assertTrue(isinstance(data, Contact))

    def test_realname_string(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact, {"name": MockRealName(),
                                   "label": MockString(min=4, max=10)})

        contact = mockingbird.Contact()

        self.assertTrue(isinstance(contact, Contact))
        self.assertFalse(contact.name == None)
        self.assertFalse(contact.label == None)
        self.assertTrue(len(contact.name) > 1)
        self.assertTrue(len(contact.label) > 1)

    def test_nested(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact,     {"name": MockRealName(),
                                       "label": MockString(min=4, max=10),
                                       "meta": MockObject(ContactMeta)})

        mockingbird.spec(ContactMeta, {"phone": MockPhoneNumber(),
                                       "email": MockEmail(),
                                       "dob": MockDate(),
                                       "age": MockInt(min=22, max=44),
                                       "is_married": MockBoolean()})

        contact = mockingbird.Contact()
        meta = contact.meta

        self.assertFalse(contact == None)
        self.assertTrue(isinstance(contact, Contact))
        self.assertFalse(contact.name == None)
        self.assertFalse(contact.label == None)
        self.assertTrue(len(contact.name) > 1)
        self.assertTrue(len(contact.label) > 1)

        self.assertFalse(meta == None)
        self.assertIsInstance(meta, ContactMeta)
        self.assertFalse(meta.phone == None)
        self.assertFalse(meta.email == None)
        self.assertFalse(meta.dob == None)
        self.assertFalse(meta.age == None)
        self.assertFalse(meta.is_married == None)

        self.assertTrue(len(meta.phone) > 1)
        self.assertTrue(len(meta.email) > 1)
        self.assertTrue(len(meta.dob) > 1)
        self.assertTrue(meta.age >= 22 and meta.age <= 44)
        self.assertTrue(type(meta.is_married) == bool)

    # def test_choice(self):
    #     mockingbird = self.mockingbird

    #     mockingbird.spec(Message,     {"service": MockChoice(['twitter', 'facebook']),
    #                                    "text": MockString(min=4, max=10)})

    def test_list_count(self):
        mockingbird = self.mockingbird

        mockingbird.spec(Contact,     {"name": MockRealName(),
                                       "label": MockString(min=4, max=10),
                                       "meta": MockObject(ContactMeta)})

        mockingbird.spec(ContactMeta, {"phone": MockPhoneNumber(),
                                       "email": MockEmail(),
                                       "dob": MockDate(),
                                       "age": MockInt(min=22, max=44),
                                       "is_married": MockBoolean()})

        mockingbird.spec(AddressBook, {"contacts": MockObjectList(Contact, count=5)})

        address_book = mockingbird.AddressBook()

        self.assertFalse(address_book == None)
        self.assertTrue(isinstance(address_book, AddressBook))
        self.assertEqual(len(address_book.contacts), 5)

        for contact in address_book.contacts:
            meta = contact.meta

            self.assertFalse(contact == None)
            self.assertTrue(isinstance(contact, Contact))
            self.assertFalse(contact.name == None)
            self.assertFalse(contact.label == None)
            self.assertTrue(len(contact.name) > 1)
            self.assertTrue(len(contact.label) > 1)

            self.assertFalse(meta == None)
            self.assertTrue(isinstance(meta, ContactMeta))
            self.assertFalse(meta.phone == None)
            self.assertFalse(meta.email == None)
            self.assertFalse(meta.dob == None)
            self.assertFalse(meta.age == None)
            self.assertFalse(meta.is_married == None)

            self.assertTrue(len(meta.phone) > 1)
            self.assertTrue(len(meta.email) > 1)
            self.assertTrue(len(meta.dob) > 1)
            self.assertTrue(meta.age >= 22 and meta.age <= 44)
            self.assertTrue(type(meta.is_married) == bool)

    def test_list_range(self):
        mockingbird = self.mockingbird

        mockingbird.spec(Contact,     {"name": MockRealName(),
                                       "label": MockString(min=4, max=10),
                                       "meta": MockObject(ContactMeta)})

        mockingbird.spec(ContactMeta, {"phone": MockPhoneNumber(),
                                       "email": MockEmail(),
                                       "dob": MockDate(),
                                       "age": MockInt(min=22, max=44),
                                       "is_married": MockBoolean()})

        mockingbird.spec(AddressBook, {"contacts": MockObjectList(Contact, min=5, max=11)})

        address_book = mockingbird.AddressBook()
        total_contacts = len(address_book.contacts)

        self.assertFalse(address_book == None)
        self.assertTrue(isinstance(address_book, AddressBook))

        self.assertTrue(total_contacts >= 5 and total_contacts <= 10)

        for contact in address_book.contacts:
            meta = contact.meta

            self.assertFalse(contact == None)
            self.assertTrue(isinstance(contact, Contact))
            self.assertFalse(contact.name == None)
            self.assertFalse(contact.label == None)
            self.assertTrue(len(contact.name) > 1)
            self.assertTrue(len(contact.label) > 1)

            self.assertFalse(meta == None)
            self.assertTrue(isinstance(meta, ContactMeta))
            self.assertFalse(meta.phone == None)
            self.assertFalse(meta.email == None)
            self.assertFalse(meta.dob == None)
            self.assertFalse(meta.age == None)
            self.assertFalse(meta.is_married == None)

            self.assertTrue(len(meta.phone) > 1)
            self.assertTrue(len(meta.email) > 1)
            self.assertTrue(len(meta.dob) > 1)
            self.assertTrue(meta.age >= 22 and meta.age <= 44)
            self.assertTrue(type(meta.is_married) == bool)

if __name__ == '__main__':
    unittest.main()
