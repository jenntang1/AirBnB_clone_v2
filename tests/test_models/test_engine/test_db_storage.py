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

if __name__ == "__main__":
    unittest.main()
