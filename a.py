from faker import Faker
from src.modules.pg_faker import PgFaker
import time

fake = Faker('id_ID')

metadata = [
    {
      "column": "id",
      "udt": "serial",
      "is_default": True
    },
    {
      "column": "ops_user",
      "udt": "email",
      "is_default": False
    },
    {
      "column": "object_type",
      "udt": "varchar(16)",
      "is_default": False
    },
    {
      "column": "object_id",
      "udt": "uuid",
      "is_default": False
    },
    {
      "column": "event_value",
      "udt": "varchar(16)",
      "is_default": False
    },
    {
      "column": "event_description",
      "udt": "text",
      "is_default": False
    },
    {
      "column": "created_at",
      "udt": "timestamp",
      "is_default": False
    },
    {
      "column": "updated_at",
      "udt": "timestamp",
      "is_default": False
    }
  ]

while True:
  print ''
  print PgFaker.query_insert(
          metadata=metadata,
          table='xxx.ops_logs',
          rows=5,
          styled=True,
          fake=fake
        )
  time.sleep(1)


