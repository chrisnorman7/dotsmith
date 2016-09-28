"""The menu bar for each editor."""

import wx, config
from simpleconf.dialogs.wx import SimpleConfWxDialog
from ..util import create_editor, translate

class MenuBar(wx.MenuBar):
 def __init__(self, frame):
  super(MenuBar, self).__init__()
  self.file_menu = wx.Menu()
  self.new_menu = wx.Menu()
  frame.Bind(wx.EVT_MENU, lambda event: create_editor(), self.new_menu.Append(wx.ID_NEW, '&New\tCTRL+N', 'Create an empty file and load it into a new editor.'))
  frame.Bind(wx.EVT_MENU, lambda event, frame = frame: create_editor(frame.filename), self.new_menu.Append(wx.ID_ANY, '&Duplicate\tCTRL+SHIFT+N', 'Load the file from this editor into a new editor.'))
  self.file_menu.AppendSubMenu(self.new_menu, '&New')
  frame.Bind(wx.EVT_MENU, lambda event, frame = frame: translate(frame.entry.GetValue()), self.file_menu.Append(wx.ID_ANY, '&Translate...\tCTRL+T', 'Translate the current document from print to braille.'))
  self.Append(self.file_menu, '&File')
  self.edit_menu = wx.Menu()
  frame.Bind(wx.EVT_MENU, lambda event, frame = frame: frame.entry.Clear() if not frame.entry.GetValue() or wx.MessageBox('Are you sure you want to clear the document?', 'Really Clear', style = wx.ICON_EXCLAMATION | wx.YES_NO) == wx.YES else None, self.edit_menu.Append(wx.ID_ANY, '&Clear\tCTRL+BACK', 'Clear the current document.'))
  self.preferences_menu = wx.Menu()
  for section in config.config.section_order:
   frame.Bind(wx.EVT_MENU, lambda event, section = section: SimpleConfWxDialog(section).Show(True), self.preferences_menu.Append(wx.ID_ANY, '&%s...' % section.title, 'View and edit the %s preferences.' % section.title.lower()))
  self.Append(self.preferences_menu, '&Preferences')
  self.Append(self.edit_menu, '&Edit')
