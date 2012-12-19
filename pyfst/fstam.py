
"""
fstam.py
(C) 2012 by Damir Cavar <http://cavar.me/damir/>

The associations with state and transitions could be triggered by:
* entering a state
* leaving a state
* starting a transition (pre-write to output with transducer)
* finishing a transition (post-write to output with transducer)

The actions themselves can be:
* output to stream
* call of a procedure
* set value of a variable



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

class FSTActionMap:
   """Defines a class to contain actions that are associated with
      states and transitions."""

   self.ACTION_TYPE_OUTPUT_TO_STREAM = 0
   self.ACTION_TYPE_CALL_PROCEDURE   = 1
   self.ACTION_TYPE_SET_VARIABLE     = 2

   self.ACTION_TRIGGER_ENTER      = 0
   self.ACTION_TRIGGER_LEAVE      = 1

   def __init__(self):
      self._actionMap = {}

   def setAction(self, atype, atrigger, key, value):
      # self.actionMap
      pass

