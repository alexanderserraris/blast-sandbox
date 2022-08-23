import unittest
import testUtils
import sys

file = sys.argv[1]

@testUtils.lint_jupyter_notebook(f"{file}.ipynb")
class TestStudentCode(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
