Python Koremutake
=================

Convert to and from Koremutake Memorable Random Strings.

Koremutake is a 128bit MeRS encoding algorithm that can convert any large, 
unsigned number into a memorable sequence of phonetically unique syllables.

See http://shorl.com/koremutake.php for details

To install, run 'sudo easy_install koremutake'

```python
>>> import koremutake
>>> koremutake.encode(10610353957)
'koremutake'
>>> koremutake.decode('koremutake')
10610353957
```
