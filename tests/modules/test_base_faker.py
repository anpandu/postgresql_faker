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

if __name__ == "__main__":
  unittest.main()