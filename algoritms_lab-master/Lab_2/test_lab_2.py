from lab_2 import Calendar
import unittest


class Test(unittest.TestCase):
    def test_from_example(self):
        array = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        test = Calendar(array)
        test.array = test.quick_sort(test.array)
        test.changing_calendar()
        self.assertEqual(test.result, [(0, 1), (3, 8), (9, 12)])

    def test_with_empty_array(self):
        test = Calendar([])
        test.array = test.quick_sort(test.array)
        test.changing_calendar()
        self.assertEqual(test.result, [])

    def test_with_one_cortage(self):
        test = Calendar([(1, 4)])
        test.array = test.quick_sort(test.array)
        test.changing_calendar()
        self.assertEqual(test.result, [(1, 4)])

    def test_with_other_data(self):
        test = Calendar([(1, 9), (3, 8), (5, 6)])
        test.array = test.quick_sort(test.array)
        test.changing_calendar()
        self.assertEqual(test.result, [(1, 9)])

    def test3(self):
        test = Calendar([(0,1), (0,6), (2,5), (3,1), (10,12), (12, 4)])
        test.array=test.quick_sort(test.array)
        test.changing_calendar()
        self.assertEqual(test.result, [(0, 6), (10, 12)])


if __name__ == '__main__':
    unittest.main
