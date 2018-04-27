import os
import re

class Config(object):

  TABLE = os.getenv('TABLE', 'users')
  ROWS_NUM = int(os.getenv('ROWS_NUM', '1'))
  METADATA = os.getenv('METADATA', './examples/metadata.json')
  LOCALE = os.getenv('LOCALE', 'en_US')