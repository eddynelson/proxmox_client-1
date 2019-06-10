import unittest

from main import ProxmoxClient

CONFIG = {
  "base_url": "142.44.137.41",
  "verify_ssl": False,
  "password": "010203",
  "username": "root@pam"
}


class ProxmoxClientTest(unittest.TestCase):
    def setUp(self):
        self.client = ProxmoxClient(CONFIG)
        self.type_list = type([])
        self.type_dict = type({})
        self.success_result = { "message": 'Success!!' }

    def test_get_ticket(self):
        try:
            client = ProxmoxClient(CONFIG)
        except:
            self.fail("Error to get ticket")

        self.assertTrue(True)

    def test_get_cluster_tasks(self):
        result = self.client.get_cluster_tasks()
        self.assertTrue(type(result) is self.type_list)
    
    def test_get_cluster_status(self):
        result = self.client.get_cluster_status()
        self.assertTrue(type(result) is self.type_list)

    def test_get_cluster_resources(self):
        result = self.client.get_cluster_resources()
        self.assertTrue(type(result) is self.type_list)

    def test_get_cluster_nextid(self):
        result = self.client.get_cluster_nextid()
        self.assertTrue(type(result) is int)

    def test_get_cluster_logs(self):
        result = self.client.get_cluster_logs()
        self.assertTrue(type(result) is self.type_list)

    def test_get_cluster_replications(self):
        result = self.client.get_cluster_resources()
        self.assertTrue(type(result) is self.type_list)

    def test_update_cluster_options(self):
        result = self.client.update_cluster_options(data={ 'language': 'en' })
        self.assertEqual(result, self.success_result)

if __name__ == '__main__':
    unittest.main()