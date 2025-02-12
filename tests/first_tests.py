import json
from time import sleep

import pytest
from pathlib import Path
from file_management import *


def test_build_path_object():
    """Test that build_path_object() correctly renames a file"""
    source_file = Path("json_file.json")
    expected_new_file = Path("json_file_normalized.json")
    assert build_path_object(source_file) == expected_new_file


def test_normalize_file():
    """
    Test to ensure that normalize file:
        * Returns the expected path object
        * That a file with the expected path name exists
        * That each line in the new file is in valid json format
        * That the new file contains the expected number of lines

    The test concludes by deleting the file created for test, then
    tests to ensure that the file has been deleted.
    """
    source_file = "json_list_test_file.json"
    expected_new_file = Path("json_list_test_file_normalized.json")
    expected_new_file_line_count = 10

    # Ensure normalize_file returns the expected path object
    assert normalize_file(source_file) == expected_new_file
    # Ensure that a file has been created using that Path name
    assert expected_new_file.exists()

    # Open new file and count lines
    with open(expected_new_file, "r") as file:
        new_file_line_count_actual = sum(1 for _ in file)
        for line in file:
            try:
                # Ensures that each line is a valid json object
                assert isinstance(json.loads(line), dict)
            except json.JSONEncoder:
                assert False, "Line is not valid json"
    # Ensure that the new file contains the expected number of lines
    assert new_file_line_count_actual == expected_new_file_line_count

    expected_new_file.unlink()  # Delete the file
    assert not expected_new_file.exists()  # Ensure file has been deleted


# def test_read_and_write_file()
#     """Test to ensure file is being read properly"""
#     source_file = Path("json_list_test_file.json")

