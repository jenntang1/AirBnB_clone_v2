#!/usr/bin/python3
"""test for db storage"""
import unittest
import pep8
import os
''' from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
'''


class TestDBStorage(unittest.TestCase):
    """this will test the DBStorage"""

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "Found code \
                         style errors (and warnings).")

'''    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Incorrect storage type")
    def setUp(self):
        """connect to test database"""
        self.engine = create_engine('mysql+mysqldb://root: \
                                    hbnb_test@localhost/hbnb_test_db',
                                    pool_pre_ping=True)
        self.session = Session(engine)
        Base.metadata.create_all(self.engine)
        self.session.add(self.user)
        self.session.commit()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Incorrect storage type")
    def tearDown(self):
        Base.metadata.drop_all(self.engine)
'''

if __name__ == "__main__":
    unittest.main()
