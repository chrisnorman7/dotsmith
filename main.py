"""The main entry point to the program."""

if __name__ == '__main__':
 import application, logging, os, os.path
 from default_argparse import parser
 application.args = parser.parse_args()
 logging.basicConfig(stream = application.args.log_file, level = application.args.log_level)
 logging.info('Starting %s, version %s.', application.name, application.version)
 import config
 logging.info('Config file: %s.', config.config.filename)
 from gui.util import create_editor
 create_editor()
 application.app.MainLoop()
 logging.info('Dumping configuration to disk...')
 if not os.path.isdir(application.data_dir):
  logging.info('Creating config directory %s.', application.data_dir)
  os.makedirs(application.data_dir)
 config.config.write(indent = 1)
 logging.info('Goodbye.')
