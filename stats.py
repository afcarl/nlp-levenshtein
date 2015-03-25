# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import sys
from operator import itemgetter

special_characters = {
  u'ą': {u'a'},
  u'a': {u'ą'},
  u'ę': {u'e'},
  u'e': {u'ę'},
  u'z': {u'ż', u'ź'},
  u'ż': {u'z', u'ź'},
  u'ź': {u'z', u'ż'},
  u'ó': {u'u', u'o'},
  u'o': {u'ó'},
  u'l': {u'ł'},
  u'ł': {u'l'},
  u'n': {u'ń'},
  u'ń': {u'n'},
  u'c': {u'ć'},
  u'ć': {u'c'},
  u's': {u'ś'},
  u'ś': {u's'},
  u'o': {u'ó'}
}

def cost_function(target, source, index):
  tab = np.array([1.]*len(target))
  for i in xrange(0, len(tab)):
    if target[i] == source[index]:
      tab[i] = 0
    else:
      if source[index] in special_characters and target[i] in special_characters[source[index]]:
        tab[i] = 0.25
      else:
        if index - 1 >= 0:
          if ((source[index-1] == u'r' and source[index] == u'z' and target[i] == u'ż')
            or (source[index-1] == u'c' and source[index] == u'h' and target[i] == u'h')):
            tab[i] = 0.25
          if ((i - 1 >= 0) and (source[index-1] == target[i] and source[index] == target[i-1])):
              tab[i] = 0.25
        if index + 1 < len(source):
          if ((source[index] == u'r' and source[index+1] == u'z' and target[i] == u'ż')
            or (source[index] == u'c' and source[index+1] == u'h' and target[i] == u'h')):
            tab[i] = 0.25
          if ((i + 1 < len(target)) and (source[index+1] == target[i] and source[index] == target[i+1])):
            tab[i] = 0.25
        if i - 1 >= 0:
          if ((target[i-1] == u'r' and target[i] == u'z' and source[index] == u'ż')
            or (target[i-1] == u'c' and target[i] == u'h' and source[index] == u'h')):
            tab[i] = 0.25
        if i + 1 < len(target):
          if ((target[i] == u'r' and target[i+1] == u'z' and source[index] == u'ż')
            or (target[i] == u'c' and target[i+1] == u'h' and source[index] == u'h')):
            tab[i] = 0.25
  return tab

def levenshtein(source, target, verbose=False):
  if len(target) == 0:
    return len(source)

  source = np.array(tuple(source))
  target = np.array(tuple(target))

  previous_row = np.arange(target.size + 1.)
  matrix = previous_row
  for i in xrange(len(source)):
      current_row = previous_row + 1
      current_row[1:] = previous_row[1:] + cost_function(target, source, i)

      if verbose:
        print "prev", i
        print current_row
      current_row[1:] = np.minimum(
          current_row[1:],
          np.add(previous_row[:-1], cost_function(target, source, i)))
      if verbose:
        print "prev + cost_function", i
        print np.add(previous_row[:-1], cost_function(target, source, i))
        print "cost_function:", i, " target: ", target, " source[i]: ", source[i]
        print cost_function(target, source, i)
      for j in xrange(1,len(current_row)):
        current_row[j] = np.minimum(
          current_row[j],
          current_row[j-1] + cost_function(target, source, i)[j-1])

      previous_row = current_row
      matrix = np.vstack([matrix, previous_row])
  if verbose:
    print matrix.T

  return previous_row[-1]

if __name__ == '__main__':
  if len(sys.argv) == 3:
    w1 = unicode(sys.argv[1], "utf-8")
    w2 = unicode(sys.argv[2], "utf-8")

    print levenshtein(w1, w2)

  else:
    print("python stats.py [word1] [word2]")

