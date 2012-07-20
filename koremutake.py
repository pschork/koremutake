"""
Convert to and from Koremutake Memorable Random Strings.

Koremutake is a 128bit MeRS encoding algorithm that can convert any large, 
unsigned number into a memorable sequence of phonetically unique syllables.

See http://shorl.com/koremutake.php for details

>>> import koremutake
>>> koremutake.encode(10610353957)
'koremutake'
>>> koremutake.decode('koremutake')
10610353957
"""
import unittest

__author__ = 'Patrick Schork <patrick@schork.com>'

__all__ = ['encode','decode']

phonemes = ['ba','be','bi','bo','bu','by','da','de','di','do','du','dy','fa',
            'fe','fi','fo','fu','fy','ga','ge','gi','go','gu','gy','ha','he',
            'hi','ho','hu','hy','ja','je','ji','jo','ju','jy','ka','ke','ki',
            'ko','ku','ky','la','le','li','lo','lu','ly','ma','me','mi','mo',
            'mu','my','na','ne','ni','no','nu','ny','pa','pe','pi','po','pu',
            'py','ra','re','ri','ro','ru','ry','sa','se','si','so','su','sy',
            'ta','te','ti','to','tu','ty','va','ve','vi','vo','vu','vy','bra',
            'bre','bri','bro','bru','bry','dra','dre','dri','dro','dru','dry',
            'fra','fre','fri','fro','fru','fry','gra','gre','gri','gro','gru',
            'gry','pra','pre','pri','pro','pru','pry','sta','ste','sti','sto',
            'stu','sty','tra','tre']

def encode(value):
    "Encode unsigned integer value to Koremutake string"
    key = ""
    if value < 0: 
        raise ValueError('Encode value must be a positive integer')
    if value == 0:
        return phonemes[0]
    while value > 0:
        digit = value % len(phonemes)
        key = phonemes[digit] + key
        value /= len(phonemes)
    return key

def decode(value):
    "Decode Koremutake string to unsigned integer value"
    orig = value
    x=long(0)
    while value:
        if value[:2] in phonemes:
            bit,value = value[:2],value[2:]
        else:
            bit,value = value[:3],value[3:]   
        x = x*len(phonemes) + phonemes.index(bit)
    return x

class test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode(0), "ba")
        self.assertEqual(encode(127), "tre")
        self.assertEqual(encode(128), "beba")
        self.assertEqual(encode(256), "biba")
        self.assertEqual(encode(128**2), "bebaba")
        self.assertEqual(encode(128**2 - 1), "tretre")
        self.assertEqual(encode(128**3), "bebababa")
        self.assertEqual(encode(128**3 - 1), "tretretre")
        self.assertEqual(encode(10610353957), "koremutake")
        self.assertEqual(encode(4398046511103), "tretretretretretre")

        # Negative numbers can't be converted
        self.assertRaises(ValueError, encode, -1)

    def test_decode(self):
        self.assertEqual(decode("ba"), 0)
        self.assertEqual(decode("tre"),127)
        self.assertEqual(decode("beba"), 128)
        self.assertEqual(decode("biba"), 256)
        self.assertEqual(decode("bebaba"), 128**2)
        self.assertEqual(decode("tretre"), 128**2 - 1)
        self.assertEqual(decode("bebababa"), 128**3)
        self.assertEqual(decode("tretretre"), 128**3 - 1)
        self.assertEqual(decode("koremutake"), 10610353957)
        self.assertEqual(decode("tretretretretretre"), 4398046511103)
        self.assertEqual(decode("baba"), 0)
        self.assertEqual(decode("bababababa"), 0)
        self.assertEqual(decode("babatre"), 127)

        # Invalid koremutake strings
        self.assertRaises(ValueError, decode, "foo")
        self.assertRaises(ValueError, decode, "kooremutake")
        self.assertRaises(ValueError, decode, "bab")

if __name__ == '__main__':
    unittest.main()
