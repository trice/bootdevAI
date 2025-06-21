import unittest

from functions.run_python import run_python_file


class TestRunFile(unittest.TestCase):
    def test_with_main(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_with_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_with_outside_allowed_directory(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_with_nonexistent_script(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)

if __name__ == "__main__":
    unittest.main()
