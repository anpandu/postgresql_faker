import os
import unittest

from modules.utils import read_json, print_json
from modules.base_faker import BaseFaker
from faker import Factory
 
class TestBaseFaker(unittest.TestCase):
 
  def setUp(self):
    pass
 
  def tearDown(self):
    pass
 
  def test_generate(self):
    fake = Factory.create()

    # default
    self.assertTrue(BaseFaker.default(), 'default')

    # random
    options = ['a', 'b', 'c']
    res = BaseFaker.random(options)
    self.assertTrue(res in options)

    # datetime
    start = '2000-01-01T00:00:00.000Z'
    end = '2000-01-01T23:59:59.999Z'
    res = BaseFaker.timestamp(start, end)
    self.assertTrue(res >= start)
    self.assertTrue(res <= end)

if __name__ == "__main__":
  unittest.main()