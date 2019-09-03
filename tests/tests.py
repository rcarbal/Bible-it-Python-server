import os
import unittest
import json

from database.databse_connection import DatabaseConnect
from database.db_classes_niv import Verse


class TestBibleitResults(unittest.TestCase):

    def test_results_from_db(self):
        # db_path = os.path.join(os.path.dirname(__file__), '..\\database\\bibledatabase.db')
        # print(db_path)
        # database = DatabaseConnect(database='sqlite:///{}?check_same_thread=False'.format(db_path))
        # verses = database.session.query(Verse).all()

        data = None
        with open('../bible-json/NIV.json') as json_file:
            data = json.load(json_file)

        bible_string = json.dumps(data)

        self.assertTrue("god" in bible_string)




if __name__ == '__main__':
    unittest.main()
