import unittest
from unittest.mock import patch

from rustimport_jupyter import load_ipython_extension


class TestLoadIPythonExtension(unittest.TestCase):
    @patch("rustimport_jupyter.which")
    def test_import_error(self, which_mock):
        which_mock.return_value = None

        with self.assertRaises(OSError):
            load_ipython_extension(None)
