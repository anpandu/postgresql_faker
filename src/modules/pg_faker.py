import json
from faker import Factory
from base_faker import BaseFaker
from utils import to_camel
    
class PgFaker(object):

  @staticmethod
  def parse_metadata(metadata):
    columns = [md.get('column', '').lower() for md in metadata]
    udts = [md.get('udt', 'text').lower() for md in metadata]
    is_defaults = [md.get('is_default', False) for md in metadata]
    options = [md.get('options', []) for md in metadata]
    return columns, udts, is_defaults, options

  @staticmethod
  def get_value(udt, is_default=False, options=[], fake=Factory.create()):
    if is_default:
      return BaseFaker.default()
    if len(options) > 0:
      return BaseFaker.random(options=options)
    if 'varchar' in udt:
      length = int(udt[8:-1])
      seed = BaseFaker.bs() if length <= 32 else BaseFaker.sentence()
      return to_camel(seed)[:length]
    value = {
      'serial': BaseFaker.serial(),
      'name': BaseFaker.name(fake=fake),
      'first_name': BaseFaker.first_name(fake=fake),
      'last_name': BaseFaker.last_name(fake=fake),
      'name': BaseFaker.name(fake=fake),
      'email': BaseFaker.email(fake=fake),
      'text': BaseFaker.text(fake=fake),
      'bs': BaseFaker.bs(fake=fake),
      'address': BaseFaker.address(fake=fake),
      'city': BaseFaker.city(fake=fake),
      'state': BaseFaker.state(fake=fake),
      'uuid': BaseFaker.uuid(),
      'default': BaseFaker.default(),
      'timestamp': BaseFaker.timestamp()
    }.get(udt, BaseFaker.default())
    return value
  
  @staticmethod
  def query_insert(metadata, table, rows=1, styled=False, fake=Factory.create()):
    # metadata
    columns, udts, is_defaults, options_list = PgFaker.parse_metadata(metadata)
    # colums
    columns_part = '(%s)' % (', '.join(columns))
    # values
    multiple_values = []
    for r in range(rows):
      values = [None for md in metadata]
      for idx, t in enumerate(metadata):
        values[idx] = PgFaker.get_value(udt=udts[idx], is_default=is_defaults[idx], options=options_list[idx], fake=fake)
      values = [v if v == 'default' else '\'%s\'' % v for v in values]
      values_part = '(%s)' % (', '.join(values))
      multiple_values += [values_part]
    # query
    query = 'INSERT INTO %s %s VALUES %s;' % (table, columns_part, ', '.join(multiple_values)) 
    query = query if not styled else 'INSERT INTO %s\n  %s\nVALUES\n  %s;' % (table, columns_part, ',\n  '.join(multiple_values)) 
    return query
