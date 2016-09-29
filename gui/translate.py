"""A frame to translate from print to braille."""

import wx, config
from wx.lib.sized_controls import SizedFrame
from wx.lib.intctrl import IntCtrl
from .elements import TableChoice
from .util import create_editor
from louis import translate, table_path

class TranslateFrame(SizedFrame):
 """The frame that handles the translation options."""
 def __init__(self, text):
  """Translate text."""
  self.text = text
  super(TranslateFrame, self).__init__(None, title = 'Translation Options')
  self.Bind(wx.EVT_SHOW, self.on_show)
  p = self.GetContentsPane()
  p.SetSizerType('form')
  wx.StaticText(p, label = '&Translation Table')
  self.translation_table = TableChoice(p, config.config.braille['translation_table'])
  width = config.config.page.width
  wx.StaticText(p, label = 'Page &Width')
  self.width = IntCtrl(p, value = width.value, min = width.validator.min)
  height = config.config.page.height
  wx.StaticText(p, label = 'Page &Height')
  self.height = IntCtrl(p, value = height.value, min = height.validator.min)
  self.ok = wx.Button(p, label = '&OK')
  self.ok.SetDefault()
  self.ok.Bind(wx.EVT_BUTTON, self.on_ok)
  self.cancel = wx.Button(p, label = '&Cancel')
  self.cancel.Bind(wx.EVT_BUTTON, lambda event: self.Close(True))
 
 def on_ok(self, event):
  """The OK button was pressed."""
  text = ''
  for line in self.text.split('\n'):
   text += '%s\n' % translate([table_path(self.translation_table.GetValue())], line)[0]
  f = create_editor()
  f.set_text(text)
  self.Close(True)
  f.Show(True)
  f.Maximize(True)
 
 def on_show(self, event):
  """Show the window."""
  event.Skip()
  self.Maximize(True)
