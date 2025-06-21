import unittest

from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_write_file(self):
        file_content = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(file_content)
        
    def test_write_file_to_subdirectory(self):
        file_content = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(file_content)
        
    def test_write_file_to_outside_directory(self):
        file_content = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(file_content)


if __name__ == "__main__":
    unittest.main()