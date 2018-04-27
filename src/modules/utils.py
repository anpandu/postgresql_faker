import json
from datetime import datetime

def read_json(filename):
  file = open(filename)
  return json.loads(file.read())

def flatten(l):
  return [x for sublist in l for x in sublist]

def to_camel(text):
  splitted = [text]
  splitted = flatten([t.split(' ') for t in splitted])
  splitted = flatten([t.split('-') for t in splitted])
  splitted = flatten([t.split('_') for t in splitted])
  return ''.join([w[0].upper() + w[1:] for w in splitted])

def get_current_time_str():
  now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
  return now