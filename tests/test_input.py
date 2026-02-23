import os
import pytest
from app.io.input import read_from_file_builtin, read_from_file_pandas
from app.io.output import output_text_to_console, write_to_file_builtin

def test_read_builtin_isDone():
    test_file = "tests/temp_test.txt"
    text = "function check"
    with open(test_file, "w") as f:
        f.write(text)

    result = read_from_file_builtin(test_file)
    assert text == result 
    os.remove(test_file)

def test_read_builtin_isEmpty():
    test_file = "tests/temp_empty.txt"
    text = ""
    with open(test_file, "w") as f:
        f.write(text)

    result = read_from_file_builtin(test_file)
    assert text == result
    os.remove(test_file)

def test_read_builtin_notFound():
    test_file = "non_exist_file.txt"
    with pytest.raises(FileNotFoundError):
        read_from_file_builtin(test_file)