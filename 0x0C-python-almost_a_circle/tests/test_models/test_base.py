#!/usr/bin/python3
"""
unittest for base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)
