import unittest
from file_handler import File_handler
from unittest import mock
# from server import FILES

PATH = "/Users/fransgabro/slutuppgift2/devops20_python_slutuppgift/slutuppgift"
LS = ['.tox', '__init__.py', '__pycache__', 'client.py', 'coverage.xml', 'file_handler.py',
      'random1.txt', 'random2.txt', 'requirements.txt', 'server.py', 'test_file_handler.py']
# komplettering
LS2 = ['.tox', '__init__.py', '__pycache__', 'client.py', 'coverage.xml', 'file_handler.py',
       'random1.txt', 'random2.txt', 'requirements.txt', 'server.py', 'test_file_handler.py', 'tox.ini']
RM1 = 'random1.txt'
RM2 = 'random2.txt'


class test_file_handler(unittest.TestCase):

    def fake_file(self):
        return LS

    def setUp(self):
        self.fh = File_handler(PATH)
        self.fh.cp(RM1, RM2)
        self.patcher = mock.patch('file_handler.File_handler.ls', side_effect=self.fake_file)  # komplettering
        self.patcher.start()

    def test_file_handler(self):
        self.assertIsInstance(self.fh, File_handler)

    def test_ls(self):
        self.assertTrue(list, self.fh.ls())
        self.assertEqual(LS, self.fh.ls())

    def test_size(self):
        self.assertEqual(self.fh.size(RM1), 3)

    def test_rm(self):
        self.assertEqual(self.fh.rm(RM2), "File removed")
        self.assertNotEqual(self.fh.ls(), LS2)

    def tearDown(self):
        self.patcher.stop()


if __name__ == "__main__":
    unittest.main()
