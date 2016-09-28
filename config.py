"""Application configuration."""

import application, os.path, wx
from simpleconf import Section, Option, validators

class Config(Section):
 filename = os.path.join(application.data_dir, 'config.json')
 class page(Section):
  """Page configuration."""
  title = 'Page'
  width = Option(29, title = '&Characters per line', validator = validators.Integer(min = 1))
  height = Option(27, title = '&Lines per page', validator = validators.Integer(min = 1))
  margin_top = Option(0, title = '&Top margin', validator = validators.Integer(min = 0))
  margin_binding = Option(0, title = '&Binding Margin', validator = validators.Integer(min = 0))
  option_order = [width, height, margin_top, margin_binding]
 
 class user(Section):
  """User info."""
  title = 'User Info'
  name = Option(wx.GetUserName(), title = '&Name')
  organisation = Option('', title = '&Organisation')
  email = Option(wx.GetEmailAddress(), title = '&Email')
  option_order = [name, organisation, email]
 section_order = [user, page]

config = Config()