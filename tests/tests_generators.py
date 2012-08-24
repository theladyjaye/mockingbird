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


class GeneratorsSuite(unittest.TestCase):

    def setUp(self):
        self.mockingbird = Mockingbird()

    def test_realname(self):
        data = MockRealName()
        result = data(self.mockingbird)
        self.assertFalse(result == None)
        self.assertGreater(len(result), 1)

    def test_string(self):
        data = MockString(min=4, max=10)
        result = data(self.mockingbird)
        self.assertFalse(result == None)
        self.assertTrue(len(result) > 1)

    def test_string_count(self):
        data = MockString(count=10)
        for i in range(20):
            result = data(self.mockingbird).split()
            self.assertFalse(result == None)
            self.assertTrue(len(result) == 10)

    def test_string_value(self):
        data = MockString(value="lucy")
        for i in range(20):
            result = data(self.mockingbird)
            self.assertFalse(result == None)
            self.assertEqual(result, 'lucy')

    def test_phone(self):
        data = MockPhoneNumber()
        result = data(self.mockingbird)
        self.assertFalse(result == None)
        self.assertGreater(len(result), 1)

    def test_email(self):
        data = MockEmail()
        result = data(self.mockingbird)
        self.assertFalse(result == None)
        self.assertTrue(len(result) > 1)

    def test_date(self):
        data = MockDate()
        result = data(self.mockingbird)
        self.assertFalse(result == None)
        self.assertTrue(len(result) > 1)

    def test_int(self):
        data = MockInt(min=20, max=30)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertFalse(result == None)
            self.assertTrue(result > 19)

    def test_int_value(self):
        data = MockInt(value=5)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertFalse(result == None)
            self.assertTrue(result == 5)

    def test_boolean(self):
        data = MockBoolean()

        for i in range(20):
            result = data(self.mockingbird)
            self.assertTrue(isinstance(result, bool))

    def test_boolean_true(self):
        data = MockBoolean(value=True)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertTrue(isinstance(result, bool))
            self.assertTrue(result)

    def test_boolean_false(self):
        data = MockBoolean(value=False)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertTrue(isinstance(result, bool))
            self.assertFalse(result)

    def test_choice(self):
        choices = ["lucy", "ollie", "clark"]
        data = MockChoice(choices)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertTrue(result in choices)

    def test_choice_boolean(self):
        choices = [True, False]
        data = MockChoice(choices)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertTrue(result in choices)

    def test_choice_single(self):
        choices = ["lucy"]
        data = MockChoice(choices)

        for i in range(20):
            result = data(self.mockingbird)
            self.assertEqual(result, "lucy")

    def test_object(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact, {"name": MockRealName(),
                                   "label": MockString(min=4, max=10)})
        data = MockObject(Contact)
        result = data(mockingbird)

        self.assertTrue(isinstance(result, Contact))
        self.assertFalse(result.name == None)
        self.assertFalse(result.label == None)
        self.assertTrue(len(result.name) > 1)
        self.assertTrue(len(result.label) > 1)

    def test_object_list_count(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact, {"name": MockRealName(),
                                   "label": MockString(min=4, max=10)})

        data = MockObjectList(Contact, count=2)
        result = data(mockingbird)

        self.assertEqual(len(result), 2)

        for item in result:
            self.assertTrue(isinstance(item, Contact))
            self.assertFalse(item.name == None)
            self.assertFalse(item.label == None)
            self.assertTrue(len(item.name) > 1)
            self.assertTrue(len(item.label) > 1)

    def test_object_list_range(self):
        mockingbird = self.mockingbird
        mockingbird.spec(Contact, {"name": MockRealName(),
                                   "label": MockString(min=4, max=10)})

        data = MockObjectList(Contact, min=2, max=11)
        result = data(mockingbird)
        total = len(result)
        self.assertTrue(total >= 2 and total <= 10)

        for item in result:
            self.assertTrue(isinstance(item, Contact))
            self.assertFalse(item.name == None)
            self.assertFalse(item.label == None)
            self.assertTrue(len(item.name) > 1)
            self.assertTrue(len(item.label) > 1)

if __name__ == '__main__':
    unittest.main()
