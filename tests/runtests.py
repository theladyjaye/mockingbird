from __future__ import absolute_import
import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest

TEST_MODULES = [
    'tests.tests_exceptions',
    'tests.tests_generators',
    'tests.tests_mockingbird'
]


def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == '__main__':
    unittest.main(defaultTest='all')
