import os
import unittest

from modules.utils import read_json, print_json
from modules.pg_faker import PgFaker
from faker import Factory
 
class TestPgFaker(unittest.TestCase):
 
  def setUp(self):
    pass
 
  def tearDown(self):
    pass
 
  def test_parse_metadata(self):
    metadata = [
      {
        "column": "id",
        "udt": "serial",
        "is_default": True
      },
      {
        "column": "email",
        "udt": "email"
      },
      {
        "column": "description",
        "udt": "text"
      },
      {
        "column": "created_at",
        "udt": "timestamp"
      },
      {
        "column": "var1",
        "options": ["a", "b", "c"]
      }
    ]
    columns, udts, is_defaults, options = PgFaker.parse_metadata(metadata)
    self.assertEqual(columns, ['id', 'email', 'description', 'created_at', 'var1'])
    self.assertEqual(udts, ['serial', 'email', 'text', 'timestamp', 'text'])
    self.assertEqual(is_defaults, [True, False, False, False, False])
    self.assertEqual(options, [[], [], [], [], ["a", "b", "c"]])
 
  def test_get_value(self):
    self.assertEqual('default', PgFaker.get_value('text', is_default=True))
    self.assertTrue(PgFaker.get_value('text', options=[1, 2, 3]) in [1, 2, 3])
    self.assertTrue(len(PgFaker.get_value('varchar(16)')) <= 16)
 
  def test_query_insert(self):
    # metadata = [
    #   {
    #     "column": "id",
    #     "udt": "serial",
    #     "is_default": True
    #   },
    #   {
    #     "column": "email",
    #     "udt": "email"
    #   },
    #   {
    #     "column": "description",
    #     "udt": "text"
    #   },
    #   {
    #     "column": "created_at",
    #     "udt": "timestamp"
    #   },
    #   {
    #     "column": "var1",
    #     "options": ["a", "b", "c"]
    #   }
    # ]
    # print PgFaker.query_insert(metadata=metadata, table='xxx', styled=True, rows=5)
    self.assertTrue(1 == 1)


if __name__ == "__main__":
  unittest.main()