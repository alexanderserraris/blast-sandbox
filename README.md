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

### Jupyter tests
- Write the test in `jupyter-test.py`
- Place the Jupyter Notebook to be tested in the `src` folder
- Run the test with `python jupyter-test.py`  


## Notes
- In `testUtils.py` there are some useful helper-functions for testing.
- Don't know how to write a test? The Python unittest documentation is the place to be.
