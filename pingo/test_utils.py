import unittest

import util


class StrKeyDictTest(unittest.TestCase):

    def setUp(self):
        self.d = util.StrKeyDict(
            [('2', 'two'), ('4', 'four')]
        )

    def test_getitem(self):
        with self.assertRaises(KeyError):
            self.d['1']
        with self.assertRaises(KeyError):
            self.d[1]
        assert self.d['2'] == 'two'
        assert self.d[2] == 'two'

    def test_in(self):
        assert 2 in self.d
        assert '2' in self.d

    def test_setitem(self):
        self.d[0] = 'zero'
        assert self.d['0'] == 'zero'

    def test_normalize(self):
        self.d['A0'] = 'A-zero'
        assert self.d['a0'] == 'A-zero'

    def test_update(self):
        self.d.update({6: 'six', '8': 'eight'})
        assert set(self.d.keys()) == set(['2', '4', '6', '8'])
        self.d.update([(10, 'ten'), ('12', 'twelve')])
        assert set(self.d.keys()) == set(['2', '4', '6', '8', '10', '12'])

        with self.assertRaises(TypeError):
            self.d.update([1, 3, 5])

if __name__ == '__main__':
    unittest.main()
