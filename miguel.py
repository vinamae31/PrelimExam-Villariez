import unittest

def name():
    name = 'VILLARIEZ'
    return name

class Check(unittest.TestCase):

    def test(self):
        self.assertEqual(name(), 'MIGUEL')

if __name__=='__main__':
    unittest.main()