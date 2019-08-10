import unittest
from database.database_utils import DatabaseUtils


class TestBibleitResults(unittest.TestCase):

    def setUp(self):
        self.utils = DatabaseUtils()

    def test_results_from_db(self):
        word = "cat"
        result = self.utils.query_db(word)
        count = result.count(word)
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
