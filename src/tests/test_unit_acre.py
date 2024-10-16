import unittest
from oxrse_unit_conv.units import km2, acre, m2

class TestAcre(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(acre.si_unit.matches(m2))

    def test_basic_conversion(self):
        self.assertEqual(acre.to_si(1), 4_046.86)
        self.assertEqual(acre.to_unit(10, acre), 10)
        self.assertAlmostEqual(m2.to_unit(5000, acre), 1.235527,5)

    def test_km_conversion(self):
        self.assertAlmostEqual(acre.to_unit(1000, km2), 4.04686, 5)


if __name__ == '__main__':
    unittest.main()