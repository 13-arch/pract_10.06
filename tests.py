import pract1306 as p
import unittest


class Test_Equalize(unittest.TestCase):
    def test_negative_number(self):
        self.assertDictEqual(p.igorek(1,-2,1),{"ValueError":"cant sqrt negative"})
    
    def test_positive_numbers(self):
        self.assertGreater(p.igorek(1,1,1),-1)
        self.assertLess(p.igorek(1,1,1),1)
    
    def test_zero_numbers(self):
        self.assertListEqual(p.igorek(0,0,0), ['there is zero division',])

    
    def test_input(self):
        self.assertSetEqual(p.igorek("","",""), {"this is not number"})
        self.assertSetEqual(p.igorek('asd','asd','asd'), {"this is not number"})
        self.assertSetEqual(p.igorek(1,"10**-9",2), {"this is not number"})

if __name__=="__main__":
    unittest.main()
