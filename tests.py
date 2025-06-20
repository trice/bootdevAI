import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_info(self):
        result = get_files_info("calculator", ".")
        print(result)
        
        
    def test_get_files_info_with_valid_subdirectory(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        
    def test_get_files_info_with_invalid_subdirectory(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        
    def test_get_files_info_with_directory_outside_relative_path(self):
        result = get_files_info("calculator", "../")
        print(result)
        
    def test_get_files_info_with_non_directory(self):
        result = get_files_info("calculator", "main.py")
        print(result)
        

if __name__ == "__main__":
    unittest.main()