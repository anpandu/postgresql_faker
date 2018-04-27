import json
from faker import Factory
from base_faker import BaseFaker
from utils import to_camel
    
class PgFaker(object):

  @staticmethod
  def parse_metadata(metadata):
    columns = [md[0].lower() for md in metadata]
    udts = [md[1].lower() for md in metadata]
    is_defaults = [md[2] for md in metadata]
    return columns, udts, is_defaults

  @staticmethod
  def get_value(udt, is_default=False, fake=Factory.create()):
    value = BaseFaker.default()
    if not is_default:
      value = {
        'serial': BaseFaker.serial(),
        'name': BaseFaker.name(fake=fake),
        'first_name': BaseFaker.first_name(fake=fake),
        'last_name': BaseFaker.last_name(fake=fake),
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
      if 'varchar' in udt:
        length = int(udt[8:-1])
        seed = BaseFaker.bs() if length <= 32 else BaseFaker.sentence()
        value = to_camel(seed)[:length]
    return value
  
  @staticmethod
  def query_insert(metadata, table, fake=Factory.create()):
    fake = Factory.create()
    columns, udts, is_defaults = PgFaker.parse_metadata(metadata)
    values = [None for md in metadata]
    for idx, t in enumerate(metadata):
      values[idx] = PgFaker.get_value(udt=udts[idx], is_default=is_defaults[idx], fake=fake)
    values = [v if v == 'default' else '\'%s\'' % v for v in values]
    columns_part = '(%s)' % (', '.join(columns))
    values_part = '(%s)' % (', '.join(values))
    query = 'INSERT INTO %s %s\nVALUES %s;' % (table, columns_part, values_part) 
    return query

if __name__ == '__main__':
  fake = Factory.create()
  print 'serial      = ', json.dumps(PgFaker.get_value('serial', False, fake))
  print 'name        = ', json.dumps(PgFaker.get_value('name', False, fake))
  print 'first_name  = ', json.dumps(PgFaker.get_value('first_name', False, fake))
  print 'last_name   = ', json.dumps(PgFaker.get_value('last_name', False, fake))
  print 'email       = ', json.dumps(PgFaker.get_value('email', False, fake))
  print 'text        = ', json.dumps(PgFaker.get_value('text', False, fake))
  print 'bs          = ', json.dumps(PgFaker.get_value('bs', False, fake))
  print 'address     = ', json.dumps(PgFaker.get_value('address', False, fake))
  print 'city        = ', json.dumps(PgFaker.get_value('city', False, fake))
  print 'state       = ', json.dumps(PgFaker.get_value('state', False, fake))
  print 'uuid        = ', json.dumps(PgFaker.get_value('uuid', False, fake))
  print 'default     = ', json.dumps(PgFaker.get_value('default', False, fake))
  print 'timestamp   = ', json.dumps(PgFaker.get_value('timestamp', False, fake))
  print 'varchar(32) = ', json.dumps(PgFaker.get_value('varchar(32)', False, fake))
  print 'varchar(64) = ', json.dumps(PgFaker.get_value('varchar(64)', False, fake))