# Make Python Library

[Link](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f)

### Executing Tests

```bash
python setup.py pytest
```

### Build

```bash
python setup.py bdist_wheel
```

### Install

```bash
pip install /Users/mina/Desktop/Mina/Edu/Learning/MyLibrary/dist/mylib-0.1.0-py3-none-any.whl
```

### Install in IPython Notebook

```bash
import sys

!{sys.executable} -m pip install /Users/mina/Desktop/Mina/Edu/Learning/MyLibrary/dist/mylib-0.1.0-py3-none-any.whl
```

### How to test print function

```python
import unittest.mock
import io

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
def test_normal(self, mock_stdout):
    print('Chicken dinner!')
    self.assertEqual(mock_stdout.getvalue(), 'Chicken dinner!')
```