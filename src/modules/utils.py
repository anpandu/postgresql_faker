def flatten(l):
  return [x for sublist in l for x in sublist]

def to_camel(text):
  splitted = [text]
  splitted = flatten([t.split(' ') for t in splitted])
  splitted = flatten([t.split('-') for t in splitted])
  splitted = flatten([t.split('_') for t in splitted])
  return ''.join([w[0].upper() + w[1:] for w in splitted])