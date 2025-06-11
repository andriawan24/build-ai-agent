# import unittest
from functions.run_python import run_python

# class TestFunction(unittest.TestCase):
#     def test_print_root_folder(self):
#         result = get_files_info("calculator", ".")
#         self.assertTrue("main.py" in result)
#         self.assertTrue("tests.py" in result)
#         self.assertTrue("pkg" in result)
#         self.assertTrue("render.py" not in result)

#     def test_print_subfolder(self):
#         result = get_files_info("calculator", "pkg")
#         self.assertTrue("main.py" not in result)
#         self.assertTrue("calculator.py" in result)
#         self.assertTrue("render.py" in result)

#     def test_print_invalid_folder(self):
#         with self.assertRaises(Exception) as context:
#             get_files_info("calculator", "/bin")

#         self.assertTrue('outside the permitted working directory' in str(context.exception))

#     def test_print_another_invalid_folder(self):
#         with self.assertRaises(Exception) as context:
#             get_files_info("calculator", "../")

#         self.assertTrue('outside the permitted working directory' in str(context.exception))

if __name__ == "__main__":
    print(run_python("calculator", "main.py"))
    print(run_python("calculator", "tests.py"))
    print(run_python("calculator", "../main.py"))
    print(run_python("calculator", "nonexistent.py"))
    # unittest.main()