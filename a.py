from faker import Faker
from config import Config
from src.modules.pg_faker import PgFaker
from src.modules.utils import read_json
import time

LOCALE = Config.LOCALE
TABLE = Config.TABLE
ROWS_NUM = Config.ROWS_NUM
METADATA = Config.METADATA

fake = Faker(LOCALE)
metadata = read_json(METADATA)

while True:
  print ''
  print PgFaker.query_insert(
          metadata=metadata,
          table=TABLE,
          rows=ROWS_NUM,
          styled=True,
          fake=fake
        )
  time.sleep(1)


