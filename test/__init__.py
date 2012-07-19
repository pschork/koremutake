import unittest
from koremutake import encode, decode

class test_koremutake(unittest.TestCase):

    def test_encode(self):
        assert encode(0) == 'ba'
        assert encode(10610353957) == 'koremutake'
        assert encode(31223361103) == 'prikunubrite'
        assert encode(244793201) == 'pribritragry'
        
    def test_decode(self):
        assert decode('ba') == 0
        assert decode('koremutake') == 10610353957
        assert decode('prikunubrite') == 31223361103
        assert decode('pribritragry') == 244793201

    def test_encode_negative(self):
        try:
            encode(-1)
            raise Exception,'Invalid value accepted'
        except AssertionError, e:
            pass

    def test_decode_invalid(self):
        try:
            decode('koremuutake')
            raise Exception,'Invalid encoding accepted'
        except AssertionError, e:
            pass

if __name__ == '__main__':
    unittest.main()
