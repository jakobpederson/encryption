import unittest
import encryption


class EncryptionTest(unittest.TestCase):

    def setUp(self):
        self.client = encryption.Encryption()

    def test_x(self):
        self.assertEqual('hae and via ecy', self.client.encrypt_message('haveaniceday'))
        self.assertEqual('fto ehg ee dd', self.client.encrypt_message('feedthedog'))
        self.fail('x')
