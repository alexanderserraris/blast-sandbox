import unittest
import testUtils
import sys

@testUtils.lint_jupyter_notebook(f"OK.ipynb") # looks in `src` folder for this file
class TestStudentCode(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
