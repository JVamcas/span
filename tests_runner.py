import unittest
from unittest import runner


if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(start_dir="tests",pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    runner = unittest.TextTestRunner()
    runner.run(suite)