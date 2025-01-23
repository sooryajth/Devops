import unittest
#HELLO KUNJUMANII
#Hey its my first devops hands on project
class TestApp(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    def test_subtraction(self):
        self.assertEqual(3-2,1)
if __name__ == "__main__":
    unittest.main()

