from faker import Faker
from src.modules.pg_faker import PgFaker
import time

fake = Faker('id_ID')

metadata = [
  ('id', 'serial', True),
  ('ops_user', 'email', False),
  ('object_type', 'varchar(16)', False),
  ('object_id', 'uuid', False),
  ('event_value', 'varchar(16)', False),
  ('event_description', 'text', False),
  ('created_at', 'timestamp', False),
  ('updated_at', 'timestamp', False),
]

while True:
  print ''
  print PgFaker.query_insert(metadata=metadata, table='xxx.ops_logs')
  time.sleep(1)


