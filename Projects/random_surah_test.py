import random_surah
import unittest
from unittest.mock import patch

class random_surah_test(unittest.TestCase):
    @patch('builtins.input', return_value='1-30')
    def test_juz_range(self, mock_input):
        result = random_surah.user()
        self.assertEqual(result[0:12], "Read surahs ")