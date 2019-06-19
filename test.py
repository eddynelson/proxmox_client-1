import unittest

from main import ProxmoxClient

CONFIG = {
  "base_url": "192.168.1.21",
  "verify_ssl": False,
  "password": "010203",
  "username": "root@pam"
}

# Requirement for run this file:
# 1. Vm or container for clonning and set vmid in setUp method
# 2. Vm or container for template and set vmid in setUp method
# 3. Vm or container for remove and set vmid in setUp method
# 4. Vm or container for other and set vmid in setUp method
# 5. Change node name in setUp method


class ProxmoxClientTest(unittest.TestCase):
    def setUp(self):
        self.client = ProxmoxClient(CONFIG)
        self.type_list = type([])
        self.type_dict = type({})
        self.success_result = { "message": 'Success!!' }
        self.node = "eddy"

        #nodes
        self.vm_for_clonning = 100
        self.vm_for_template = 101
        self.vm_for_remove = 102
        self.vm_for_other = 103
        self.nextid = self.client.get_nextid()

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

    # Containers
    def test_get_all_ct(self):
        result = self.client.get_all_ct(data={ "node": self.node })
        self.assertTrue(type(result) is self.type_list)

    def test_get_nextid(self):
        result = self.client.get_nextid()
        self.assertTrue(type(result) is int)

    def test_get_config_ct(self):
        result = self.client.get_config_ct(data={ "node": self.node, "vmid": self.vm_for_other })
        self.assertTrue(type(result) is self.type_dict)

    def test_create_snapshot(self):
        result = self.client.create_snapshot(data={ "node": self.node, 'vmid': self.vm_for_other, "snapname": 'any' })
        self.assertEqual(result, self.success_result)

    def test_start_ct(self):
        result = self.client.start_ct(data={ "node": self.node, 'vmid': self.vm_for_other })
        self.assertEqual(result, self.success_result)

    def test_stop_ct(self):
        result = self.client.stop_ct(data={ "node": self.node, 'vmid': self.vm_for_other })
        self.assertEqual(result, self.success_result)

    def test_get_snapshots(self):
        result = self.client.get_snapshots(data={ "node": self.node, "vmid": self.vm_for_other })
        self.assertTrue(type(result) is self.type_list)

    def test_get_snapshot(self):
        result = self.client.get_snapshot(data={ "node": self.node, "vmid": self.vm_for_other, "snapname": "any" })
        self.assertTrue(type(result) is self.type_dict)

    def test_clone_ct(self):
        result = self.client.clone_ct(data={ "node": self.node, 'vmid':self.vm_for_clonning})
        self.assertEqual(result, self.success_result)
    
    def test_create_template(self):
        result = self.client.create_template(data={ "node": self.node, 'vmid': self.vm_for_template })
        self.assertEqual(result, self.success_result)

    def test_update_config_ct(self):
        result = self.client.update_config_ct(data={ "node": self.node, 'vmid': self.vm_for_other, "cores": 2 })
        self.assertEqual(result, self.success_result)

    def test_update_snapshot(self):
        result = self.client.update_snapshot(data={
            "node": self.node, 
            'vmid': self.vm_for_other, 
            "snapname": "any", 
            "description": "other" 
        })
        self.assertEqual(result, self.success_result)

    def test_rollback_snapshot(self):
        result = self.client.rollback_snapshot(data={
            "node": self.node, 
            'vmid': self.vm_for_other, 
            "snapname": "any" 
        })
        self.assertEqual(result, self.success_result)

    def test_delete_snapshot(self):
        result = self.client.delete_snapshot(data={
            "node": self.node, 
            "vmid": self.vm_for_other, 
            "snapname": "any"
        })
        self.assertEqual(result, self.success_result)

    def test_delete_ct(self):
        result = self.client.delete_ct(data={
            "node": self.node,
            "vmid": self.vm_for_remove
        })
        self.assertEqual(result, self.success_result)

if __name__ == '__main__':
    unittest.main()