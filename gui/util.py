"""General utility functions."""

import wx, application

def do_error(message, title = 'Error', style = None):
 """Display an error message."""
 if style is None:
  style = wx.ICON_EXCLAMATION
 return wx.MessageBox(str(message), str(title), style = style)

def create_editor(filename = None):
 """Create a new editor."""
 editor = EditorFrame()
 if filename is not None:
  editor.load_file(filename)
 editor.Show(True)
 editor.Maximize(True)
 application.editors.append(editor)
 return editor

from .editor import EditorFrame
