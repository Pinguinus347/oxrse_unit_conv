import unittest
from oxrse_unit_conv.units import km2, m2


class TestKilometer(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(km2.si_unit.matches(m2))

    def test_basic_conversion(self):
        self.assertEqual(km2.to_si(1), 1_000_000)
        self.assertEqual(km2.to_unit(10, km2), 10)


if __name__ == '__main__':
    unittest.main()
