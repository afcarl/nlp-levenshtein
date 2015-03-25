# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest
from stats import levenshtein, cost_function

class TestLogger(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_levenshtein(self):
    self.assertEqual(levenshtein(u'abc', u'afcde'), 3)
    self.assertEqual(levenshtein(u'żołnież', u'rzołnież'), 0.5)
    self.assertEqual(levenshtein(u'rzołnież', u'żołnież'), 0.5)

  def test_cost_function(self):
    self.assertItemsEqual(cost_function(u'rzołnież', u'żołnież', 0),
      [0.25, 0.25, 1., 1., 1., 1., 1., 0.])
    self.assertItemsEqual(cost_function(u'rzołnież', u'żołnież', 1),
      [1., 1., 0., 1., 1., 1., 1., 1.])
    self.assertItemsEqual(cost_function(u'żołnież', u'rzołnież', 0),
      [0.25, 1., 1., 1., 1., 1., 0.25])
    self.assertItemsEqual(cost_function(u'żołnież', u'rzołnież', 1),
      [0.25, 1., 1., 1., 1., 1., 0.25])

  def test_special_cases(self):
    self.assertEqual(levenshtein(u'żołnież', u'zolniez'), 0.75)
    self.assertEqual(levenshtein(u'chociaż', u'hociaż'), 0.25)
    self.assertEqual(levenshtein(u'chociarz', u'hociaż'), 0.75)
    self.assertEqual(levenshtein(u'piszę', u'pizsę'), 0.5)
    self.assertEqual(levenshtein(u'pizsę', u'piszę'), 0.5)


if __name__ == '__main__':
  unittest.main()
