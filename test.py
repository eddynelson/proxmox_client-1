import unittest

from main import ProxmoxClient

CONFIG = {
  "base_url": "142.44.137.41",
  "verify_ssl": False,
  "password": "010203",
  "username": "root@pam"
}


class ProxmoxClientTest(unittest.TestCase):
  def test_get_ticket(self):
      try:
          self.client = ProxmoxClient(CONFIG)
      except:
          self.fail("Error to get ticket")

      self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()