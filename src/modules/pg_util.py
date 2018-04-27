import psycopg2

import datetime

def _connect(auth):
  host = auth['host'] if 'host' in auth else ''
  port = auth['port'] if 'port' in auth else '5432'
  user = auth['user'] if 'user' in auth else ''
  password = auth['password'] if 'password' in auth else ''
  database = auth['database'] if 'database' in auth else ''
  conn = None
  try:
    conn = psycopg2.connect(host=host,
                            port=port,
                            user=user,
                            password=password,
                            database=database)
    cur = conn.cursor()
    return conn, cur
  except (Exception, psycopg2.DatabaseError) as error:
    raise error

class PgQuery(object):

  @staticmethod
  def execute(auth={}, query=''):
    conn, cursor = _connect(auth)
    cursor.execute(query)
    cursor.close()
    conn.commit()
    conn.close()
    return True

  @staticmethod
  def fetch(auth={}, query=''):
    if auth == {}:
      return query
    else:
      conn, cursor = _connect(auth)
      cursor.execute(query)
      objects_list = []
      for row in cursor:
        d = [e for e in row]
        objects_list.append(d)
      cursor.close()
      conn.close()
      return objects_list