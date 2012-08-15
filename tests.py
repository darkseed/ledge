import ledge
import unittest
import os
from tempfile import mkdtemp


class LedgeTestCase(unittest.TestCase):

    def setUp(self):
        self.data = {'foo': 'bar', 'flub': ['beep', 'boop']}

    def test_filesystem(self):

        temp_dir = mkdtemp()
        temp_file = os.path.join(temp_dir, 'test.ledge')

        s = ledge.Ledge(backend=ledge.backends.File(temp_file))

        s.update(self.data)
        s.sync()

        s2 = ledge.Ledge(backend=ledge.backends.File(temp_file))
        self.assertEqual(s2, self.data)

    def test_s3(self):
        s = ledge.Ledge(backend=ledge.backends.S3('dabapps-ledgetest', 'foo'))

        s.update(self.data)
        s.sync()

        s2 = ledge.Ledge(backend=ledge.backends.S3('dabapps-ledgetest', 'foo'))
        self.assertEqual(s2, self.data)


if __name__ == "__main__":
    unittest.main()
