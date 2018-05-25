from faker import Factory
from uuid import uuid4
from random import randrange
from datetime import datetime 

class BaseFaker(object):

  @staticmethod
  def default():
    return 'default'

  @staticmethod
  def random(options=[]):
    return options[randrange(len(options))]

  @staticmethod
  def uuid():
    return str(uuid4())
  
  @staticmethod  
  def text(length=255, fake=Factory.create()):
    return fake.sentence()[:length]
  
  @staticmethod  
  def email(fake=Factory.create()):
    return fake.email()
  
  @staticmethod  
  def address(fake=Factory.create()):
    return fake.address()
  
  @staticmethod  
  def city(fake=Factory.create()):
    return fake.city()
  
  @staticmethod  
  def state(fake=Factory.create()):
    return fake.state()
  
  @staticmethod  
  def bs(fake=Factory.create()):
    return fake.bs()
  
  @staticmethod  
  def bs_camel(fake=Factory.create()):
    return _to_camel(fake.bs())
  
  @staticmethod  
  def name(fake=Factory.create()):
    return fake.name()
  
  @staticmethod  
  def first_name(fake=Factory.create()):
    return fake.first_name()
  
  @staticmethod  
  def last_name(fake=Factory.create()):
    return fake.last_name()
  
  @staticmethod  
  def sentence(fake=Factory.create()):
    return fake.sentence()
  
  @staticmethod  
  def timestamp(start='1970-01-01T00:00:00.000Z', end='2099-12-12T23:59:59.999Z'):
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
    start_ts = float(datetime.strptime(start, fmt).strftime('%s.%f')) * 1000.0
    end_ts = float(datetime.strptime(end, fmt).strftime('%s.%f')) * 1000.0
    range_ts = randrange(end_ts - start_ts) if end_ts > start_ts else 0
    now = (start_ts + range_ts) / 1000.0
    now = datetime.fromtimestamp(now).strftime(fmt)
    return now
  
  @staticmethod  
  def serial():
    return randrange(65536)