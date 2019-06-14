import requests
import json

MSG = { "message": 'Success!!' }

class ProxmoxClient():
    # Init config
    def __init__(self, config):
        self._base_url = config['base_url']
        self._verify_ssl = config['verify_ssl']
        self._username = config['username']
        self._password = config['password']

        # security
        self._ticket = None
        self._token = None
        self._cookies = {}

        self.api_url = 'https://'+self._base_url+':8006/api2/json'

        self._get_ticket()

    def _get_ticket(self):
        res = requests.post(
          self.api_url + '/access/ticket', 
          verify = self._verify_ssl,
          data = [('username', self._username), ('password', self._password)]
        )

        res.raise_for_status()

        data = res.json()['data']
        self._ticket = data['ticket']
        self._token = data['CSRFPreventionToken']

        self._cookies = { 'PVEAuthCookie': self._ticket }

    #Cluster
    def get_cluster_tasks(self):
        res = requests.get(
          self.api_url + '/cluster/tasks',
          verify = False,
          cookies = self._cookies
        )

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_status(self):
        res = requests.get(
          self.api_url + '/cluster/status',
          verify = False,
          cookies = self._cookies
        )

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_resources(self):
        res = requests.get(
          self.api_url + '/cluster/resources',
          verify = False,
          cookies=self._cookies
        )

        res.raise_for_status()

        return res.json()['data']
    
    def get_cluster_nextid(self):
        res = requests.get(
          self.api_url + '/cluster/nextid',
          verify = False,
          cookies = self._cookies
        )

        res.raise_for_status()

        return int(res.json()['data'])

    def get_cluster_logs(self):
        res = requests.get(
          self.api_url + '/cluster/log',
          verify = False,
          cookies = self._cookies
        )

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_replications(self):
        res = requests.get(
          self.api_url + '/cluster/replication',
          verify = False,
          cookies = self._cookies
        )

        res.raise_for_status()

        return res.json()['data']

    def update_cluster_options(self, data):
        res = requests.put(
          self.api_url + '/cluster/options',
          verify = False,
          cookies = self._cookies,
          data = data,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        if res.status_code == 200:
            return MSG

    # Containers
    def get_all_ct(self, data):
        route = '/nodes/%s/lxc' % (data['node'])

        res = requests.get(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return res.json()['data']

    def get_nextid(self):
        route =  '/cluster/nextid'

        res = requests.get(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return int(res.json()['data'])

    def get_config_ct(self, data):
        route =  '/nodes/%s/lxc/%s/config' % (data['node'], data['vmid'])

        data.pop('node', None)
        data.pop('vmid', None)

        res = requests.get(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          data=data,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return res.json()['data']

    def get_snapshots(self, data):
        route =  '/nodes/%s/lxc/%s/snapshot' % (data['node'], data['vmid'])

        res = requests.get(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return res.json()['data']

    def get_snapshot(self, data):
        route =  '/nodes/%s/lxc/%s/snapshot/%s/config' % (data['node'], data['vmid'], data['snapname'])

        res = requests.get(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return res.json()['data']

    # Not test
    def create_ct(self, data):
        route = '/nodes/%s/lxc' % (data['node'])

        res = requests.post(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          data = data,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return res.json()['data']

    def start_ct(self, data):
        route = '/nodes/%s/lxc/%s/status/start' % (data['node'], data['vmid'])

        res = requests.post(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return MSG
    
    def stop_ct(self, data):
        route = '/nodes/%s/lxc/%s/status/stop' % (data['node'], data['vmid'])

        res = requests.post(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return MSG

    # Not test
    def suspend_ct(self, data):
        route = '/nodes/%s/lxc/%s/status/suspend' % (data['node'], data['vmid'])

        res = requests.post(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return MSG

    # Not test
    def shutdown_ct(self, data):
        route = '/nodes/%s/lxc/%s/status/shutdown' % (data['node'], data['vmid'])

        res = requests.post(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return MSG
    
    # Not test
    def resume_ct(self, data):
        route = '/nodes/%s/lxc/%s/status/resume' % (data['node'], data['vmid'])

        res = requests.post(
          self.api_url + route,
          verify = False,
          cookies = self._cookies,
          headers = { 'CSRFPreventionToken': self._token }
        )

        res.raise_for_status()

        return MSG

    # Not test
    def clone_ct(self, data):
        route = '/nodes/%s/lxc/%s/clone' % (data['node'], data['vmid'])

        nextid = self.get_nextid()

        res = requests.post(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          data={ "newid": nextid  },
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG

    def create_snapshot(self, data):
        route = '/nodes/%s/lxc/%s/snapshot' % (data['node'], data['vmid'])

        data.pop('node', None)
        data.pop('vmid', None)

        res = requests.post(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG

    def create_template(self, data):
        route = '/nodes/%s/lxc/%s/template' % (data['node'], data['vmid'])

        res = requests.post(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG

    def update_config_ct(self, data):
        route = '/nodes/%s/lxc/%s/config' % (data['node'], data['vmid'])

        data.pop('node', None)
        data.pop('vmid', None)

        res = requests.put(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG

    def update_snapshot(self, data):
        route = '/nodes/%s/lxc/%s/snapshot/%s/config' % (data['node'], data['vmid'], data['snapname'])

        data.pop('node', None)
        data.pop('vmid', None)
        data.pop('snapname', None)

        res = requests.put(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG
    
    # Fix me
    def resize_ct(self, data):
        route = '/nodes/%s/lxc/%s/resize' % (data['node'], data['vmid'])

        data.pop('node', None)
        data.pop('vmid', None)

        res = requests.put(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG
    
    def delete_snapshot(self, data):
        route = '/nodes/%s/lxc/%s/snapshot/%s' % (data['node'], data['vmid'], data['snapname'])

        data.pop('node', None)
        data.pop('vmid', None)
        data.pop('snapname', None)

        res = requests.delete(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG

    def delete_ct(self, data):
        route = '/nodes/%s/lxc/%s' % (data['node'], data['vmid'])

        res = requests.delete(
          self.api_url + route,
          verify=False,
          cookies=self._cookies,
          headers={ "CSRFPreventionToken": self._token }
        )
        
        res.raise_for_status()

        return MSG
