#!/usr/bin/env python3

"""
fst.py
(C) 2012 by Damir Cavar <http://cavar.me/damir/>



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

import fstSymbolMapping


class FST:
   """A Finite State Transducer class for weighted finite state transducers."""

   def __init__(self):
      """ """
      self._states        = set()
      self._startstate    = 0
      # self._input         = {}
      self._actionTable   = None
      self._symbolMapping = None
      self._finalStates   = set()
      self._alphabet      = set()

   def isDeterministic(self):
      """ """
      return True

   def numStates(self):
      """ """
      return None

   def numTransitions(self):
      """ """
      return None

   def getStartState(self):
      """ """
      return None

   def setWeight(self):
      """ """
      pass

   def addTransition(self):
      """ """
      pass

   def removeTransition(self):
      """ """
      pass

   def getTransition(self, fromState, inputSymbol, outputSymbol, toState, weight):
      """ """
      pass



if __name__ == "__main__":
   myFst = FST()

