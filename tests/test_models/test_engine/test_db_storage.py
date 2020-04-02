#!/usr/bin/python3
"""test for db storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestDBStorage(unittest.TestCase):
    """this will test the DBStorage"""

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
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


if __name__ == "__main__":
    unittest.main()
