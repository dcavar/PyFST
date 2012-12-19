
"""
fstsm.py
(C) 2012 by Damir Cavar <http://cavar.me/damir/>


The FSTSymbolMap-class provides a data storage for multi-character
symbols and their mapping to unique single character symbols based
on the Unicode V. XXX character map.

Currently, this mapping is not necessary for FSTs, it can be helpful
to reduce the size and potentially the speed of the processing, by
reducing strings to ints.



ASSUMPTIONS:

We assume here that the code runs under Python 3.x.
We do not assume that the code will run under Python 2.x, and
we might not invest time or effort to make it Python 2.x
compatible.



LICENSE:

Copyright 2012 by Damir Cavar (http://cavar.me/damir/)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

See LICENSE.md.
"""



class FSTSymbolMap:
   """A class for maintaining the mapping of multi-character symbols
      to unique byte-sequence symbol used internal to FST instances."""

   self._symbolMap = None
   self._alphabet  = None

   def __init__(self):
      self._symbolMap = {}

   def setAlphabet(self, alphabet):
      self._alphabet = set(alphabet)

   def getSymbol(self, symbol):
      return self._symbolMap.get(symbol, "")

   def addSymbol(self, symbol):
      # TODO:
      # identify a unique unicode char to be used for symbol (a multi-char
      # symbol)
      self._symbolMap[symbol] = symbol




if __name__ == "__main__":
   mySM = FSTSymbolMap()


