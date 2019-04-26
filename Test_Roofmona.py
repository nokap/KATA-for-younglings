import unittest
import methodRoofmona
matrix = [[4,8,2,9,34,57,22,44], [0,2,8,9,1,2,55,3,22,4]]
matrix2 = [[4,8,2,9,34,82,22,44], [0,2,8,9,1,2,54,3,22,4]]
matrix3 = [[4,8,2,9,34,84,22,44], [0,2,8,9,1,2,55,3,22,4]]

class TestAdd(unittest.TestCase):
    def test_boompo(self):
        self.assertEqual(methodRoofmona.largestlowest(matrix), (57,0), "output should be output 57,0")

    def test_boompo2(self):
        self.assertEqual(methodRoofmona.largestlowest(matrix2), (82,0), "output should be output 82,0")

    def test_boompo3(self):
        self.assertEqual(methodRoofmona.largestlowest(matrix3), (84,0), "output should be output 84,0")



if __name__ == '__main__':
    unittest.main()
