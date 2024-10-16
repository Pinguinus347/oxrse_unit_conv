import unittest
from oxrse_unit_conv.units import nM, M


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(nM.si_unit.matches(M))

    def test_basic_conversion(self):
        self.assertEqual(nM.to_si(1), 1e-9)


if __name__ == '__main__':
    unittest.main()
