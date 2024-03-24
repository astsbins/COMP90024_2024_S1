import read_functions
import pytest

def test_read_file():
    file = read_functions.read_json("test.json")
    assert file == {"test": "this is a test"}
    
def test_read_chunk0():
    file = "test2.json"
    seek_head = 0
    assert read_functions.read_chunk(file, seek_head).strip() == '{   "tests" :'
    
    
    