import unittest
from main import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1], f"Expected [0, 1], but got {result}")
        
        result = self.solution.twoSum([3, 2, 4], 6)
        self.assertEqual(result, [1, 2], f"Expected [1, 2], but got {result}")

        result = self.solution.twoSum([3, 3], 6)
        self.assertEqual(result, [0, 1], f"Expected [0, 1], but got {result}")

        result = self.solution.twoSum([3, 2, 3], 6)
        self.assertEqual(result, [0, 2], f"Expected [0, 2], but got {result}")

if __name__ == '__main__':
    # Test loader and runner
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    result = unittest.TextTestRunner(failfast=False).run(suite)
    
    # Yalnızca testlerin tamamlanmasını ve hata mesajlarını yazdırıyoruz
    if not result.wasSuccessful():
        print("Some tests failed. Here are the details:")
        for failure in result.failures:
            print(failure)
        for error in result.errors:
            print(error)
