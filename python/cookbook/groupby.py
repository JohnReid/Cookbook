"""
http://code.activestate.com/recipes/259173-groupby/
Licensed under the PSF License
"""

import sys

if sys.version_info < (3,):
  class groupby(dict):
      def __init__(self, seq, key=lambda x:x):
          for value in seq:
              k = key(value)
              self.setdefault(k, []).append(value)
      __iter__ = dict.iteritems
