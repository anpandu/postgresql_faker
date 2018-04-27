import json
import time
from faker import Faker
from config import Config
from src.modules.pg_faker import PgFaker
from src.modules.pg_util import PgQuery
from src.modules.utils import read_json, get_current_time_str

LOCALE = Config.LOCALE
TABLE = Config.TABLE
ROWS_NUM = Config.ROWS_NUM
INTERVAL = Config.INTERVAL
METADATA = Config.METADATA
STYLED = Config.STYLED

fake = Faker(LOCALE)
metadata = read_json(METADATA)

AUTH = {
  'host': Config.PG_HOST,
  'user': Config.PG_USER,
  'port': Config.PG_PORT,
  'password': Config.PG_PASSWORD,
  'database': Config.PG_DATABASE,
}

print json.dumps(AUTH, indent=2)
print ''

count = 0
while True:
  insert_query = PgFaker.query_insert(
    metadata=metadata,
    table=TABLE,
    rows=ROWS_NUM,
    styled=STYLED,
    fake=fake
  )
  if STYLED:
    print '[%s][%s]\n%s\n' % (get_current_time_str(), count, insert_query)
  else:
    print '[%s][%s] %s' % (get_current_time_str(), count, insert_query)
  PgQuery.execute(auth=AUTH, query=insert_query)
  count += 1
  time.sleep(INTERVAL)

