# Python en Jupyter Notebook BLAST tests

Execute BLAST tests locally for education development. Currently supporting 
python and Jupyter Notebook (Python) tests with unittest.

## Requirements
> Python 3.10+

## Installation
```shell
git clone https://github.com/alexanderserraris/python-jupyter-test
cd blast-jupyter-linter
```

## Usage
### Python tests
- Write the test in `python-test.py`
- Place the python file to be tested in the `src` folder
- Run the test with `python python-test.py`

#### Example test
```python
import unittest
import testUtils

class TestStudentCode(unittest.TestCase):

    # @message: Tests of de output hello world is
    def test_OutputIsHelloWorld(self):
        output = testUtils.run_student_file("hello_world.py") # Looks in `src` folder for this file
        self.assertRegex(output, "hello world!")


if __name__ == '__main__':
    unittest.main()
```

### Jupyter tests
_Currently: **only linting is supported** for Jupyter Notebooks_
- Write the test in `jupyter-test.py`
- Place the Jupyter Notebook to be tested in the `src` folder
- Run the test with `python jupyter-test.py`  

#### Example test
```python
import unittest
import testUtils 

@testUtils.lint_jupyter_notebook(f"notebook.ipynb") # looks in `src` folder for this file
class TestStudentCode(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

```


## Notes
- In `testUtils.py` there are some useful helper-functions for testing.
- Don't know how to write a test? The Python unittest documentation is the place to be.
