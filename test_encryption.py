import unittest
import encryption


class EncryptionTest(unittest.TestCase):

    def setUp(self):
        self.client = encryption.Encryption()

    def test_encrypt_message(self):
        self.assertEqual('hae and via ecy', self.client.encrypt_message('haveaniceday'))
        self.assertEqual('fto ehg ee dd', self.client.encrypt_message('feedthedog'))
        self.assertEqual('clu hlt io', self.client.encrypt_message('chillout'))

    def test_swap_columns_rows(self):
        grid = [[1, 1, 1], [2, 2, 2], [3, 3]]
        result = self.client.row_column_swap(grid)
        self.assertCountEqual([[1, 2, 3], [1, 2, 3], [1, 2]], result)

    def test_concatenate_strings(self):
        list_of_list_of_strings = [['c', 'a', 't'], ['d', 'o', 'g']]
        result = self.client.list_to_string(list_of_list_of_strings)
        self.assertCountEqual(['cat', 'dog'], result)
