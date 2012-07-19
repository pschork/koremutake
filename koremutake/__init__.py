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
# Encoding algorithm adapted from http://code.activestate.com/recipes/111286

__name__ = 'koremutake'
__version__ = '1.0.4'
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
    assert value >= 0, 'Value to encode must be unsigned'
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
        assert value[:2] in phonemes or value[:3] in phonemes,\
            "Failed to decode '%s' @ %s digit" % (orig, len(orig) - len(value))
        if value[:2] in phonemes:
            bit,value = value[:2],value[2:]
        else:
            bit,value = value[:3],value[3:]   
        x = x*len(phonemes) + phonemes.index(bit)
    return x
