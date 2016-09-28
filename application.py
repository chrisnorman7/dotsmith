"""App-specific storage."""

import wx

app = wx.App()

name = 'Dotsmith'
version = '0.0.0'

app.SetAppName(name)
app.SetAppDisplayName('%s %s' % (name, version))

standard_paths = wx.StandardPaths.Get()

data_dir = standard_paths.GetUserDataDir()
local_data_dir = standard_paths.GetUserLocalDataDir()

editors = [] # The open editors.
