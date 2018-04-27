import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config(object):

  TABLE = os.getenv('TABLE', 'users')
  ROWS_NUM = int(os.getenv('ROWS_NUM', '1'))
  INTERVAL = int(os.getenv('INTERVAL', '1'))
  METADATA = os.getenv('METADATA', './examples/metadata.json')
  LOCALE = os.getenv('LOCALE', 'en_US')
  STYLED = bool(os.getenv('STYLED', 'False') == 'True')

  PG_HOST = os.getenv('PG_HOST', 'localhost')
  PG_PORT = os.getenv('PG_PORT', '5432')
  PG_USER = os.getenv('PG_USER', 'admin')
  PG_PASSWORD = os.getenv('PG_PASSWORD', 'admin123')
  PG_DATABASE = os.getenv('PG_DATABASE', 'mydb')