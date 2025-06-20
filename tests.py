import unittest
from functions.get_file_content import get_file_content

class TestGetFilesContent(unittest.TestCase):
    def test_get_file_content(self):
        content = get_file_content("calculator", "main.py")
        print(content)
        
    def test_get_file_content_with_invalid_path(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        
    def test_get_file_content_with_invalid_file(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)


if __name__ == "__main__":
    unittest.main()