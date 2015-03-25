# -*- coding: utf-8 -*-
#!/usr/bin/env python

# from __future__ import print_function
import numpy as np
import os
import sys
from stats import levenshtein, cost_function
from operator import itemgetter
from heapq import nsmallest

if __name__ == '__main__':
  if len(sys.argv) == 3:
    dictionary = sys.argv[1]
    word = unicode(sys.argv[2], "utf-8")

    lines = [line.strip() for line in open(dictionary)]
    lines_map = {}

    for line in lines:
      lines_map[line] = levenshtein(unicode(line, "utf-8"), word)
    for line, score in nsmallest(5, lines_map.items(), key=itemgetter(1)):
      print line, " : ", score

  else:
    print("python stats.py [dictionary] [word2]")

