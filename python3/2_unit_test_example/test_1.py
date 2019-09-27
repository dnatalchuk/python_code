#!/usr/bin/env python3

import unittest
import add_module


class TestAdd(unittest.TestCase):

    def test_add(self):
        result = add_module.add(10, 5)
        self.assertEqual(result, 15)

if __name__ == "__main__":
    unittest.main()
