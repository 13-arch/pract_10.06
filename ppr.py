
import unittest


#тестируемая часть приложения

def round_square(r):        #Функция для поиска площади
    if isinstance(r,str) is True:
        square="TypeError"
    elif r<0:
        square="ValueError: radius cant be negative"
    else:
        square=r*r*3.14
    return square

    
def circle(r):        #Функция поиска длины
    length=2*r*3.14
    return length



class TestRoundSquare(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(round_square(2), 12.56)

    def test_integer_negativ_numbers(self):
        self.assertEqual(round_square(-2), "ValueError: radius cant be negative")
    
    def test_zero_numbers(self):
        self.assertEqual(round_square(0), 0.0)

    def test_float_positive_numbers(self):
        self.assertEqual(round_square(0.1), 0.031400000000000004 )
    
    def test_error_input(self):
        self.assertEqual(round_square('dsfsdf'), "TypeError")
        self.assertEqual(round_square(''), "TypeError")
        self.assertEqual(round_square("10**-9"), "TypeError")

if __name__ == "__main__":
    unittest.main()