from faker import Faker
from config import Config
from src.modules.pg_faker import PgFaker
from src.modules.pg_util import PgQuery
from src.modules.utils import read_json
import time

LOCALE = Config.LOCALE
TABLE = Config.TABLE
ROWS_NUM = Config.ROWS_NUM
METADATA = Config.METADATA

fake = Faker(LOCALE)
metadata = read_json(METADATA)

AUTH = {
  'host': Config.PG_HOST,
  'user': Config.PG_USER,
  'port': Config.PG_PORT,
  'password': Config.PG_PASSWORD,
  'database': Config.PG_DATABASE,
}

insert_query = PgFaker.query_insert(
  metadata=metadata,
  table=TABLE,
  rows=ROWS_NUM,
  styled=True,
  fake=fake
)

# raw = PgQuery.fetch(auth=AUTH, query='SELECT 1;')
print insert_query
print PgQuery.execute(auth=AUTH, query=insert_query)