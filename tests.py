import ledge
import unittest
import os
from tempfile import mkdtemp


class LedgeTestCase(unittest.TestCase):

    def setUp(self):
        self.data = {'foo': 'bar', 'flub': ['beep', 'boop']}
        self.temp_dir = mkdtemp()

    def get_temp_file(self, filename):
        return os.path.join(self.temp_dir, filename)

    def test_readonly(self):
        temp_file = self.get_temp_file('test_readonly.ledge')
        l = ledge.Ledge(backend=ledge.backends.File(temp_file))
        self.assertRaises(ledge.exceptions.ReadOnlyError, l.sync)

    def test_filesystem(self):
        temp_file = self.get_temp_file('test_filesystem.ledge')

        s = ledge.Ledge(backend=ledge.backends.File(temp_file), readonly=False)

        s.update(self.data)
        s.sync()

        s2 = ledge.Ledge(backend=ledge.backends.File(temp_file))
        self.assertEqual(s2, self.data)

    def teasdfst_s3(self):
        s = ledge.Ledge(backend=ledge.backends.S3('dabapps-ledgetest', 'foo'), readonly=False)

        s.update(self.data)
        s.sync()

        s2 = ledge.Ledge(backend=ledge.backends.S3('dabapps-ledgetest', 'foo'))
        self.assertEqual(s2, self.data)


if __name__ == "__main__":
    unittest.main()
