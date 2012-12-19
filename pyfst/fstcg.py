
"""
fstcg.py
(C) 2012 by Damir Cavar <http://cavar.me/damir/>

The FSTCodeGenerator class implements algorithms for the conversion
and export of FST-instances.



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



class FSTCodeGenerator:
   """Generates """

   def __init__(self, myFST):
      self._FST = myFST

   def getDOT(self):
      """Returns a DOT (Graphviz) representation of the underlying Finite State Transducer."""
      return ""

   def getCJC(self):
      """Returns a C-code implementation of the underlying Finite State Transducer.
         The C-code is using labels and goto statements and does not involve dynamic variables
         except of the read and write streams."""
      return ""



if __name__ == "__main__":
   import fst
   myFST = FST()
   myFSTCG = FSTCodeGenerator(myFST)
   myFSTCG.getCJC()
   myFSTCG.getDOT()

