"""Application configuration."""

import application, os, os.path, wx
from gui.elements import TableChoice
from simpleconf import Section, Option, validators
from louis import table_dir

class Config(Section):
 filename = os.path.join(application.data_dir, 'config.json')
 class user(Section):
  """User info."""
  title = 'User Info'
  name = Option(wx.GetUserName(), title = '&Name')
  organisation = Option('', title = '&Organisation')
  email = Option(wx.GetEmailAddress(), title = '&Email')
  option_order = [name, organisation, email]
 
 class page(Section):
  """Page configuration."""
  title = 'Page'
  width = Option(29, title = '&Characters per line', validator = validators.Integer(min = 1))
  height = Option(27, title = '&Lines per page', validator = validators.Integer(min = 1))
  margin_top = Option(0, title = '&Top margin', validator = validators.Integer(min = 0))
  margin_binding = Option(0, title = '&Binding Margin', validator = validators.Integer(min = 0))
  option_order = [width, height, margin_top, margin_binding]
 
 class braille(Section):
  title = 'Braille'
  translation_table = Option(os.listdir(table_dir)[0], title = 'Default &Translation Table', control = lambda option, window: TableChoice(window.panel, option.value))
  option_order = [translation_table]
 
 section_order = [user, braille, page]

config = Config()