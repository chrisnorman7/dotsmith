"""Various elements used throughout the interface."""

import wx, os
from louis import table_dir

class StringChoice(wx.Choice):
 """A wx.Coice which returns strings from GetValue and takes a string for SetValue."""
 def __init__(self, panel, value, choices):
  super(StringChoice, self).__init__(panel, choices = choices)
  self.SetValue(value)
 
 def GetValue(self):
  """Get the value of this control as a string."""
  return self.GetStringSelection()
 
 def SetValue(self, value):
  """Set the value of this control."""
  return self.SetStringSelection(value)

class TableChoice(StringChoice):
 """Choose a braille table."""
 def __init__(self, panel, value):
  """Create the control. Pass the parent of the control and the value as arguments."""
  super(TableChoice, self).__init__(panel, value, os.listdir(table_dir))
