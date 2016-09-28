"""
The main editor.

This is where print should be edited.
"""

import wx, application
from .util import do_error
from .menus.menubar import MenuBar

class EditorFrame(wx.Frame):
 def __init__(self):
  """Create a new editor."""
  super(EditorFrame, self).__init__(None, title = application.name)
  self.filename = None # set with load_file.
  s = wx.BoxSizer(wx.VERTICAL)
  p = wx.Panel(self)
  self.entry = wx.TextCtrl(p, style = wx.TE_MULTILINE | wx.TE_RICH2)
  s.Add(self.entry, 1, wx.GROW)
  p.SetSizerAndFit(s)
  self.Bind(wx.EVT_CLOSE, self.on_close)
  self.SetMenuBar(MenuBar(self))
 
 def load_file(self, filename):
  """Load a file into this editor."""
  try:
   with open(filename, 'r') as f:
    self.entry.SetValue(f.read())
   self.filename = filename
  except Exception as e:
   do_error(e, 'Error Loading %s' % filename)
 
 def on_close(self, event):
  """The frame is about to close; remove it from the list of open editors."""
  event.Skip()
  application.editors.remove(self)
