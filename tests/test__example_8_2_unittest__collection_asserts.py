"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
--------------------------------------------------------------------------
python -m unittest tests.test__example_8_2_unittest__collection_asserts -v
--------------------------------------------------------------------------
or discover and execute all the tests with the command:
-------------------------------
python -m unittest discover -v
-------------------------------
"""
import unittest


class TestCaseCollectionAsserts(unittest.TestCase):
    def setUp(self):
        self.list1 = ["Python", "Selenium"]
        self.list2 = ["Selenium", "Python"]
        self.tuple1 = ("Python", "Selenium")
        self.tuple2 = ("Selenium", "Python")
        self.set1 = {"Python", "Selenium"}
        self.set2 = {"Selenium", "Python"}
        self.dict1 = {"key1": "value1", "key2": "value2"}
        self.dict2 = {"key2": "value2", "key1": "value1"}

    def test15(self):
        self.assertListEqual(self.list1, self.list2, "some text if the test fails")

    def test16(self):
        self.assertTupleEqual(self.tuple1, self.tuple2, "some text if the test fails")

    def test17(self):
        self.assertSetEqual(self.set1, self.set2, "some text if the test fails")

    def test18(self):
        self.assertDictEqual(self.dict1, self.dict2, "some text if the test fails")

    def test19(self):
        self.assertIn("Selenium", "Selenium Python", "some text if the test fails")

    def test20(self):
        self.assertNotIn("Selenium", "Selenium Python", "some text if the test fails")

# test15 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts) ... FAIL
# test16 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts) ... FAIL
# test17 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts) ... ok
# test18 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts) ... ok
# test19 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts) ... ok
# test20 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts) ... FAIL
#
# ======================================================================
# FAIL: test15 (tests.test__example_8_2_unittest__collection_asserts.TestCaseCollectionAsserts)
# ...
