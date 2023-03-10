import unittest
import argparse
import first


class TestWeatherModule(unittest.TestCase):

    def test_1(self):
        w = first.temperature
        self.assertLess(w, 36)

    def test_2(self):
        x = first.humidity
        self.assertGreater(x, 20)


if __name__ == "__main__":
    unittest.main()

    parser = argparse.ArgumentParser(description='Unit tests for weather forecasting app')
    parser.add_argument('--test', action='store_true', help='Test the weather_information function')
    args = parser.parse_args()

    if not args.test_name:
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestWeatherModule)
    else:
        test_suite = unittest.TestSuite()
        test_suite.addTest(TestWeatherModule(args.test_name))
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
